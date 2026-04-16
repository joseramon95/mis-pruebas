from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
    flash,
)
from app import db
from app.utils.auth import login_required, log_accion
import json

bp = Blueprint("crud", __name__, url_prefix="")


# ===== Socios =====
@bp.route("/socios")
@login_required
def listar_socios():
    from app.models import Socio

    socios = Socio.query.order_by(Socio.orden).all()
    return render_template("socios/lista.html", socios=socios)


@bp.route("/socios/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_socio():
    from app.models import Socio

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
        return redirect(url_for("crud.listar_socios"))
    return render_template("socios/form.html", socio=None)


@bp.route("/socios/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_socio(id):
    from app.models import Socio

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
        return redirect(url_for("crud.listar_socios"))
    return render_template("socios/form.html", socio=socio)


@bp.route("/socios/eliminar/<int:id>", methods=["POST"])
@login_required
def eliminar_socio(id):
    from app.models import Socio

    socio = Socio.query.get_or_404(id)
    nombre = socio.nombre
    db.session.delete(socio)
    db.session.commit()
    log_accion("ELIMINAR", "Socios", f"Socio eliminado: {nombre}")
    flash("Socio eliminado", "success")
    return redirect(url_for("crud.listar_socios"))


@bp.route("/socios/toggle/<int:id>", methods=["POST"])
@login_required
def toggle_socio(id):
    from app.models import Socio

    socio = Socio.query.get_or_404(id)
    socio.activo = not socio.activo
    db.session.commit()
    estado = "activó" if socio.activo else "desactivó"
    log_accion("TOGGLE", "Socios", f"{estado} socio: {socio.nombre}")
    return jsonify({"success": True, "activo": socio.activo})


# ===== Componentes =====
@bp.route("/componentes")
@login_required
def listar_componentes():
    from app.models import Componente

    componentes = Componente.query.order_by(Componente.nombre).all()
    return render_template("componentes/lista.html", componentes=componentes)


@bp.route("/componentes/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_componente(id):
    from app.models import Componente

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
        return redirect(url_for("crud.listar_componentes"))
    return render_template("componentes/form.html", componente=componente)


# ===== Casos =====
@bp.route("/casos")
@login_required
def listar_casos():
    from app.models import CasoExito

    casos = CasoExito.query.order_by(CasoExito.orden).all()
    return render_template("casos/lista.html", casos=casos, no_cabecera=True)


@bp.route("/casos/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_caso():
    from app.models import CasoExito

    if request.method == "POST":
        resultados_text = request.form.get("resultados", "")
        resultados_json = (
            json.dumps([r.strip() for r in resultados_text.split("\n") if r.strip()])
            if resultados_text.strip()
            else None
        )
        caso = CasoExito(
            slug=request.form.get("slug"),
            titulo=request.form.get("titulo"),
            descripcion=request.form.get("descripcion", ""),
            imagen=request.form.get("imagen", ""),
            contenido=request.form.get("contenido", ""),
            resultados=resultados_json,
            autor_testimonio=request.form.get("autor_testimonio", ""),
            cargo_testimonio=request.form.get("cargo_testimonio", ""),
            texto_testimonio=request.form.get("texto_testimonio", ""),
            orden=int(request.form.get("orden", 0)) if request.form.get("orden") else 0,
        )
        db.session.add(caso)
        db.session.commit()
        log_accion("CREAR", "Casos", f"Nuevo caso: {caso.titulo}")
        flash("Caso de éxito creado", "success")
        return redirect(url_for("crud.listar_casos"))
    return render_template("casos/form.html", caso=None)


@bp.route("/casos/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_caso(id):
    from app.models import CasoExito

    caso = CasoExito.query.get_or_404(id)
    if request.method == "POST":
        resultados_text = request.form.get("resultados", "")
        caso.resultados = (
            json.dumps([r.strip() for r in resultados_text.split("\n") if r.strip()])
            if resultados_text.strip()
            else None
        )
        caso.slug = request.form.get("slug")
        caso.titulo = request.form.get("titulo")
        caso.descripcion = request.form.get("descripcion", "")
        caso.imagen = request.form.get("imagen", "")
        caso.contenido = request.form.get("contenido", "")
        caso.autor_testimonio = request.form.get("autor_testimonio", "")
        caso.cargo_testimonio = request.form.get("cargo_testimonio", "")
        caso.texto_testimonio = request.form.get("texto_testimonio", "")
        caso.orden = (
            int(request.form.get("orden", 0)) if request.form.get("orden") else 0
        )
        db.session.commit()
        log_accion("EDITAR", "Casos", f"Caso modificado: {caso.titulo}")
        flash("Caso de éxito actualizado", "success")
        return redirect(url_for("crud.listar_casos"))
    resultados_list = []
    if caso.resultados:
        try:
            resultados_list = json.loads(caso.resultados)
        except:
            pass
    return render_template("casos/form.html", caso=caso, resultados=resultados_list)


@bp.route("/casos/eliminar/<int:id>", methods=["POST"])
@login_required
def eliminar_caso(id):
    from app.models import CasoExito

    caso = CasoExito.query.get_or_404(id)
    titulo = caso.titulo
    db.session.delete(caso)
    db.session.commit()
    log_accion("ELIMINAR", "Casos", f"Caso eliminado: {titulo}")
    flash("Caso de éxito eliminado", "success")
    return redirect(url_for("crud.listar_casos"))


@bp.route("/casos/toggle/<int:id>", methods=["POST"])
@login_required
def toggle_caso(id):
    from app.models import CasoExito

    caso = CasoExito.query.get_or_404(id)
    caso.activo = not caso.activo
    db.session.commit()
    estado = "activó" if caso.activo else "desactivó"
    log_accion("TOGGLE", "Casos", f"{estado} caso: {caso.titulo}")
    return jsonify({"success": True, "activo": caso.activo})


# ===== Usuarios =====
@bp.route("/usuarios")
@login_required
def listar_usuarios():
    from app.models import Usuario

    usuarios = Usuario.query.all()
    return render_template("usuarios/lista.html", usuarios=usuarios)


@bp.route("/usuarios/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_usuario():
    from app.models import Usuario

    if request.method == "POST":
        if Usuario.query.filter_by(username=request.form.get("username")).first():
            flash("El usuario ya existe", "error")
            return redirect(url_for("crud.nuevo_usuario"))
        usuario = Usuario(
            username=request.form.get("username"), rol=request.form.get("rol", "editor")
        )
        usuario.set_password(request.form.get("password"))
        db.session.add(usuario)
        db.session.commit()
        log_accion("CREAR", "Usuarios", f"Nuevo usuario: {usuario.username}")
        flash("Usuario creado", "success")
        return redirect(url_for("crud.listar_usuarios"))
    return render_template("usuarios/form.html", usuario=None)


@bp.route("/usuarios/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_usuario(id):
    from app.models import Usuario

    usuario = Usuario.query.get_or_404(id)
    if request.method == "POST":
        if request.form.get("password"):
            usuario.set_password(request.form.get("password"))
        usuario.rol = request.form.get("rol", "editor")
        usuario.activo = request.form.get("activo") == "1"
        db.session.commit()
        log_accion("EDITAR", "Usuarios", f"Usuario modificado: {usuario.username}")
        flash("Usuario actualizado", "success")
        return redirect(url_for("crud.listar_usuarios"))
    return render_template("usuarios/form.html", usuario=usuario)


@bp.route("/usuarios/eliminar/<int:id>", methods=["POST"])
@login_required
def eliminar_usuario(id):
    from app.models import Usuario

    usuario = Usuario.query.get_or_404(id)
    if usuario.id == session["user_id"]:
        flash("No puedes eliminarte a ti mismo", "error")
        return redirect(url_for("crud.listar_usuarios"))
    nombre = usuario.username
    db.session.delete(usuario)
    db.session.commit()
    log_accion("ELIMINAR", "Usuarios", f"Usuario eliminado: {nombre}")
    flash("Usuario eliminado", "success")
    return redirect(url_for("crud.listar_usuarios"))


# ===== Logs =====
@bp.route("/logs")
@login_required
def ver_logs():
    from app.models import Log

    page = request.args.get("page", 1, type=int)
    logs = Log.query.order_by(Log.timestamp.desc()).paginate(page=page, per_page=50)
    return render_template("logs.html", logs=logs)
