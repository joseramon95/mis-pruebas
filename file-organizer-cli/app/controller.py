from pathlib import Path
from app.model import FileModel, FileInfo
from app.view import View


class Controller:
    def __init__(self, view: View):
        self.view = view
        self.model: FileModel | None = None
        self.current_files: list[FileInfo] = []
        self.log_path: Path | None = None

    def set_directory(self, path: str) -> bool:
        project_root = Path(__file__).parent.parent
        logs_dir = project_root / "logs"
        self.model = FileModel(path, logs_dir)
        if not self.model.validate_path():
            self.view.show_error("La ruta no existe o no es un directorio")
            return False
        self.view.show_success(f"Directorio configurado: {path}")
        return True

    def scan_directory(self):
        if not self.model:
            self.view.show_error("No hay directorio configurado")
            return False

        self.current_files = self.model.scan_files()
        self.view.show_info(f"Se encontraron {len(self.current_files)} archivos")

        if self.current_files:
            self.log_path = self.model.save_file_list()
            self.view.show_log_saved(self.log_path)

        return True

    def show_files(self):
        if not self.current_files:
            self.view.show_error("Primero escanea la carpeta")
            return
        self.view.show_files(self.current_files)

    def classify_files(self):
        if not self.model or not self.current_files:
            self.view.show_error("Primero escanea la carpeta")
            return
        classified = self.model.classify_by_extension()
        self.view.show_by_extension(classified)

    def delete_duplicates_flow(self):
        if not self.model or not self.current_files:
            self.view.show_error("Primero escanea la carpeta")
            return

        self.view.show_info("Calculando hashes... (puede tardar)")

        duplicates = self.model.find_duplicates()

        if not duplicates:
            self.view.show_duplicates(duplicates)
            return

        self.view.show_duplicates(duplicates)

        if self.view.confirm("¿Eliminar duplicados (mantener uno de cada grupo)?"):
            files_to_delete = []
            for group in duplicates:
                files_to_delete.extend(group[1:])

            self.view.show_delete_preview(files_to_delete)

            if self.view.confirm("¿Confirmar eliminación?"):
                results = self.model.delete_files(files_to_delete)
                self.view.show_delete_results(results)

                self.model.log_elimination(results["deleted"])

                self.current_files = self.model.scan_files()
        else:
            self.view.show_info("Operación cancelada")

    def delete_by_name_flow(self):
        if not self.model or not self.current_files:
            self.view.show_error("Primero escanea la carpeta")
            return

        self.view.show_log_location(self.model.get_elimination_log_path())

        self.view.show_info(
            "Ingresa los nombres de los archivos a eliminar (uno por línea)"
        )
        self.view.show_info("Escribe 'fin' cuando termines")

        names = []
        while True:
            name = self.view.prompt("Archivo")
            if name.lower() == "fin":
                break
            if name:
                names.append(name)

        if not names:
            self.view.show_info("No se ingresaron archivos")
            return

        files_to_delete, not_found = self.model.get_files_by_names(names)

        if not_found:
            print(f"\n⚠️  No encontrados: {', '.join(not_found)}")

        if not files_to_delete:
            self.view.show_error("No se encontraron archivos coincidentes")
            return

        self.view.show_delete_preview(files_to_delete)

        if self.view.confirm("¿Confirmar eliminación?"):
            results = self.model.delete_files(files_to_delete)
            self.view.show_delete_results(results)

            self.model.log_elimination(results["deleted"])

            self.current_files = self.model.scan_files()
        else:
            self.view.show_info("Operación cancelada")

    def main_flow(self):
        option = self.view.ask_delete_option()

        if option == "1":
            self.delete_duplicates_flow()
        elif option == "2":
            self.delete_by_name_flow()
        else:
            self.view.show_error("Opción no válida")
