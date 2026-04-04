from app.gui import FileSelector
from app.model import FileModel, FileInfo
from pathlib import Path


class GUIController:
    def __init__(self):
        self.gui = FileSelector()
        self.model: FileModel | None = None
        self.current_files: list = []

        self.gui.set_callbacks(
            on_select_folder=self.on_select_folder,
            on_classify=self.on_classify,
            on_show_all=self.on_show_all,
            on_delete_selection=self.on_delete_selection,
            on_exceptions=self.on_exceptions,
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

    def on_exceptions(self):
        exceptions = self.gui.show_exclusion_dialog()

        if exceptions is not None:
            self.gui.set_exceptions(exceptions)
            self.gui.log_message(
                f"Excepciones configuradas: {len(exceptions)} archivos"
            )
        else:
            self.gui.clear_exceptions()
            self.gui.log_message("Excepciones canceladas")

    def on_delete_selection(self):
        if not self.model or not self.current_files:
            self.gui.show_error("Error", "Primero selecciona una carpeta")
            return

        selected_paths = self.gui.open_file_selection()

        if not selected_paths:
            self.gui.log_message("No se seleccionaron archivos")
            return

        selected_names = [Path(p).name for p in selected_paths]
        self.gui.set_selection_label(f"Seleccionados: {len(selected_names)} archivos")

        files_to_delete = []
        for name in selected_names:
            file_info = self.model.get_file_by_name(name)
            if file_info:
                files_to_delete.append(file_info)

        if not files_to_delete:
            self.gui.show_error("Error", "No se encontraron archivos validos")
            return

        exceptions = self.gui.get_exceptions()
        excluded = []

        if exceptions:
            excluded_names = []
            for name in exceptions:
                file_info = self.model.get_file_by_name(name)
                if file_info:
                    excluded.append(file_info)
                    excluded_names.append(name)
                    if file_info in files_to_delete:
                        files_to_delete.remove(file_info)

            if excluded_names:
                self.gui.log_message(
                    f"Excluidos por excepciones: {len(excluded_names)}"
                )

        self.gui.log_message(f"Archivos a eliminar: {len(files_to_delete)}")

        if not files_to_delete:
            self.gui.show_error("Error", "No hay archivos para eliminar")
            return

        if self.gui.show_confirm(
            "Confirmar", f"¿Eliminar {len(files_to_delete)} archivos?"
        ):
            results = self.model.delete_files(
                files_to_delete, "Eliminacion por seleccion", excluded
            )

            self.gui.log_message(f"Eliminados: {len(results['deleted'])}")

            if results["errors"]:
                for err in results["errors"]:
                    self.gui.log_message(f"Error: {err['file']} - {err['error']}")

            self.current_files = self.model.scan_files()
            self.gui.display_files(self.current_files)
            self.gui.show_info("Resultado", f"Eliminados: {len(results['deleted'])}")
            self.gui.clear_selection_label()
            self.gui.clear_exceptions()
        else:
            self.gui.log_message("Operacion cancelada")

    def set_directory(self, path: str) -> bool:
        project_root = Path(__file__).parent.parent
        logs_dir = project_root / "logs"
        self.model = FileModel(path, logs_dir)
        return self.model.validate_path()

    def run(self):
        self.gui.run()
