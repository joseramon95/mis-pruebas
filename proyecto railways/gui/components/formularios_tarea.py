import tkinter as tk

class formulario_Tareas():
    def __init__(self, parent):
        super().__init__(parent)
            #labels
        self.lbl_nombre = tk.label(self, text = "Nombre:")
        self.lbl_id = tk.label(self, text= "ID Usuario:")
        self.lbl_porcentaje = tk.label(self, text= "Porcentaje:")

        #campos de entrada
        self.entry_nombre = tk.Entry(self)
        self.entry_id = tk.Entry(self)
        self.entry_porcentaje = tk.Entry(self)

        #organizacion de la interfaz grid
        self.lbl_nombre.grid (row=0, column=0, sticky="w")
        self.entry_nombre.grid(row=0, column=1 )

        self.lbl_id.grid (row=1, column=0, sticky="w")
        self.entry_id.grid(row=1, column=1 )

        self.lbl_porcentaje.grid (row=2, column=0, sticky="w")
        self.entry_porcentaje.grid(row=2, column=1 )

def obtener_datos(self):
    return {
        "nombre": self.entry_nombre.get(),
        "id_usuario": self.entry_id.get(),
        "porcentaje": self.entry_porcentaje.get()
    }
