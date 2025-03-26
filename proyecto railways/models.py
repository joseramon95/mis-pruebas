from database import conectar_bd

def agregar_producto(nombre, cantidad):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, cantidad) VALUES (?, ?)", (nombre, cantidad))
    conn.commit()
    conn.close()

def obtener_productos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos
