from flask import Flask, render_template, session, redirect, url_for, request
from config import config
import os
from extensions import db
import utils
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Gestor_de_Tareas.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

db.init_app(app)

# Crear tablas al iniciar la app
with app.app_context():
    import models
    db.create_all()

# ===== Rutas =====
@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if utils.autenticar_usuario(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('auth/login.html', error="Usuario o contraseña incorrectos")
    return render_template('auth/login.html')

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('auth/home.html', username=session['username'])


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        from models import User
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('auth/register.html', error="El usuario ya existe")

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        session['username'] = username
        return redirect(url_for('home'))

    return render_template('auth/register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# ===== Ejecutar app =====
if __name__ == "__main__":
    app.config.from_object(config['develoment'])
    app.run(debug=True)
