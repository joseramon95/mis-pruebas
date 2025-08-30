import sqlite3

# se conecta a la base de datos
def conectar_bd():
    conn = sqlite3.conect('Gestor_de_Tareas.sqlite')
    cursor = conn.cursor()
    cursor.execute ('''CREATE TABLE IF NOT EXIST tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_tarea TEXT, 
    id_usuario INTEGER,
    porcentaje INTEGER)''')


    conn = sqlite3.conect('Gestor_de_Tareas.sqlite')
    cursor = conn.cursor()
    cursor.execute ('''CREATE TABLE IF NOT EXIST usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_usuario TEXT NOT NULL, 
    numero_telefonico INTEGER NOT NULL,
    email varchar TEXT)''')

    conn.commit()
    return conn

def crear_tarea (nombre_tarea, id_usuario, porcentaje):
    conn = conectar_bd()
    try: 
        cursor = conn.cursor()
        cursor.execute(
                "INSERT INTO tareas (nombre_tarea, id_usuario, porcentaje) VALUES (?, ?, ?)",
                (id_usuario, nombre_tarea, porcentaje) 
            )
        conn.commit()
        return cursor.lastrowid() # da el id de la nueva tarea
    except exeption as e :
        conn.rollback() #dezhace cambio si algo sale mal
        raise e # se lanza alerta para que no deje de funcionar el programa
    finally:
        conn.close()


def crear_usuario (nombre_usuario, numero_telefonico, email):
    conn = conectar_bd()
    try: 
        cursor = conn.cursor()
        cursor.execute(
                "INSERT INTO tareas (nnombre_usuario, numero_telefonico, email) VALUES (?, ?, ?)",
                (nombre_usuario, numero_telefonico, email) 
            )
        conn.commit()
        return cursor.lastrowid() # da el id del nuevo usuario
    except exeption as e :
        conn.rollback() #dezhace cambio si algo sale mal
        raise e # se lanza alerta para que no deje de funcionar el programa
    finally:
        conn.close()