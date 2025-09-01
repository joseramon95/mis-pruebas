from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db, login_manager
from models import User, Tarea
from utils import autenticar_usuario
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecreto')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Gestor_de_Tareas.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    # Crear todas las tablas definidas en los modelos

    # Mensajes globales de login
    login_manager.login_message = "Debes iniciar sesión primero"
    login_manager.login_message_category = "alert-danger"

    with app.app_context():
        db.create_all()  # crea tablas si no existen

    return app

app = create_app()


@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Buscar usuario
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)  # Marca al usuario como logueado
            return redirect(url_for('home'))
        else:
            return render_template('auth/login.html', error="Usuario o contraseña incorrectos")

    return render_template('auth/login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar si el usuario ya existe
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('auth/register.html', error="El usuario ya existe")

        # Crear nuevo usuario con contraseña hasheada
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Iniciar sesión automáticamente
        session['username'] = username
        return redirect(url_for('home'))

    # Si es GET, mostrar formulario
    return render_template('auth/register.html')

@app.route("/tarea/<int:id>", methods=['GET', 'PUT', 'DELETE'])
@login_required
def manejar_tarea(id):
    # Obtener la tarea
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({"error": "Tarea no encontrada"}), 404

    # Solo el dueño puede modificar o eliminar
    if tarea.user_id != current_user.id:
        return jsonify({"error": "No autorizado"}), 403

    if request.method == 'GET':
        # Devolver la tarea en JSON
        return jsonify({
            "id": tarea.id,
            "titulo": tarea.titulo,
            "descripcion": tarea.descripcion
        })

    elif request.method == 'PUT':
        data = request.get_json()  # Recibir JSON desde JS
        tarea.titulo = data.get("titulo", tarea.titulo)
        tarea.descripcion = data.get("descripcion", tarea.descripcion)
        db.session.commit()
        return jsonify({"success": True, "tarea": {
            "id": tarea.id,
            "titulo": tarea.titulo,
            "descripcion": tarea.descripcion
        }})

    elif request.method == 'DELETE':
        db.session.delete(tarea)
        db.session.commit()
        return jsonify({"success": True, "message": "Tarea eliminada"})
    # DELETE → eliminar tarea
    elif request.method == 'DELETE':
        db.session.delete(tarea)
        db.session.commit()
        return jsonify({"mensaje": "Tarea eliminada"})


@app.route("/add_tarea", methods=['GET', 'POST'])
@login_required
def add_tarea():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form.get('descripcion', '')
        nueva_tarea = Tarea(
            titulo=titulo,
            descripcion=descripcion,
            user_id=current_user.id
        )
        db.session.add(nueva_tarea)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('auth/add_tarea.html')

@app.route("/home", methods=['POST', 'GET', 'PUT', 'DELETE'])
@login_required
def home():
    tareas = Tarea.query.filter_by(user_id=current_user.id).all()
    return render_template('auth/home.html', tareas=tareas)
    

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)





