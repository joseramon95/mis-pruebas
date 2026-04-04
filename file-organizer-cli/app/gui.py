import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
from typing import Callable, Optional, List
from app.model import FileInfo


class ExclusionDialog(tk.Toplevel):
    def __init__(self, parent, current_exceptions: List[str] = None):
        super().__init__(parent)
        self.title("Excepciones - Archivos a Conservar")
        self.geometry("500x400")
        self.resizable(True, True)
        self.result: Optional[List[str]] = None
        self.current_exceptions = current_exceptions or []

        self.transient(parent)
        self.grab_set()

        self._setup_ui()

        self.protocol("WM_DELETE_WINDOW", self.on_cancel)

    def _setup_ui(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(
            main_frame,
            text="Archivos a CONSERVAR (no se eliminaran):",
            font=("Arial", 10, "bold"),
        ).pack(anchor=tk.W)
        ttk.Label(
            main_frame,
            text="Ingresa un nombre de archivo por linea:",
            font=("Arial", 9),
        ).pack(anchor=tk.W, pady=(0, 5))

        text_frame = ttk.Frame(main_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        self.text_area = scrolledtext.ScrolledText(text_frame, height=15)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        for name in self.current_exceptions:
            self.text_area.insert(tk.END, f"{name}\n")

        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X)

        ttk.Button(btn_frame, text="Guardar", command=self.on_accept).pack(
            side=tk.LEFT, padx=(0, 5)
        )
        ttk.Button(btn_frame, text="Limpiar Todo", command=self.on_clear).pack(
            side=tk.LEFT, padx=(0, 5)
        )
        ttk.Button(btn_frame, text="Cerrar", command=self.on_cancel).pack(side=tk.LEFT)

    def on_accept(self):
        content = self.text_area.get("1.0", tk.END)
        self.result = [line.strip() for line in content.split("\n") if line.strip()]
        self.destroy()

    def on_clear(self):
        self.text_area.delete("1.0", tk.END)
        self.result = []
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.destroy()


class FileSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Eliminador Masivo de Archivos")
        self.geometry("700x500")
        self.resizable(True, True)

        self.selected_files: List[FileInfo] = []
        self.files: List[FileInfo] = []
        self.directory: str = ""
        self.selected_for_deletion: List[str] = []
        self.exceptions: List[str] = []

        self._setup_ui()

    def _setup_ui(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)

        folder_frame = ttk.Frame(main_frame)
        folder_frame.grid(row=0, column=0, sticky="w", pady=(0, 10))
        folder_frame.columnconfigure(0, weight=1)

        self.folder_label = ttk.Label(
            folder_frame, text="No se ha seleccionado carpeta"
        )
        self.folder_label.grid(row=0, column=0, sticky="w")

        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=1, column=0, sticky="w", pady=(0, 10))

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
        list_frame.grid(row=2, column=0, sticky="nsew")
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        self.file_listbox = tk.Listbox(
            list_frame, selectmode=tk.EXTENDED, width=80, height=15
        )
        self.file_listbox.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(
            list_frame, orient=tk.VERTICAL, command=self.file_listbox.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=3, column=0, sticky="w", pady=(10, 0))

        ttk.Button(
            action_frame, text="Eliminar Seleccion", command=self._on_delete_selection
        ).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(action_frame, text="Excepciones", command=self._on_exceptions).grid(
            row=0, column=1
        )

        self.selection_label = ttk.Label(action_frame, text="")
        self.selection_label.grid(
            row=1, column=0, columnspan=2, sticky="w", pady=(5, 0)
        )

        self.log_text = scrolledtext.ScrolledText(
            main_frame, height=8, state=tk.DISABLED
        )
        self.log_text.grid(row=4, column=0, sticky="nsew", pady=(10, 0))

    def select_folder(self):
        folder = filedialog.askdirectory(title="Seleccionar carpeta")
        if folder:
            self.directory = folder
            self.folder_label.config(text=f"Carpeta: {folder}")
            self._callback_select_folder(folder)

    def display_files(self, files: List[FileInfo]):
        self.files = files
        self.file_listbox.delete(0, tk.END)
        for i, f in enumerate(files, 1):
            size = self._format_size(f.size)
            self.file_listbox.insert(tk.END, f"{i}. {f.name} ({size})")

    def display_by_extension(self, classified: dict):
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

    def show_exclusion_dialog(self) -> Optional[List[str]]:
        dialog = ExclusionDialog(self, self.exceptions)
        self.wait_window()
        return dialog.result

    def open_file_selection(self) -> List[str]:
        if not self.directory:
            return []

        files = filedialog.askopenfilenames(
            title="Seleccionar archivos a eliminar",
            initialdir=self.directory,
            filetypes=[("Todos los archivos", "*.*")],
        )

        return list(files)

    def get_selected_indices(self) -> List[int]:
        selection = self.file_listbox.curselection()
        return [int(i) + 1 for i in selection]

    def set_selection_label(self, text: str):
        self.selection_label.config(text=text)

    def clear_selection_label(self):
        self.selection_label.config(text="")

    def get_files_to_delete(self) -> List[str]:
        return self.selected_for_deletion

    def get_exceptions(self) -> List[str]:
        return self.exceptions

    def set_exceptions(self, exceptions: List[str]):
        self.exceptions = exceptions

    def clear_exceptions(self):
        self.exceptions = []

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

    def _on_delete_selection(self):
        if self._callback_delete_selection:
            self._callback_delete_selection()

    def _on_exceptions(self):
        if self._callback_exceptions:
            self._callback_exceptions()

    def set_callbacks(
        self,
        on_select_folder: Callable,
        on_classify: Callable,
        on_show_all: Callable,
        on_delete_selection: Callable,
        on_exceptions: Callable,
    ):
        self._callback_select_folder = on_select_folder
        self._callback_classify = on_classify
        self._callback_show_all = on_show_all
        self._callback_delete_selection = on_delete_selection
        self._callback_exceptions = on_exceptions

    def run(self):
        self.mainloop()
