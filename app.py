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
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = "e3-admin-secret-key-2026"

DATABASE_URL = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

is_production = (
    os.environ.get("FLASK_ENV") == "production"
    or "render" in os.environ.get("HOSTNAME", "").lower()
)


@app.before_request
def before_request():
    if is_production:
        app.config["SESSION_COOKIE_SAMESITE"] = "None"
        app.config["SESSION_COOKIE_SECURE"] = True
    else:
        app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
        app.config["SESSION_COOKIE_SECURE"] = False


CORS(
    app,
    resources={r"/api/*": {"origins": ["*"], "supports_credentials": True}},
    allow_headers=["*"],
    expose_headers=["*"],
)
CORS(
    app,
    resources={r"/health": {"origins": ["*"]}},
    allow_headers=["*"],
    expose_headers=["*"],
)
CORS(
    app,
    resources={r"/login": {"origins": ["*"], "supports_credentials": True}},
    allow_headers=["*"],
    expose_headers=["*"],
)
CORS(
    app,
    resources={r"/dashboard": {"origins": ["*"], "supports_credentials": True}},
    allow_headers=["*"],
    expose_headers=["*"],
)
CORS(
    app,
    resources={r"/logout": {"origins": ["*"], "supports_credentials": True}},
    allow_headers=["*"],
    expose_headers=["*"],
)
CORS(
    app,
    resources={r"/api/socios*": {"origins": ["*"], "supports_credentials": True}},
    allow_headers=["*"],
    expose_headers=["*"],
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
    imagen = db.Column(db.Text, nullable=False)
    whatsapp = db.Column(db.Text, nullable=False)
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


class CasoExito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text)
    imagen = db.Column(db.Text)
    contenido = db.Column(db.Text)
    resultados = db.Column(db.Text)
    autor_testimonio = db.Column(db.String(100))
    cargo_testimonio = db.Column(db.String(100))
    texto_testimonio = db.Column(db.Text)
    activo = db.Column(db.Boolean, default=True)
    orden = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# Decorador para proteger rutas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


def check_basic_auth():
    auth = request.authorization
    if auth and auth.username and auth.password:
        usuario = Usuario.query.filter_by(username=auth.username).first()
        if usuario and usuario.check_password(auth.password) and usuario.activo:
            session["user_id"] = usuario.id
            session["username"] = usuario.username
            return True
    return False


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
    if request.method == "GET" and request.authorization:
        if check_basic_auth():
            return jsonify({"authenticated": True, "username": session.get("username")})
        return jsonify({"authenticated": False}), 401

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


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


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
        orden_value = request.form.get("orden")
        try:
            orden_value = int(orden_value) if orden_value else 0
        except ValueError:
            orden_value = 0
        socio = Socio(
            nombre=request.form.get("nombre"),
            descripcion=request.form.get("descripcion"),
            imagen=request.form.get("imagen"),
            whatsapp=request.form.get("whatsapp"),
            orden=orden_value,
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
        orden_value = request.form.get("orden")
        try:
            socio.orden = int(orden_value) if orden_value else 0
        except ValueError:
            socio.orden = 0
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
                "contact": {"text": "Contactar", "link": s.whatsapp},
            }
            for s in socios
        ]
    )


@app.route("/api/socios/all")
def api_socios_all():
    if "user_id" not in session and not check_basic_auth():
        return jsonify({"error": "No autenticado"}), 401
    socios = Socio.query.order_by(Socio.orden).all()
    return jsonify(
        [
            {
                "id": s.id,
                "nombre": s.nombre,
                "descripcion": s.descripcion,
                "imagen": s.imagen,
                "whatsapp": s.whatsapp,
                "activo": s.activo,
                "orden": s.orden,
            }
            for s in socios
        ]
    )


