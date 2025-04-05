#poner todo en su respictivo archivo 

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from models import conectar_bd


class GestorTareas:
    def __init__(self, root):
        self.root = root
        try:
            self.conn = conectar_bd() #manda llamar de models.py
        except Exception as e :# exepcin por si da error
            messagebox.showerror("Error", f"no se puede conectar a la BD: {e}")
            self.root.desroy()

        self.root.title ("Gestor de Tareas Avanzado")
        self.root.geometry("700x500")

        self.crear_interfaz()
        self.actualizar_lista()

def interfaz (self):
    "esto sirve para crear las vetanas graficas "
    #esto creas frames para los controles
    frame_controles = tk.frame(self.root, padx=10, pady=10)
    frame_controles.pack(fill=tk.X)

#campos de entrada
tk.Label(frame_controles, text="Nombre:").grid(row=0, column=0, sticky="w")
self.entry_nombre = tk.Entry(frame_controles, width=30)
self.entry_nombre.grid(row=0, column=1, padx=5, pady=2)




if __name__ == "__main__":
    root = tk.Tk()
    from tkinter import simpledialog  # Importación para dialogos modales
    app = GestorTareas(root)
    root.mainloop()