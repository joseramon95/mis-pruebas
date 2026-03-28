from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
    flash,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "e3-admin-secret-key-2026"

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///e3_admin.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/debug/db")
def debug_db():
    db_url = os.environ.get("DATABASE_URL", "NOT SET")
    return jsonify(
        {
            "env_DATABASE_URL": db_url[:50] + "..."
            if db_url and len(db_url) > 50
            else db_url,
            "config_DATABASE_URL": app.config["SQLALCHEMY_DATABASE_URI"][:30] + "..."
            if app.config["SQLALCHEMY_DATABASE_URI"]
            else "None",
        }
    )


# Modelos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), default="editor")
    activo = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Socio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    imagen = db.Column(db.String(200), nullable=False)
    whatsapp = db.Column(db.String(200), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    orden = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Componente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    titulo = db.Column(db.String(200))
    subtitulo = db.Column(db.String(200))
    contenido = db.Column(db.Text)
    link = db.Column(db.String(200))
    extra_data = db.Column(db.Text)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    accion = db.Column(db.String(50), nullable=False)
    componente_afectado = db.Column(db.String(100))
    detalle = db.Column(db.Text)
    ip_address = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship("Usuario", backref="logs")


# Decorador para proteger rutas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


def log_accion(accion, componente=None, detalle=None):
    usuario_id = session.get("user_id")
    ip = request.remote_addr
    log = Log(
        usuario_id=usuario_id,
        accion=accion,
        componente_afectado=componente,
        detalle=detalle,
        ip_address=ip,
    )
    db.session.add(log)
    db.session.commit()


# Rutas de autenticación
@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and usuario.check_password(password) and usuario.activo:
            session["user_id"] = usuario.id
            session["username"] = usuario.username
            log_accion("LOGIN", detalle=f"Usuario {username} inició sesión")
            return redirect(url_for("dashboard"))

        flash("Usuario o contraseña incorrectos", "error")

    return render_template("login.html")


@app.route("/logout")
def logout():
    if "user_id" in session:
        log_accion("LOGOUT", detalle=f"Usuario {session.get('username')} cerró sesión")
    session.clear()
    return redirect(url_for("login"))


# Dashboard
@app.route("/dashboard")
@login_required
def dashboard():
    stats = {
        "socios": Socio.query.count(),
        "componentes": Componente.query.count(),
        "usuarios": Usuario.query.filter(Usuario.id != session["user_id"]).count(),
        "logs_hoy": Log.query.filter(
            db.func.date(Log.timestamp) == datetime.now().date()
        ).count(),
    }
    logs_recientes = Log.query.order_by(Log.timestamp.desc()).limit(10).all()
    return render_template("dashboard.html", stats=stats, logs=logs_recientes)


# CRUD Socios
@app.route("/socios")
@login_required
def listar_socios():
    socios = Socio.query.order_by(Socio.orden).all()
    return render_template("socios/lista.html", socios=socios)


@app.route("/socios/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_socio():
    if request.method == "POST":
        socio = Socio(
            nombre=request.form.get("nombre"),
            descripcion=request.form.get("descripcion"),
            imagen=request.form.get("imagen"),
            whatsapp=request.form.get("whatsapp"),
            orden=request.form.get("orden", 0),
        )
        db.session.add(socio)
        db.session.commit()
        log_accion("CREAR", "Socios", f"Nuevo socio: {socio.nombre}")
        flash("Socio creado exitosamente", "success")
        return redirect(url_for("listar_socios"))

    return render_template("socios/form.html", socio=None)


@app.route("/socios/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_socio(id):
    socio = Socio.query.get_or_404(id)

    if request.method == "POST":
        socio.nombre = request.form.get("nombre")
        socio.descripcion = request.form.get("descripcion")
        socio.imagen = request.form.get("imagen")
        socio.whatsapp = request.form.get("whatsapp")
        socio.orden = request.form.get("orden", 0)
        db.session.commit()
        log_accion("EDITAR", "Socios", f"Socio modificado: {socio.nombre}")
        flash("Socio actualizado", "success")
        return redirect(url_for("listar_socios"))

    return render_template("socios/form.html", socio=socio)


@app.route("/socios/eliminar/<int:id>", methods=["POST"])
@login_required
def eliminar_socio(id):
    socio = Socio.query.get_or_404(id)
    nombre = socio.nombre
    db.session.delete(socio)
    db.session.commit()
    log_accion("ELIMINAR", "Socios", f"Socio eliminado: {nombre}")
    flash("Socio eliminado", "success")
    return redirect(url_for("listar_socios"))


@app.route("/socios/toggle/<int:id>", methods=["POST"])
@login_required
def toggle_socio(id):
    socio = Socio.query.get_or_404(id)
    socio.activo = not socio.activo
    db.session.commit()
    estado = "activó" if socio.activo else "desactivó"
    log_accion("TOGGLE", "Socios", f"{estado} socio: {socio.nombre}")
    return jsonify({"success": True, "activo": socio.activo})


# CRUD Componentes
@app.route("/componentes")
@login_required
def listar_componentes():
    componentes = Componente.query.order_by(Componente.nombre).all()
    return render_template("componentes/lista.html", componentes=componentes)


@app.route("/componentes/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_componente(id):
    componente = Componente.query.get_or_404(id)

    if request.method == "POST":
        componente.titulo = request.form.get("titulo")
        componente.subtitulo = request.form.get("subtitulo")
        componente.contenido = request.form.get("contenido")
        componente.link = request.form.get("link")
        componente.extra_data = request.form.get("extra_data")
        db.session.commit()
        log_accion("EDITAR", componente.nombre, f"Contenido actualizado")
        flash("Componente actualizado", "success")
        return redirect(url_for("listar_componentes"))

    return render_template("componentes/form.html", componente=componente)


# CRUD Usuarios
@app.route("/usuarios")
@login_required
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template("usuarios/lista.html", usuarios=usuarios)


@app.route("/usuarios/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_usuario():
    if request.method == "POST":
        if Usuario.query.filter_by(username=request.form.get("username")).first():
            flash("El usuario ya existe", "error")
            return redirect(url_for("nuevo_usuario"))

        usuario = Usuario(
            username=request.form.get("username"), rol=request.form.get("rol", "editor")
        )
        usuario.set_password(request.form.get("password"))
        db.session.add(usuario)
        db.session.commit()
        log_accion("CREAR", "Usuarios", f"Nuevo usuario: {usuario.username}")
        flash("Usuario creado", "success")
        return redirect(url_for("listar_usuarios"))

    return render_template("usuarios/form.html", usuario=None)


@app.route("/usuarios/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)

    if request.method == "POST":
        if request.form.get("password"):
            usuario.set_password(request.form.get("password"))
        usuario.rol = request.form.get("rol", "editor")
        usuario.activo = request.form.get("activo") == "1"
        db.session.commit()
        log_accion("EDITAR", "Usuarios", f"Usuario modificado: {usuario.username}")
        flash("Usuario actualizado", "success")
        return redirect(url_for("listar_usuarios"))

    return render_template("usuarios/form.html", usuario=usuario)


@app.route("/usuarios/eliminar/<int:id>", methods=["POST"])
@login_required
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    if usuario.id == session["user_id"]:
        flash("No puedes eliminarte a ti mismo", "error")
        return redirect(url_for("listar_usuarios"))
    nombre = usuario.username
    db.session.delete(usuario)
    db.session.commit()
    log_accion("ELIMINAR", "Usuarios", f"Usuario eliminado: {nombre}")
    flash("Usuario eliminado", "success")
    return redirect(url_for("listar_usuarios"))


# Logs
@app.route("/logs")
@login_required
def ver_logs():
    page = request.args.get("page", 1, type=int)
    logs = Log.query.order_by(Log.timestamp.desc()).paginate(page=page, per_page=50)
    return render_template("logs.html", logs=logs)


# API para datos (para consumo externo)
@app.route("/api/socios")
def api_socios():
    socios = Socio.query.filter_by(activo=True).order_by(Socio.orden).all()
    return jsonify(
        [
            {
                "id": s.id,
                "title": s.nombre,
                "description": s.descripcion,
                "image": s.imagen,
                "contact": {"text": "Contactar por WhatsApp", "link": s.whatsapp},
            }
            for s in socios
        ]
    )


@app.route("/api/componentes")
def api_componentes():
    componentes = Componente.query.all()
    return jsonify(
        [
            {
                "nombre": c.nombre,
                "titulo": c.titulo,
                "subtitulo": c.subtitulo,
                "contenido": c.contenido,
                "link": c.link,
                "extra_data": c.extra_data,
            }
            for c in componentes
        ]
    )


# Inicializar base de datos
def init_db():
    with app.app_context():
        db.create_all()

        # Crear usuario root si no existe
        if not Usuario.query.filter_by(username="root").first():
            root = Usuario(username="root", rol="admin")
            root.set_password("root")
            db.session.add(root)

        # Crear componentes por defecto
        componentes_default = [
            {
                "nombre": "Hero",
                "titulo": "Nosotros Resolvemos",
                "subtitulo": "Tus Problemas",
                "contenido": "Soluciones estratégicas de alta complejidad para transformar tu incertidumbre en crecimiento.",
            },
            {
                "nombre": "Features",
                "titulo": "La Arquitectura de la Certeza...",
                "subtitulo": "En un mercado definido...",
                "contenido": "",
            },
            {
                "nombre": "AboutUs",
                "titulo": "Quiénes Somos",
                "subtitulo": "E³: Consultora especializada...",
                "contenido": "",
            },
            {
                "nombre": "MisionVision",
                "titulo": "Misión y Visión",
                "subtitulo": "",
                "contenido": "",
            },
            {
                "nombre": "CTA",
                "titulo": "Listo Para Construir...",
                "subtitulo": "Comienza a construir...",
                "contenido": "",
            },
            {
                "nombre": "Contact",
                "titulo": "Contacto",
                "subtitulo": "¿Tienes preguntas?...",
                "contenido": "",
            },
        ]

        for c in componentes_default:
            if not Componente.query.filter_by(nombre=c["nombre"]).first():
                db.session.add(Componente(**c))

        db.session.commit()


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
