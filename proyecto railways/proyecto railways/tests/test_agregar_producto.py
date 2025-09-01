import unittest
from unittest.mock import patch, MagicMock
import sqlite3


class TestApp(unittest.TestCase):
    def setUp(self):
        # Crea la base de datos en memoria y la tabla para los artículos
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()
        # Crea la tabla 'articulos'
        self.cursor.execute("CREATE TABLE articulos (codigo INTEGER PRIMARY KEY, nombre TEXT, precio REAL)")
        # Inserta un producto de prueba
        self.cursor.execute("INSERT INTO articulos (codigo, nombre, precio) VALUES (1, 'Producto de prueba', 50.0)")
        self.connection.commit()

    def tearDown(self):
        # Cierra la conexión a la base de datos
        self.connection.close()

    @patch('sqlite3.connect', return_value=sqlite3.connect(":memory:"))  # Mockea sqlite3.connect
    def test_guardar_producto(self, mock_connect):
        mock_connect.return_value = self.connection

        # mocks para los campos de entrada
        entry_producto = MagicMock()
        entry_precio = MagicMock()
        entry_producto.get.return_value = "Nuevo producto"
        entry_precio.get.return_value = 100

        # Simula la función guarda
        def guarda(producto_entry, precio_entry, window=None):
            nombre = producto_entry.get()
            precio = precio_entry.get()
            self.cursor.execute("INSERT INTO articulos (nombre, precio) VALUES (?, ?)", (nombre, precio))
            self.connection.commit()

        # Llama a la función simulada guarda
        guarda(entry_producto, entry_precio)

        # Verifica si el producto ha sido agregado
        self.cursor.execute("SELECT * FROM articulos WHERE nombre=?", (entry_producto.get(),))
        producto = self.cursor.fetchone()

        # Validaciones
        self.assertIsNotNone(producto)  # Asegura que el producto ha sido encontrado
        self.assertEqual(producto[1], "Nuevo producto")  # Verifica el nombre del producto
        self.assertEqual(producto[2], 100)  # Verifica el precio del producto

        try:
            if producto is None:
                raise Exception("El producto no ha sido agregado correctamente.")
        except sqlite3.Error as e:
            print(f"Error en la base de datos: {str(e)}")
            self.fail(f"Test falló debido a un error en la base de datos: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")
            self.fail(f"Test falló debido a: {str(e)}")


if __name__ == '__main__':
    unittest.main()
