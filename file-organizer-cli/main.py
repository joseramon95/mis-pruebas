#!/usr/bin/env python3
import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.controller import Controller
from app.view import View


def main():
    view = View()
    controller = Controller(view)

    view.show_banner()

    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = view.prompt("Introduce la ruta de la carpeta")

        if not directory:
            view.show_error("No se proporcionó directorio")
            return

    if not controller.set_directory(directory):
        return

    if not controller.scan_directory():
        return

    while True:
        view.show_main_menu()
        option = view.prompt("Selecciona una opción")

        match option:
            case "1":
                controller.scan_directory()
            case "2":
                controller.show_files()
            case "3":
                controller.classify_files()
            case "4":
                controller.delete_duplicates_flow()
            case "5":
                controller.delete_by_name_flow()
            case "0" | "q":
                view.show_info("¡Hasta luego!")
                break
            case _:
                view.show_error("Opción no válida")


if __name__ == "__main__":
    main()
