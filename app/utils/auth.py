from functools import wraps
from flask import redirect, url_for, request, session
from app.models import Usuario
from app import db


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
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
    from app.models import Log

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
