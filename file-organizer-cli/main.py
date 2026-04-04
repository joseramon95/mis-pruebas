#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.controller import Controller
from app.view import View


def main():
    view = View()
    controller = Controller(view)

    view.show_banner()

    if len(sys.argv) > 1:
        directory = sys.argv[1]
        if not controller.set_directory(directory):
            return
        controller.scan_directory()
    else:
        directory = view.prompt("Introduce la ruta de la carpeta")

        if not directory:
            view.show_error("No se proporcionó directorio")
            return

        if not controller.set_directory(directory):
            return

    while True:
        view.show_menu()
        option = view.prompt("Selecciona una opción")

        match option:
            case "1":
                recursive = view.confirm("¿Escaneo recursivo?")
                controller.scan_directory(recursive)
            case "2":
                controller.classify_files()
            case "3":
                controller.delete_files_flow()
            case "4":
                controller.find_duplicates_flow()
            case "5":
                controller.show_all_files()
            case "0" | "q":
                view.show_info("¡Hasta luego!")
                break
            case _:
                view.show_error("Opción no válida")


if __name__ == "__main__":
    main()
