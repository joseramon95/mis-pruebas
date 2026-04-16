from flask import Blueprint, render_template, session
from app import db
from datetime import datetime
from app.utils.auth import login_required

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route("")
@bp.route("/")
@login_required
def dashboard():
    from app.models import Socio, Componente, Usuario, Log, CasoExito

    stats = {
        "socios": Socio.query.count(),
        "componentes": Componente.query.count(),
        "usuarios": Usuario.query.filter(Usuario.id != session["user_id"]).count(),
        "logs_hoy": Log.query.filter(
            db.func.date(Log.timestamp) == datetime.now().date()
        ).count(),
        "casos_exito": CasoExito.query.count(),
    }
    logs_recientes = Log.query.order_by(Log.timestamp.desc()).limit(10).all()
    return render_template("dashboard.html", stats=stats, logs=logs_recientes)
