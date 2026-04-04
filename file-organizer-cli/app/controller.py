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
            self.log_path = self.model.save_archive_list()
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

            if self.view.confirm("¿Confirmar eliminacion?"):
                results = self.model.delete_files(
                    files_to_delete, "Eliminacion de duplicados"
                )
                self.view.show_delete_results(results)
                self.current_files = self.model.scan_files()
        else:
            self.view.show_info("Operacion cancelada")

    def delete_by_name_flow(self):
        if not self.model or not self.current_files:
            self.view.show_error("Primero escanea la carpeta")
            return

        self.view.show_info(
            "Ingresa los nombres de los archivos a eliminar (uno por linea)"
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

        excluded = []

        if not_found:
            self.view.show_info(f"No se encontraron {len(not_found)} archivos:")
            for name in not_found:
                self.view.show_info(f"  - {name}")

            self.view.show_info("Que deseas hacer?")
            self.view.show_info("1. Guardar en lista de exclusion y continuar")
            self.view.show_info("2. Corregir nombre (buscar coincidencias parciales)")
            self.view.show_info("3. Cancelar operacion")

            option = self.view.prompt("Elige una opcion (1/2/3)")

            if option == "1":
                excluded = not_found
                self.model.save_exclusion_list(excluded)
                self.view.show_success(
                    f"Guardados {len(excluded)} archivos en lista de exclusion"
                )

            elif option == "2":
                partial_matches = self._find_partial_matches(not_found)
                if partial_matches:
                    self.view.show_info("Coincidencias encontradas:")
                    for orig, matches in partial_matches.items():
                        self.view.show_info(f"  '{orig}' -> {matches}")

                    if self.view.confirm("Usar coincidencias?"):
                        for orig, matches in partial_matches.items():
                            if matches:
                                matched_file = self.model.get_file_by_name(matches[0])
                                if matched_file and matched_file not in files_to_delete:
                                    files_to_delete.append(matched_file)
                        excluded = [
                            orig
                            for orig, matches in partial_matches.items()
                            if not matches
                        ]
                    else:
                        excluded = not_found
                        self.model.save_exclusion_list(excluded)
                        self.view.show_info("Operacion cancelada por el usuario")
                        return
                else:
                    self.view.show_info("No se encontraron coincidencias")
                    excluded = not_found
                    self.model.save_exclusion_list(excluded)

            else:
                self.view.show_info("Operacion cancelada")
                return

        if not files_to_delete:
            self.view.show_error("No hay archivos para eliminar")
            return

        self.view.show_delete_preview(files_to_delete)

        if self.view.confirm("¿Confirmar eliminacion?"):
            results = self.model.delete_files(
                files_to_delete, "Eliminacion por nombre", excluded
            )
            self.view.show_delete_results(results)
            self.current_files = self.model.scan_files()
        else:
            self.view.show_info("Operacion cancelada")

    def _find_partial_matches(self, names: list[str]) -> dict[str, list[str]]:
        matches = {}
        for name in names:
            name_lower = name.lower().replace(" ", "")
            partial = []
            for file in self.current_files:
                file_lower = file.name.lower().replace(" ", "")
                if name_lower in file_lower or file_lower in name_lower:
                    if file.name.lower() != name.lower():
                        partial.append(file.name)
            matches[name] = partial[:3]
        return matches

    def main_flow(self):
        option = self.view.ask_delete_option()

        if option == "1":
            self.delete_duplicates_flow()
        elif option == "2":
            self.delete_by_name_flow()
        else:
            self.view.show_error("Opcion no valida")
