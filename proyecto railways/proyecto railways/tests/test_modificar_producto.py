import unittest
from unittest.mock import patch, MagicMock
import sqlite3
#---modifcar para hacer la prueba de modifcar---
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
    def test_modificar_producto(self, mock_connect):
        mock_connect.return_value = self.connection

        # Mock del código del producto a eliminar
        id_producto = MagicMock()
        id_producto.return_value = 1 

        try:
            nuevo_nombre = 'Producto modificado 01'
            nuevo_precio = 500
            self.cursor.execute("UPDATE articulos SET nombre = ? , precio = ?  WHERE codigo = ?", (nuevo_nombre,nuevo_precio,id_producto.return_value))
            self.connection.commit()

            #se verifoca que el precio se modifico
            self.cursor.execute("SELECT * FROM articulos WHERE codigo = ?",(id_producto.return_value,))
            producto = self.cursor.fetchone()

            #se mira la base de datos para ver que si se modifico
            self.assertIsNotNone(producto)
            self.assertEqual(producto[1], nuevo_nombre)
            self.assertEqual(producto[2], nuevo_precio)

        except sqlite3.Error as e:
            print(f"error en la base de datos {str(e)}")
            self.fail(f"la prueba fallo en la base de datos por la falla {str(e)}")

        except Exception as e:
            print (f"error {str(e)}")
            self.fail (f"el test fallo debido a {str(e)}")

if __name__ == '__main__':
    unittest.main()