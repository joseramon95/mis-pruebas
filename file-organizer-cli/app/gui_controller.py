from app.gui import FileSelector
from app.model import FileModel, FileInfo
from pathlib import Path


class GUIController:
    def __init__(self):
        self.gui = FileSelector()
        self.model: FileModel | None = None
        self.current_files: list[FileInfo] = []

        self.gui.set_callbacks(
            on_select_folder=self.on_select_folder,
            on_classify=self.on_classify,
            on_show_all=self.on_show_all,
            on_delete_duplicates=self.on_delete_duplicates,
            on_delete_by_name=self.on_delete_by_name,
        )

    def on_select_folder(self):
        if not self.model:
            self.gui.log_message("Error: No se ha seleccionado carpeta")
            return

        self.current_files = self.model.scan_files()
        self.gui.display_files(self.current_files)
        self.gui.log_message(f"Se encontraron {len(self.current_files)} archivos")

        log_path = self.model.save_archive_list()
        self.gui.log_message(f"Log guardado en: {log_path}")

    def on_classify(self):
        if not self.model or not self.current_files:
            self.gui.show_error("Error", "Primero selecciona una carpeta")
            return

        classified = self.model.classify_by_extension()
        self.gui.display_by_extension(classified)
        self.gui.log_message(f"Clasificados en {len(classified)} tipos de extension")

    def on_show_all(self):
        if not self.current_files:
            self.gui.show_error("Error", "Primero selecciona una carpeta")
            return

        self.gui.display_files(self.current_files)

    def on_delete_duplicates(self):
        if not self.model or not self.current_files:
            self.gui.show_error("Error", "Primero selecciona una carpeta")
            return

        self.gui.log_message("Calculando hashes... (puede tardar)")

        duplicates = self.model.find_duplicates()

        if not duplicates:
            self.gui.show_info("Duplicados", "No se encontraron duplicados")
            self.gui.log_message("No se encontraron duplicados")
            return

        total_dups = sum(len(group) - 1 for group in duplicates)
        self.gui.log_message(
            f"Encontrados {len(duplicates)} grupos de duplicados ({total_dups} archivos)"
        )

        for i, group in enumerate(duplicates, 1):
            self.gui.log_message(f"  Grupo {i}: {len(group)} archivos")

        if self.gui.show_confirm(
            "Confirmar",
            f"¿Eliminar {total_dups} duplicados (mantener uno de cada grupo)?",
        ):
            files_to_delete = []
            for group in duplicates:
                files_to_delete.extend(group[1:])

            results = self.model.delete_files(
                files_to_delete, "Eliminacion de duplicados"
            )

            self.gui.log_message(f"Eliminados: {len(results['deleted'])}")

            if results["errors"]:
                for err in results["errors"]:
                    self.gui.log_message(f"Error: {err['file']} - {err['error']}")

            self.current_files = self.model.scan_files()
            self.gui.display_files(self.current_files)
            self.gui.show_info("Resultado", f"Eliminados: {len(results['deleted'])}")

    def on_delete_by_name(self):
        if not self.model or not self.current_files:
            self.gui.show_error("Error", "Primero selecciona una carpeta")
            return

        names = self.gui.get_files_to_delete()

        if not names:
            self.gui.show_error("Error", "Ingresa los nombres de archivos a eliminar")
            return

        files_to_delete, not_found = self.model.get_files_by_names(names)
        excluded = []

        if not_found:
            self.gui.log_message(f"No encontrados {len(not_found)} archivos:")
            for name in not_found:
                self.gui.log_message(f"  - {name}")

            partial_matches = self._find_partial_matches(not_found)

            if partial_matches:
                match_msg = "Coincidencias parciales:\n"
                for orig, matches in partial_matches.items():
                    if matches:
                        match_msg += f"  '{orig}' -> {matches}\n"

                if self.gui.show_confirm(
                    "Archivos no encontrados",
                    f"No se encontraron {len(not_found)} archivos.\n\n{match_msg}\n¿Guardar en lista de exclusion y continuar?",
                ):
                    excluded = not_found
                    self.model.save_exclusion_list(excluded)
                    self.gui.log_message(
                        f"Guardados {len(excluded)} archivos en lista de exclusion"
                    )
                else:
                    self.gui.log_message("Operacion cancelada")
                    return
            else:
                if self.gui.show_confirm(
                    "Archivos no encontrados",
                    f"No se encontraron {len(not_found)} archivos.\n\n¿Guardar en lista de exclusion y continuar?",
                ):
                    excluded = not_found
                    self.model.save_exclusion_list(excluded)
                    self.gui.log_message(
                        f"Guardados {len(excluded)} archivos en lista de exclusion"
                    )
                else:
                    self.gui.log_message("Operacion cancelada")
                    return

        if not files_to_delete:
            self.gui.show_error("Error", "No hay archivos para eliminar")
            return

        self.gui.log_message(f"Archivos a eliminar: {len(files_to_delete)}")

        if self.gui.show_confirm(
            "Confirmar", f"¿Eliminar {len(files_to_delete)} archivos?"
        ):
            results = self.model.delete_files(
                files_to_delete, "Eliminacion por nombre", excluded
            )

            self.gui.log_message(f"Eliminados: {len(results['deleted'])}")

            if results["errors"]:
                for err in results["errors"]:
                    self.gui.log_message(f"Error: {err['file']} - {err['error']}")

            self.current_files = self.model.scan_files()
            self.gui.display_files(self.current_files)
            self.gui.show_info("Resultado", f"Eliminados: {len(results['deleted'])}")

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

    def set_directory(self, path: str) -> bool:
        project_root = Path(__file__).parent.parent
        logs_dir = project_root / "logs"
        self.model = FileModel(path, logs_dir)
        return self.model.validate_path()

    def run(self):
        self.gui.run()
