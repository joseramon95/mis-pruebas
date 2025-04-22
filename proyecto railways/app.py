from flask import Flask, render_template, session, redirect, url_for
from config import config
# from gui import iniciar_gui  # Importa la interfaz gráfica

# Recordatorio: hacer trigger para eliminar tareas completas de la base de datos

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta_segura'  # Necesaria para usar sesiones

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login")
def login():
    return render_template("auth/login.html")

@app.route('/home')
def home():
    return render_template('auth/home.html')

@app.route('/register')
def register():
    return render_template('auth/register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.config.from_object(config['develoment'])
    app.run(debug=True)

