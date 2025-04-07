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

def interfaz (self):
    "esto sirve para crear las vetanas graficas "
    #esto creas frames para los controles
    frame_controles = tk.frame(self.root, padx=10, pady=10)
    frame_controles.pack(fill=tk.X)


"""
#esto se usara en en formulario para registrar usuario
tk.Label(frame_controles, text="Correo Electronico:").grid(row=0, column=0, sticky="w")
self.entry_nombre = tk.Entry(frame_controles, width=30)
self.entry_nombre.grid(row=0, column=1, padx=5, pady=2)

tk.Label(frame_controles, text="Numero Telefonico:").grid(row=0, column=0, sticky="w")
self.entry_nombre = tk.Entry(frame_controles, width=30)
self.entry_nombre.grid(row=0, column=1, padx=5, pady=2)
"""
