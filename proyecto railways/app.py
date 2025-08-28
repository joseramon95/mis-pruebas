from flask import Flask, render_template, session, redirect, url_for
from config import config
import os
# from gui import iniciar_gui  # Importa la interfaz gráfica

# Recordatorio: hacer trigger para eliminar tareas completas de la base de datos

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))  # Genera una clave secreta aleatoria # Necesaria para usar sesiones


@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST']) #arreglar los estilos del footer #se esta añadiendo los metodos de get y post
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # función de autenticación
        if autenticar_usuario(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('auth/login.html', error="Usuario o contraseña incorrectos")
    return render_template('auth/login.html')

@app.route('/home') #pendiente los futuros añadidos
def home():
    return render_template('auth/home.html')

@app.route('/register') # aun me falta que mande los datos a la base de datos posiblemente cambie a una como postgresql
def register():
    return render_template('auth/register.html')

@app.route('/logout') #ocupo hacer una funcion y pagina para salir
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.config.from_object(config['develoment'])
    app.run(debug=True)

