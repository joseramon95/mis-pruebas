import re
from pathlib import Path
from app.model import FileModel, FileInfo
from app.view import View


class Controller:
    def __init__(self, view: View):
        self.view = view
        self.model: FileModel | None = None
        self.current_files: list[FileInfo] = []
        self.classified: dict[str, list[FileInfo]] = {}

    def set_directory(self, path: str) -> bool:
        self.model = FileModel(path)
        if not self.model.validate_path():
            self.view.show_error("La ruta no existe o no es un directorio")
            return False
        self.view.show_success(f"Directorio configurado: {path}")
        return True

    def scan_directory(self, recursive: bool = False):
        if not self.model:
            self.view.show_error("No hay directorio configurado")
            return

        self.current_files = self.model.scan_files(recursive)
        self.view.show_info(f"Se encontraron {len(self.current_files)} archivos")
        self.view.show_files(self.current_files)

    def classify_files(self):
        if not self.model or not self.current_files:
            self.view.show_error("Primero escanea el directorio")
            return

        self.classified = self.model.classify_by_extension()
        self.view.show_by_extension(self.classified)

    def parse_selection(self, selection: str) -> list[FileInfo]:
        if not self.model or not self.current_files:
            return []

        selection = selection.strip().lower()

        if selection == "q":
            return []

        if selection == "all":
            return self.current_files.copy()

        files_to_delete: list[FileInfo] = []
        parts = re.split(r"[,\s]+", selection)

        for part in parts:
            part = part.strip()
            if not part:
                continue

            if re.match(r"^\d+-\d+$", part):
                start, end = map(int, part.split("-"))
                for i in range(start, end + 1):
                    file = self.model.get_file_by_index(i)
                    if file and file not in files_to_delete:
                        files_to_delete.append(file)

            elif re.match(r"^\d+$", part):
                file = self.model.get_file_by_index(int(part))
                if file and file not in files_to_delete:
                    files_to_delete.append(file)

            elif "*" in part:
                matched = self.model.get_files_by_pattern(part)
                for f in matched:
                    if f not in files_to_delete:
                        files_to_delete.append(f)

            elif part.startswith("."):
                matched = self.model.get_files_by_extension(part)
                for f in matched:
                    if f not in files_to_delete:
                        files_to_delete.append(f)

        return files_to_delete

    def delete_files_flow(self):
        if not self.current_files:
            self.view.show_error("Primero escanea el directorio")
            return

        self.view.show_help_delete()
        selection = self.view.prompt("Selecciona archivos a eliminar")

        if selection == "q":
            self.view.show_info("Operación cancelada")
            return

        files_to_delete = self.parse_selection(selection)

        if not files_to_delete:
            self.view.show_error("No se encontraron archivos coincidentes")
            return

        self.view.show_delete_preview(files_to_delete)

        if self.view.confirm("¿Confirmar eliminación?") and self.model:
            results = self.model.delete_files(files_to_delete)
            self.view.show_delete_results(results)

            self.current_files = self.model.scan_files()
        else:
            self.view.show_info("Operación cancelada")

    def find_duplicates_flow(self):
        if not self.model:
            self.view.show_error("No hay directorio configurado")
            return

        self.view.show_info("Calculando hashes... (puede tardar)")

        self.current_files = self.model.scan_files()
        duplicates = self.model.find_duplicates()

        if duplicates:
            self.view.show_duplicates(duplicates)

            if self.view.confirm("¿Eliminar duplicados (mantener uno)?"):
                files_to_delete = []
                for group in duplicates[1:]:
                    files_to_delete.extend(group)

                if self.model:
                    results = self.model.delete_files(files_to_delete)
                    self.view.show_delete_results(results)
                    self.current_files = self.model.scan_files()
        else:
            self.view.show_duplicates(duplicates)

    def show_all_files(self):
        if self.current_files:
            self.view.show_files(self.current_files)
        else:
            self.view.show_error("Primero escanea el directorio")
