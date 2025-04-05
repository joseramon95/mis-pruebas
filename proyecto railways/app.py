from flask import Flask
# from gui import iniciar_gui  # Importa la interfaz gráfica

#recordatorio hacer trigger para eliminar tareas completas de la base de datos

app = Flask(__name__)

if __name__ == "__main__":
  #  iniciar_gui()  # Lanza la interfaz Tkinter
    app.run(debug=True)  # Inicia Flask 
