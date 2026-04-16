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

bp = Blueprint("auth", __name__, url_prefix="")


@bp.route("/login", methods=["GET", "POST"])
def login():
    from app.models import Usuario
    from app.utils.auth import check_basic_auth, log_accion

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
            return redirect(url_for("dashboard.dashboard"))

        flash("Usuario o contraseña incorrectos", "error")

    return render_template("login.html")


@bp.route("/logout")
def logout():
    from app.utils.auth import log_accion

    if "user_id" in session:
        log_accion("LOGOUT", detalle=f"Usuario {session.get('username')} cerró sesión")
    session.clear()
    return redirect(url_for("auth.login"))
