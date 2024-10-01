import sys
import os
# Agrega 'src' al PYTHONPATH para poder importar el código del sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ULS_INVENTARIO import guarda, eliminar  # Importa las funciones a probar

import unittest
from tkinter import Tk, Entry, Button
from unittest.mock import MagicMock

class TestApp(unittest.TestCase):
    def setUp(self):
        # Simula una ventana de Tkinter
        self.root = Tk()
        self.entry_producto = Entry(self.root)
        self.entry_precio = Entry(self.root)
        self.btn_guardar = Button(self.root, text="Guardar")
        
        # Simular una función de guardar (sería parte de tu sistema de inventario)
        self.guardar_producto = MagicMock()

    def tearDown(self):
        self.root.destroy()

    def test_guardar_producto_desde_gui(self):
        # Simular la entrada de datos en la interfaz
        self.entry_producto.insert(0, "Producto de prueba")
        self.entry_precio.insert(0, "50")

        # Simular que el botón de "Guardar" se presiona y llama a la función guardar
        self.btn_guardar.invoke()
        
        # Verificar si la función de guardar fue llamada
        self.guardar_producto.assert_called_with("Producto de prueba", 50)

if __name__ == "__main__":
    unittest.main()