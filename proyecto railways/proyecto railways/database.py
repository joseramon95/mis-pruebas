import os
import sqlite3

# Obtener la ruta ABSOLUTA 
BASE_DIR = os.path.dirname(os.path.abspath('_file_'))
DATABASE_NAME = os.path.join(BASE_DIR, "Gestor_de_Tareas.sqlite")  # Ruta completa

print("Directorio del proyecto:", os.path.dirname(os.path.abspath('_file_')))
print("Ruta de la base de datos:", DATABASE_NAME)


#funcion para crear tabla tareas
def jls_extract_def():
    return """
            CREATE TABLE IF NOT EXISTS tareas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                nombre_tarea varchar (50),
                porcentaje INTEGER
            )
        """

#funcion para crear tabla usuarios
#no se pone coma en el ultimo comando por que da error
def crear_tabla():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre_usuario TEXT NOT NULL,

            numero_telefonico INTEGER NOT NULL,

            email TEXT,

            password_hash TEXT 
        ) 
    """)
    # se ejecuta la funcio donde se crean la tabla ya que no cree la tabla con cursor.execute
    cursor.execute(jls_extract_def())

    conn.commit()

    conn.close()


crear_tabla()  # Se ejecuta al iniciar el programa