@app.route("/api/socios", methods=["POST"])
def api_socios_create():
    if "user_id" not in session and not check_basic_auth():
        return jsonify({"error": "No autenticado"}), 401
    data = request.get_json()
    try:
        orden_value = data.get("orden", 0)
        socio = Socio(
            nombre=data.get("nombre"),
            descripcion=data.get("descripcion", ""),
            imagen=data.get("imagen", ""),
            whatsapp=data.get("whatsapp", ""),
            orden=int(orden_value) if orden_value else 0,
        )
        db.session.add(socio)
        db.session.commit()
        log_accion("CREAR", "Socios", f"Nuevo socio: {socio.nombre}")
        return jsonify({"success": True, "id": socio.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/socios/<int:id>", methods=["PUT"])
def api_socios_update(id):
    if "user_id" not in session and not check_basic_auth():
        return jsonify({"error": "No autenticado"}), 401
    socio = Socio.query.get_or_404(id)
    data = request.get_json()
    try:
        socio.nombre = data.get("nombre", socio.nombre)
        socio.descripcion = data.get("descripcion", socio.descripcion)
        socio.imagen = data.get("imagen", socio.imagen)
        socio.whatsapp = data.get("whatsapp", socio.whatsapp)
        socio.orden = data.get("orden", socio.orden)
        db.session.commit()
        log_accion("EDITAR", "Socios", f"Socio modificado: {socio.nombre}")
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/socios/<int:id>", methods=["DELETE"])
def api_socios_delete(id):
    if "user_id" not in session and not check_basic_auth():
        return jsonify({"error": "No autenticado"}), 401
    socio = Socio.query.get_or_404(id)
    nombre = socio.nombre
    db.session.delete(socio)
    db.session.commit()
    log_accion("ELIMINAR", "Socios", f"Socio eliminado: {nombre}")
    return jsonify({"success": True})


@app.route("/api/socios/<int:id>/toggle", methods=["POST"])
def api_socios_toggle(id):
    if "user_id" not in session and not check_basic_auth():
        return jsonify({"error": "No autenticado"}), 401
    socio = Socio.query.get_or_404(id)
    socio.activo = not socio.activo
    db.session.commit()
    estado = "activó" if socio.activo else "desactivó"
    log_accion("TOGGLE", "Socios", f"{estado} socio: {socio.nombre}")
    return jsonify({"success": True, "activo": socio.activo})


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


@app.route("/api/componentes/<nombre>")
def api_componente_nombre(nombre):
    componente = Componente.query.filter_by(nombre=nombre).first()
    if not componente:
        return jsonify({"error": "Componente no encontrado"}), 404
    return jsonify(
        {
            "nombre": componente.nombre,
            "titulo": componente.titulo,
            "subtitulo": componente.subtitulo,
            "contenido": componente.contenido,
            "link": componente.link,
            "extra_data": componente.extra_data,
        }
    )


@app.route("/api/contenido/soluciones")
def api_soluciones():
    casos = CasoExito.query.filter_by(activo=True).order_by(CasoExito.orden).all()
    testimonios = []
    for c in casos:
        if c.texto_testimonio:
            testimonios.append(
                {
                    "autor": c.autor_testimonio,
                    "cargo": c.cargo_testimonio,
                    "texto": c.texto_testimonio,
                }
            )
        else:
            testimonios.append(None)

    return jsonify(
        {
            "titulo": "Casos de Éxito",
            "subtitulo": "Descubre cómo hemos ayudado a organizaciones a transformar su incertidumbre en crecimiento.",
            "casos": [
                {
                    "id": c.id,
                    "slug": c.slug,
                    "titulo": c.titulo,
                    "descripcion": c.descripcion,
                    "imagen": c.imagen,
                    "testimonio": testimonios[i],
                }
                for i, c in enumerate(casos)
            ],
        }
    )


@app.route("/api/contenido/soluciones/<slug>")
def api_solucion_detalle(slug):
    caso = CasoExito.query.filter_by(slug=slug, activo=True).first()
    if not caso:
        return jsonify({"error": "Caso no encontrado"}), 404

    import json

    resultados = []
    if caso.resultados:
        try:
            resultados = json.loads(caso.resultados)
        except:
            resultados = []

    testimonio = None
    if caso.texto_testimonio:
        testimonio = {
            "autor": caso.autor_testimonio,
            "cargo": caso.cargo_testimonio,
            "texto": caso.texto_testimonio,
        }

    return jsonify(
        {
            "id": caso.id,
            "slug": caso.slug,
            "titulo": caso.titulo,
            "descripcion": caso.descripcion,
            "imagen": caso.imagen,
            "contenido": caso.contenido,
            "resultados": resultados,
            "testimonio": testimonio,
        }
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

        # Crear casos de ejemplo si no existen
        casos_default = [
            {
                "slug": "transformacion-empresarial",
                "titulo": "Transformación Empresarial",
                "descripcion": "Implementación de estrategia integral de resiliencia organizacional.",
                "imagen": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=600",
                "contenido": "Trabajamos con una empresa del sector manufacturero para transformar su estructura organizacional.",
                "resultados": '["Incremento del 40% en eficiencia operativa", "Reducción del 25% en costos de operación"]',
            },
            {
                "slug": "analisis-de-mercado",
                "titulo": "Análisis de Mercado",
                "descripcion": "Estudio profundo del sector que permitió decisiones estratégicas fundamentadas.",
                "imagen": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600",
                "contenido": "Realizamos un análisis exhaustivo del mercado.",
                "resultados": '["Identificación de 3 nuevos segmentos de mercado", "Incremento del 60% en clientes"]',
            },
            {
                "slug": "planificacion-estrategica",
                "titulo": "Planificación Estratégica",
                "descripcion": "Desarrollo de hoja de ruta para expansión con análisis de riesgo.",
                "imagen": "https://images.unsplash.com/photo-1553877522-43269d4ea984?w=600",
                "contenido": "Desarrollamos un plan estratégico completo.",
                "resultados": '["Plan de expansión a 3 nuevos mercados", "Estructura organizacional para escalar 10x"]',
            },
        ]

        for c in casos_default:
            if not CasoExito.query.filter_by(slug=c["slug"]).first():
                db.session.add(CasoExito(**c))

        db.session.commit()


init_db()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
