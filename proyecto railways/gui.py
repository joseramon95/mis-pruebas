import tkinter as tk
from tkinter import messagebox
from models import agregar_producto, obtener_productos

def agregar():
    nombre = entrada_nombre.get()
    cantidad = entrada_cantidad.get()

    if nombre and cantidad.isdigit():
        agregar_producto(nombre, int(cantidad))
        messagebox.showinfo("Éxito", "Producto agregado")
        actualizar_lista()
    else:
        messagebox.showerror("Error", "Datos inválidos")

def actualizar_lista():
    lista_productos.delete(0, tk.END)
    productos = obtener_productos()
    for producto in productos:
        lista_productos.insert(tk.END, f"{producto[1]} - {producto[2]} unidades")

def iniciar_gui():
    global entrada_nombre, entrada_cantidad, lista_productos

    ventana = tk.Tk()
    ventana.title("Inventario")

    tk.Label(ventana, text="Nombre del Producto:").pack()
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack()

    tk.Label(ventana, text="Cantidad:").pack()
    entrada_cantidad = tk.Entry(ventana)
    entrada_cantidad.pack()

    tk.Button(ventana, text="Agregar Producto", command=agregar).pack()

    lista_productos = tk.Listbox(ventana)
    lista_productos.pack()

    actualizar_lista()

    ventana.mainloop()
