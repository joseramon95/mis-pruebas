import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
from typing import Callable, Optional
from app.model import FileInfo


class ExclusionDialog(tk.Toplevel):
    def __init__(self, parent, excluded_files: list[str]):
        super().__init__(parent)
        self.title("Archivos No Encontrados - Lista de Exclusion")
        self.geometry("500x400")
        self.resizable(True, True)
        self.excluded_files = excluded_files
        self.result: Optional[list[str]] = None

        self.transient(parent)
        self.grab_set()

        self._setup_ui()

        self.protocol("WM_DELETE_WINDOW", self.on_cancel)

    def _setup_ui(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(
            main_frame, text="Archivos no encontrados:", font=("Arial", 10, "bold")
        ).pack(anchor=tk.W)
        ttk.Label(
            main_frame,
            text="Edita la lista y guarda los que quieres excluir:",
            font=("Arial", 9),
        ).pack(anchor=tk.W, pady=(0, 5))

        text_frame = ttk.Frame(main_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        self.text_area = scrolledtext.ScrolledText(text_frame, height=15)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        for name in self.excluded_files:
            self.text_area.insert(tk.END, f"{name}\n")

        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X)

        ttk.Button(
            btn_frame, text="Guardar y Continuar", command=self.on_save_continue
        ).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Cancelar", command=self.on_cancel).pack(
            side=tk.LEFT
        )

    def on_save_continue(self):
        content = self.text_area.get("1.0", tk.END)
        self.result = [line.strip() for line in content.split("\n") if line.strip()]
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.destroy()

    def show():
        self.wait_window()
        return self.result


class FileSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Eliminador Masivo de Archivos")
        self.geometry("700x500")
        self.resizable(True, True)

        self.selected_files: list[FileInfo] = []
        self.files: list[FileInfo] = []
        self.directory: str = ""

        self._setup_ui()

    def _setup_ui(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)

        folder_frame = ttk.Frame(main_frame)
        folder_frame.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        folder_frame.columnconfigure(0, weight=1)

        self.folder_label = ttk.Label(
            folder_frame, text="No se ha seleccionado carpeta"
        )
        self.folder_label.grid(row=0, column=0, sticky=tk.W)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=1, column=0, sticky=tk.W, pady=(0, 10))

        ttk.Button(
            btn_frame, text="Seleccionar Carpeta", command=self.select_folder
        ).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(
            btn_frame, text="Clasificar por Extension", command=self._on_classify
        ).grid(row=0, column=1, padx=(0, 5))
        ttk.Button(btn_frame, text="Mostrar Todos", command=self._on_show_all).grid(
            row=0, column=2, padx=(0, 5)
        )

        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        self.file_listbox = tk.Listbox(
            list_frame, selectmode=tk.EXTENDED, width=80, height=15
        )
        self.file_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        scrollbar = ttk.Scrollbar(
            list_frame, orient=tk.VERTICAL, command=self.file_listbox.yview
        )
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        action_frame.columnconfigure(1, weight=1)

        ttk.Label(action_frame, text="Archivos a eliminar:").grid(
            row=0, column=0, padx=(0, 5)
        )

        self.delete_entry = ttk.Entry(action_frame)
        self.delete_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))

        ttk.Button(
            action_frame, text="Eliminar Duplicados", command=self._on_delete_duplicates
        ).grid(row=0, column=2, padx=(0, 5))
        ttk.Button(
            action_frame, text="Eliminar por Nombre", command=self._on_delete_by_name
        ).grid(row=0, column=3)

        self.log_text = scrolledtext.ScrolledText(
            main_frame, height=8, state=tk.DISABLED
        )
        self.log_text.grid(
            row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0)
        )

    def select_folder(self):
        folder = filedialog.askdirectory(title="Seleccionar carpeta")
        if folder:
            self.directory = folder
            self.folder_label.config(text=f"Carpeta: {folder}")
            self._callback_select_folder(folder)

    def display_files(self, files: list[FileInfo]):
        self.files = files
        self.file_listbox.delete(0, tk.END)
        for i, f in enumerate(files, 1):
            size = self._format_size(f.size)
            self.file_listbox.insert(tk.END, f"{i}. {f.name} ({size})")

    def display_by_extension(self, classified: dict[str, list[FileInfo]]):
        self.file_listbox.delete(0, tk.END)
        for ext, files in sorted(classified.items()):
            self.file_listbox.insert(tk.END, f"[{ext}] ({len(files)} archivos)")
            for f in files[:10]:
                self.file_listbox.insert(tk.END, f"    - {f.name}")
            if len(files) > 10:
                self.file_listbox.insert(tk.END, f"    ... y {len(files) - 10} mas")
            self.file_listbox.insert(tk.END, "")

    def log_message(self, message: str):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def show_confirm(self, title: str, message: str) -> bool:
        return messagebox.askyesno(title, message)

    def show_info(self, title: str, message: str):
        messagebox.showinfo(title, message)

    def show_error(self, title: str, message: str):
        messagebox.showerror(title, message)

    def show_exclusion_dialog(self, excluded_files: list[str]) -> Optional[list[str]]:
        dialog = ExclusionDialog(self, excluded_files)
        return dialog.show()

    def get_files_to_delete(self) -> list[str]:
        text = self.delete_entry.get().strip()
        if not text:
            return []
        return [name.strip() for name in text.split("\n") if name.strip()]

    def _format_size(self, size: int) -> str:
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"

    def _on_classify(self):
        if self._callback_classify:
            self._callback_classify()

    def _on_show_all(self):
        if self._callback_show_all:
            self._callback_show_all()

    def _on_delete_duplicates(self):
        if self._callback_delete_duplicates:
            self._callback_delete_duplicates()

    def _on_delete_by_name(self):
        if self._callback_delete_by_name:
            self._callback_delete_by_name()

    def set_callbacks(
        self,
        on_select_folder: Callable,
        on_classify: Callable,
        on_show_all: Callable,
        on_delete_duplicates: Callable,
        on_delete_by_name: Callable,
    ):
        self._callback_select_folder = on_select_folder
        self._callback_classify = on_classify
        self._callback_show_all = on_show_all
        self._callback_delete_duplicates = on_delete_duplicates
        self._callback_delete_by_name = on_delete_by_name

    def run(self):
        self.mainloop()
