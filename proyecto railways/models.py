import sqlite3

# se conecta a la base de datos
def conectar_bd():

    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def crear_tarea (nombre_usuario, tarea, porcentaje):
    conn = conectar_bd()
    try: 
        cursor = conn.cursor()
        cursor.execute(
                "INSERT INTO tareas (id_usuario, nombre_tarea, porcentaje) VALUES (?, ?, ?)",
                (id_usuario, nombre_tarea, porcentaje) 
            )
        conn.commit()
        return cursor.lastrowid() # da el id de la nueva tarea
    except exeption as e :
        conn.rollback() #dezhace cambio si algo sale mal
        raise e # se lanza alerta para que no deje de funcionar el programa
    finally:
        conn.close()