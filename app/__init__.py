from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # Buscar templates en la raíz del proyecto, no en app/
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(base_dir, "templates")

    app = Flask(__name__, template_folder=template_dir)
    app.config["SECRET_KEY"] = "e3-admin-secret-key-2026"

    DATABASE_URL = os.environ.get("LOCAL_DB_URL") or os.environ.get("DATABASE_URL")
    is_dev = os.environ.get("FLASK_ENV") == "development" or os.environ.get("DEBUG")
    if not DATABASE_URL and is_dev:
        DATABASE_URL = "sqlite:///dev.db"
        print("⚠️  Modo desarrollo: usando SQLite (dev.db)")
    elif not DATABASE_URL:
        raise RuntimeError(
            "DATABASE_URL no configurada. "
            "Para desarrollo usá LOCAL_DB_URL o FLASK_ENV=development"
        )
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

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

    from app.models import Usuario, Socio, Componente, CasoExito, Log
    from app.routes import auth, dashboard, crud, api

    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(crud.bp)
    app.register_blueprint(api.bp)

    @app.route("/")
    def index():
        from flask import redirect, url_for

        return redirect(url_for("auth.login"))

    @app.route("/dashboard")
    def dashboard():
        from flask import redirect, url_for

        return redirect(url_for("dashboard.dashboard"))

    @app.route("/health")
    def health():
        from flask import jsonify

        return jsonify({"status": "ok"})

    return app
