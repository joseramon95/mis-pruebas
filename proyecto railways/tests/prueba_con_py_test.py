import pytest
import sqlite3

@pytest.fixture
def setup_db():
    # Crea la base de datos en memoria y la tabla para los artículos
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    # Crea la tabla 'articulos'
    cursor.execute("CREATE TABLE articulos (codigo INTEGER PRIMARY KEY, nombre TEXT, precio REAL)")
    # Inserta un producto de prueba
    cursor.execute("INSERT INTO articulos (codigo, nombre, precio) VALUES (1, 'Producto de prueba', 50.0)")
    connection.commit()
    yield connection, cursor
    connection.close()

@pytest.mark.repeat(5)  # Repite la prueba 3 veces
def test_modificar_producto(setup_db):
    connection, cursor = setup_db

    nuevo_nombre = 'Producto modificado'
    nuevo_precio = 500

    # Ejecuta la modificación
    cursor.execute("UPDATE articulos SET nombre = ?, precio = ? WHERE codigo = ?", 
                   (nuevo_nombre, nuevo_precio, 1))
    connection.commit()

    # Verifica que el producto haya sido modificado
    cursor.execute("SELECT * FROM articulos WHERE codigo = ?", (1,))
    producto = cursor.fetchone()

    assert producto is not None
    assert producto[1] == nuevo_nombre
    assert producto[2] == nuevo_precio

if __name__ == '__main__':
    pytest.main()
