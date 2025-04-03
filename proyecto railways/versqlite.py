import sqlite3

#connecion a la base de datos
conn = sqlite3.connect('Gestor_de_Tareas')
cursor = conn.cursor()

#llamar las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

print ("tablas en la base de datos:")
for tabla in tablas:
    print(tabla[0])

#cerrar coneccion
conn.close()