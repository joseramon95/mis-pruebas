import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from models import conectar_bd


class GestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("gestor de tareas")
        try:
            self.conn = conectar_bd() #manda llamar de models.py
        except Exception as e :# exepcin por si da error
            messagebox.showerror("Error", f"no se puede conectar a la BD: {e}")
            self.root.desroy()

        self.root.geometry("700x500")

        self.crear_interfaz()
        self.actualizar_lista()

        #componentes 

        #botones

