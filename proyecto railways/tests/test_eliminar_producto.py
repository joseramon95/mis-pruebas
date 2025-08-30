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
    def test_eliminar_producto(self, mock_connect):
        mock_connect.return_value = self.connection

        # Mock del código del producto a eliminar
        id_producto = MagicMock()
        id_producto.return_value = 1 

        try:
            # Ejecuta la eliminación
            self.cursor.execute("DELETE FROM articulos WHERE codigo = ?", (id_producto.return_value,))
            self.connection.commit()

            # Verifica que el producto haya sido eliminado
            self.cursor.execute("SELECT * FROM articulos WHERE codigo = ?", (id_producto.return_value,))
            producto = self.cursor.fetchone()

            # Si el producto aún existe, lanzamos una excepción
            if producto is not None:
                raise Exception(f"El ID del producto {id_producto.return_value} no ha sido eliminado.")

        except sqlite3.Error as e:
            # Captura errores relacionados con SQLite
            print(f"Error en la base de datos: {str(e)}")
            self.fail(f"Test falló debido a un error en la base de datos: {str(e)}")

        except Exception as e:
            # Captura cualquier otra excepción
            print(f"Error: {str(e)}")
            self.fail(f"Test falló debido a: {str(e)}")

        # Asegura que el producto haya sido eliminado (producto debería ser None)
        self.assertIsNone(producto)

if __name__ == '__main__':
    unittest.main()
