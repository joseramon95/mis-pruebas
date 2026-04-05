import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
from typing import Callable, Optional, List
from app.model import FileInfo


COLORS = {
    "bg_dark": "#2D1B4E",
    "bg_medium": "#4A2C7A",
    "bg_light": "#6B3FA0",
    "gold": "#FFD700",
    "gold_dark": "#B8860B",
    "gold_light": "#FFEC8B",
    "text": "#FFFFFF",
    "text_dark": "#1A1A2E",
    "list_bg": "#3D2666",
}


class ExclusionDialog(tk.Toplevel):
    def __init__(self, parent, current_exceptions: List[str] = None):
        super().__init__(parent)
        self.title("Excepciones - Archivos a Conservar")
        self.geometry("500x400")
        self.configure(bg=COLORS["bg_dark"])
        self.result: Optional[List[str]] = None
        self.current_exceptions = current_exceptions or []

        self.transient(parent)
        self.grab_set()

        self._setup_styles()
        self._setup_ui()
        self.protocol("WM_DELETE_WINDOW", self.on_cancel)

    def _setup_styles(self):
        style = ttk.Style(self)
        style.configure("Violet.TFrame", background=COLORS["bg_medium"])
        style.configure(
            "Gold.TLabel",
            background=COLORS["bg_medium"],
            foreground=COLORS["gold"],
            font=("Segoe UI", 10, "bold"),
        )
        style.configure(
            "Violet.TButton",
            background=COLORS["gold"],
            foreground=COLORS["text_dark"],
            font=("Segoe UI", 9, "bold"),
            padding=(10, 5),
        )
        style.map("Violet.TButton", background=[("active", COLORS["gold_dark"])])

    def _setup_ui(self):
        main_frame = ttk.Frame(self, style="Violet.TFrame", padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(
            main_frame,
            text="Archivos a CONSERVAR (no se eliminarán):",
            style="Gold.TLabel",
        ).pack(anchor=tk.W, pady=(0, 5))
        ttk.Label(
            main_frame,
            text="Ingresa un nombre de archivo por línea:",
            background=COLORS["bg_medium"],
            foreground=COLORS["text"],
            font=("Segoe UI", 9),
        ).pack(anchor=tk.W, pady=(0, 10))

        text_frame = ttk.Frame(main_frame, style="Violet.TFrame")
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        self.text_area = scrolledtext.ScrolledText(
            text_frame,
            height=15,
            bg=COLORS["list_bg"],
            fg=COLORS["text"],
            insertbackground=COLORS["gold"],
            font=("Consolas", 10),
            relief=tk.SUNKEN,
            bd=2,
            highlightcolor=COLORS["gold_dark"],
            highlightthickness=1,
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)

        for name in self.current_exceptions:
            self.text_area.insert(tk.END, f"{name}\n")

        btn_frame = ttk.Frame(main_frame, style="Violet.TFrame")
        btn_frame.pack(fill=tk.X)

        ttk.Button(
            btn_frame, text="💾 Guardar", style="Violet.TButton", command=self.on_accept
        ).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(
            btn_frame, text="✖ Cerrar", style="Violet.TButton", command=self.on_cancel
        ).pack(side=tk.LEFT)

    def on_accept(self):
        content = self.text_area.get("1.0", tk.END)
        self.result = [line.strip() for line in content.split("\n") if line.strip()]
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.destroy()


class FileSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("✦ Eliminador Masivo de Archivos ✦")
        self.geometry("750x550")
        self.configure(bg=COLORS["bg_dark"])
        self.resizable(True, True)

        self.files: List[FileInfo] = []
        self.directory: str = ""
        self.exceptions: List[str] = []

        self._setup_styles()
        self._setup_ui()

    def _setup_styles(self):
        self.style = ttk.Style(self)

        self.style.configure("Violet.TFrame", background=COLORS["bg_medium"])
        self.style.configure(
            "Violet.TLabelframe",
            background=COLORS["bg_dark"],
            foreground=COLORS["gold"],
            font=("Segoe UI", 10, "bold"),
        )
        self.style.configure(
            "Violet.TLabelframe.Label",
            background=COLORS["bg_dark"],
            foreground=COLORS["gold"],
            font=("Segoe UI", 10, "bold"),
        )
        self.style.configure(
            "Title.TLabel",
            background=COLORS["bg_dark"],
            foreground=COLORS["gold"],
            font=("Segoe UI", 14, "bold"),
        )
        self.style.configure(
            "Folder.TLabel",
            background=COLORS["bg_dark"],
            foreground=COLORS["gold_light"],
            font=("Segoe UI", 10),
        )
        self.style.configure(
            "Action.TLabel",
            background=COLORS["bg_medium"],
            foreground=COLORS["gold"],
            font=("Segoe UI", 9),
        )

        self.style.configure(
            "Gold.TButton",
            background=COLORS["gold"],
            foreground=COLORS["text_dark"],
            font=("Segoe UI", 9, "bold"),
            padding=(12, 6),
            relief=tk.RAISED,
            borderwidth=2,
        )
        self.style.map(
            "Gold.TButton",
            background=[("active", COLORS["gold_dark"])],
            relief=[("pressed", tk.SUNKEN)],
        )

        self.style.configure(
            "Danger.TButton",
            background="#DC3545",
            foreground=COLORS["text"],
            font=("Segoe UI", 9, "bold"),
            padding=(12, 6),
            relief=tk.RAISED,
            borderwidth=2,
        )
        self.style.map(
            "Danger.TButton",
            background=[("active", "#B02A37")],
            relief=[("pressed", tk.SUNKEN)],
        )

    def _setup_ui(self):
        main_frame = ttk.Frame(self, style="Violet.TFrame", padding="15")
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)

        title_label = ttk.Label(
            main_frame, text="✦ ELIMINADOR MASIVO DE ARCHIVOS ✦", style="Title.TLabel"
        )
        title_label.grid(row=0, column=0, pady=(0, 10))

        folder_frame = ttk.LabelFrame(
            main_frame,
            text=" 📁 Carpeta de Trabajo ",
            style="Violet.TLabelframe",
            padding="10",
        )
        folder_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        folder_frame.columnconfigure(0, weight=1)

        self.folder_label = ttk.Label(
            folder_frame, text="No se ha seleccionado carpeta", style="Folder.TLabel"
        )
        self.folder_label.grid(row=0, column=0, sticky="w")

        btn_frame = ttk.Frame(main_frame, style="Violet.TFrame")
        btn_frame.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        ttk.Button(
            btn_frame,
            text="📂 Seleccionar Carpeta",
            style="Gold.TButton",
            command=self.select_folder,
        ).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(
            btn_frame,
            text="📋 Clasificar",
            style="Gold.TButton",
            command=self._on_classify,
        ).grid(row=0, column=1, padx=(0, 5))
        ttk.Button(
            btn_frame,
            text="📄 Mostrar Todos",
            style="Gold.TButton",
            command=self._on_show_all,
        ).grid(row=0, column=2, padx=(0, 5))

        list_labelframe = ttk.LabelFrame(
            main_frame,
            text=" 📋 Archivos Encontrados ",
            style="Violet.TLabelframe",
            padding="10",
        )
        list_labelframe.grid(row=3, column=0, sticky="nsew", pady=(0, 10))
        list_labelframe.columnconfigure(0, weight=1)
        list_labelframe.rowconfigure(0, weight=1)

        list_inner = ttk.Frame(list_labelframe)
        list_inner.grid(row=0, column=0, sticky="nsew")
        list_inner.columnconfigure(0, weight=1)
        list_inner.rowconfigure(0, weight=1)

        self.file_listbox = tk.Listbox(
            list_inner,
            selectmode=tk.EXTENDED,
            width=80,
            height=12,
            bg=COLORS["list_bg"],
            fg=COLORS["text"],
            font=("Consolas", 10),
            selectbackground=COLORS["bg_light"],
            selectforeground=COLORS["gold"],
            relief=tk.SUNKEN,
            bd=2,
            highlightcolor=COLORS["gold_dark"],
            highlightthickness=1,
            activestyle="none",
        )
        self.file_listbox.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(
            list_inner, orient=tk.VERTICAL, command=self.file_listbox.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        action_frame = ttk.Frame(main_frame, style="Violet.TFrame")
        action_frame.grid(row=4, column=0, sticky="ew", pady=(0, 10))

        ttk.Button(
            action_frame,
            text="🗑️ Eliminar",
            style="Danger.TButton",
            command=self._on_delete_selection,
        ).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(
            action_frame,
            text="⭐ Excepciones",
            style="Gold.TButton",
            command=self._on_exceptions,
        ).grid(row=0, column=1, padx=(0, 5))
        ttk.Button(
            action_frame,
            text="✨ Limpiar",
            style="Gold.TButton",
            command=self._on_clear,
        ).grid(row=0, column=2)

        self.selection_label = ttk.Label(action_frame, text="", style="Action.TLabel")
        self.selection_label.grid(
            row=1, column=0, columnspan=3, sticky="w", pady=(8, 0)
        )

        log_labelframe = ttk.LabelFrame(
            main_frame,
            text=" 📜 Registro de Actividad ",
            style="Violet.TLabelframe",
            padding="10",
        )
        log_labelframe.grid(row=5, column=0, sticky="ew")
        log_labelframe.columnconfigure(0, weight=1)

        self.log_text = scrolledtext.ScrolledText(
            log_labelframe,
            height=6,
            state=tk.DISABLED,
            bg=COLORS["bg_dark"],
            fg=COLORS["gold_light"],
            font=("Consolas", 9),
            insertbackground=COLORS["gold"],
            relief=tk.SUNKEN,
            bd=2,
            highlightcolor=COLORS["gold_dark"],
            highlightthickness=1,
        )
        self.log_text.grid(row=0, column=0, sticky="ew")

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

    def show_warning(self, title: str, message: str):
        messagebox.showwarning(title, message)

    def show_exclusion_dialog(self) -> Optional[List[str]]:
        dialog = ExclusionDialog(self, self.exceptions.copy())
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

    def _on_clear(self):
        if self._callback_clear:
            self._callback_clear()

    def set_callbacks(
        self,
        on_select_folder: Callable,
        on_classify: Callable,
        on_show_all: Callable,
        on_delete_selection: Callable,
        on_exceptions: Callable,
        on_clear: Callable,
    ):
        self._callback_select_folder = on_select_folder
        self._callback_classify = on_classify
        self._callback_show_all = on_show_all
        self._callback_delete_selection = on_delete_selection
        self._callback_exceptions = on_exceptions
        self._callback_clear = on_clear

    def run(self):
        self.mainloop()
