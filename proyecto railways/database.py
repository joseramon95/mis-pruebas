import sqlite3


DATABASE_NAME = "Gestor_de_Tareas.sqlite"

#se crea la base de datos
def conectar_bd():

    conn = sqlite3.connect(DATABASE_NAME)
    return conn

#funcion para crear tabla tareas
def jls_extract_def():
    return """
            CREATE TABLE IF NOT EXISTS tareas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuarios INTEGER,
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

