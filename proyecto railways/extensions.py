<<<<<<< HEAD:extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'  # si el usuario no está logueado, va a /login
=======
# extensions.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
>>>>>>> 049ad2247eab6cf7880927b972c46d30af2df293:proyecto railways/extensions.py
