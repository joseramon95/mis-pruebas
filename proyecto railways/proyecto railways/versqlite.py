import sqlite3
import os

PROJECT_DIR = os.path.dirname(os.path.abspath('_file_'))
DB_PATH = os.path.join(PROJECT_DIR, 'Gestor_de_Tareas.sqlite')

def conectar_bd():
    print(f"\n Conectando a la base de datos en: {DB_PATH}")  # ¡Verifica esta ruta!
    conn = sqlite3.connect(DB_PATH)
    return conn

def verificar_tablas():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        
        # Verifica si la BD existe y tiene tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()
        
        if not tablas:
            print("\n¡La base de datos no tiene tablas!")
        else:
            print("\nTablas encontradas:")
            for tabla in tablas:
                print(f"- {tabla[0]}")
                
    except sqlite3.Error as e:
        print(f"\nError al verificar tablas: {e}")
    finally:
        if conn:
            conn.close()

verificar_tablas()