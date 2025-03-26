import sqlite3


DATABASE_NAME = "Gestor_de_Tareas.sqlite"


def conectar_bd():

    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def jls_extract_def():
    return """
            CREATE TABLE IF NOT EXISTS tareas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuarios INTEGER,
                nombre_tarea varchar (50),
                porcentaje INTEGER ,
            )
        """


def crear_tabla():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre_usuario TEXT NOT NULL,

            numero_telefonico INTEGER NOT NULL

            email varchar (50)

            password_hash varchar (50)
        )
    """)

    cursor.execute(jls_extract_def())

    conn.commit()

    conn.close()


crear_tabla()  # Se ejecuta al iniciar el programa

