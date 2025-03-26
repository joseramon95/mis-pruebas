from flask import Flask
from gui import iniciar_gui  # Importa la interfaz gráfica

app = Flask(__name__)

if __name__ == "__main__":
    iniciar_gui()  # Lanza la interfaz Tkinter
    app.run(debug=True)  # Inicia Flask (opcional si decides agregar API)
