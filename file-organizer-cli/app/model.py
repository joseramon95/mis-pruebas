from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import hashlib
import os
from datetime import datetime


@dataclass
class FileInfo:
    path: Path
    name: str
    extension: str
    size: int
    hash: Optional[str] = None


class LogManager:
    def __init__(self, logs_dir: Path):
        self.logs_dir = logs_dir
        self.sessions_dir = logs_dir / "sesiones"
        self.archives_dir = logs_dir / "archivos"
        self.eliminations_dir = logs_dir / "eliminaciones"

        self.sessions_dir.mkdir(parents=True, exist_ok=True)
        self.archives_dir.mkdir(parents=True, exist_ok=True)
        self.eliminations_dir.mkdir(parents=True, exist_ok=True)

        self.current_session_file: Optional[Path] = None
        self._start_session()

    def _start_session(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.current_session_file = self.sessions_dir / f"sesion_{timestamp}.txt"

        with open(self.current_session_file, "w", encoding="utf-8") as f:
            f.write(f"SESION: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")

    def log_action(self, action: str, details: str = ""):
        if not self.current_session_file:
            self.current_session_file = (
                self.sessions_dir
                / f"sesion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            )
            with open(self.current_session_file, "w", encoding="utf-8") as f:
                f.write(f"SESION: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")

        timestamp = datetime.now().strftime("%H:%M:%S")

        with open(self.current_session_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {action}\n")
            if details:
                f.write(f"         {details}\n")
            f.write("\n")

    def log_success(self, message: str):
        self.log_action(f"OK: {message}")

    def log_error(self, message: str, details: str = ""):
        self.log_action(f"ERROR: {message}", details)

    def log_warning(self, message: str):
        self.log_action(f"AVISO: {message}")

    def save_archive_list(self, files: list[FileInfo], directory: str):
        folder_name = Path(directory).name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = "".join(c if c.isalnum() else "_" for c in folder_name)
        filename = f"lista_{timestamp}_{safe_name}.txt"
        filepath = self.archives_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"LISTA DE ARCHIVOS\n")
            f.write(f"=" * 60 + "\n")
            f.write(f"Carpeta: {directory}\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total archivos: {len(files)}\n")
            f.write("-" * 60 + "\n\n")

            ext_groups = {}
            for file in files:
                if file.extension not in ext_groups:
                    ext_groups[file.extension] = []
                ext_groups[file.extension].append(file)

            for ext in sorted(ext_groups.keys()):
                f.write(f"\n[{ext}] ({len(ext_groups[ext])} archivos)\n")
                f.write("-" * 40 + "\n")
                for file in ext_groups[ext]:
                    size = self._format_size(file.size)
                    f.write(f"  {file.name} ({size})\n")

        self.log_action(f"Lista guardada: {len(files)} archivos")
        return filepath

    def save_elimination_log(
        self, deleted: list[str], errors: list[dict], directory: str, operation: str
    ):
        date = datetime.now().strftime("%Y%m%d")
        filename = f"eliminaciones_{date}.txt"
        filepath = self.eliminations_dir / filename

        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"{'=' * 60}\n")
            f.write(f"FECHA: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"CARPETA: {directory}\n")
            f.write(f"OPERACION: {operation}\n")
            f.write(f"{'-' * 60}\n")

            if deleted:
                f.write(f"\nELIMINADOS ({len(deleted)}):\n")
                for name in deleted:
                    f.write(f"  - {name}\n")

            if errors:
                f.write(f"\nERRORES ({len(errors)}):\n")
                for err in errors:
                    f.write(f"  - {err['file']}: {err['error']}\n")

            f.write(f"\nTOTAL: {len(deleted)} eliminados, {len(errors)} errores\n\n")

        self.log_action(
            f"Registro de eliminacion guardado",
            f"Eliminados: {len(deleted)}, Errores: {len(errors)}",
        )
        return filepath

    def get_recent_archives(self, limit: int = 10) -> list[Path]:
        files = sorted(
            self.archives_dir.glob("lista_*.txt"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        return files[:limit]

    def get_elimination_log_path(self) -> Path:
        date = datetime.now().strftime("%Y%m%d")
        return self.eliminations_dir / f"eliminaciones_{date}.txt"

    @staticmethod
    def _format_size(size: int) -> str:
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"


class FileModel:
    def __init__(self, directory: str, logs_dir: Optional[Path] = None):
        self.directory = Path(directory)
        self.files: list[FileInfo] = []
        self.files_by_extension: dict[str, list[FileInfo]] = {}
        self.log_manager = LogManager(logs_dir or Path("logs"))

    def validate_path(self) -> bool:
        return self.directory.exists() and self.directory.is_dir()

    def scan_files(self, recursive: bool = False) -> list[FileInfo]:
        pattern = "**/*" if recursive else "*"
        self.files = []

        for path in self.directory.glob(pattern):
            if path.is_file():
                ext = path.suffix.lower() if path.suffix else "(sin extension)"
                file_info = FileInfo(
                    path=path, name=path.name, extension=ext, size=path.stat().st_size
                )
                self.files.append(file_info)

        self.log_manager.log_action(
            f"Escaneo completado",
            f"Directorio: {self.directory}, Archivos: {len(self.files)}",
        )
        return self.files

    def classify_by_extension(self) -> dict[str, list[FileInfo]]:
        self.files_by_extension = {}
        for file in self.files:
            if file.extension not in self.files_by_extension:
                self.files_by_extension[file.extension] = []
            self.files_by_extension[file.extension].append(file)
        return self.files_by_extension

    def get_file_by_name(self, name: str) -> Optional[FileInfo]:
        for file in self.files:
            if file.name.lower() == name.lower():
                return file
        return None

    def get_files_by_names(self, names: list[str]) -> tuple[list[FileInfo], list[str]]:
        found = []
        not_found = []
        for name in names:
            file = self.get_file_by_name(name.strip())
            if file:
                found.append(file)
            else:
                not_found.append(name)
        return found, not_found

    def calculate_hash(self, file_path: Path) -> str:
        hasher = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    def find_duplicates(self) -> list[list[FileInfo]]:
        self.log_manager.log_action("Calculando hashes para detectar duplicados...")

        for file in self.files:
            file.hash = self.calculate_hash(file.path)

        hash_groups: dict[str, list[FileInfo]] = {}
        for file in self.files:
            file_hash = file.hash or ""
            if file_hash not in hash_groups:
                hash_groups[file_hash] = []
            hash_groups[file_hash].append(file)

        duplicates = [group for group in hash_groups.values() if len(group) > 1]

        self.log_manager.log_action(
            f"Duplicados encontrados: {len(duplicates)} grupos",
            f"Archivos duplicados: {sum(len(g) - 1 for g in duplicates)}",
        )
        return duplicates

    def delete_file(self, file_info: FileInfo) -> tuple[bool, str]:
        try:
            if not file_info.path.exists():
                return False, "El archivo no existe"
            if not os.access(file_info.path, os.W_OK):
                return False, "El archivo esta protegido"
            file_info.path.unlink()
            return True, "Eliminado correctamente"
        except PermissionError:
            return False, "Permiso denegado"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def delete_files(
        self, files: list[FileInfo], operation: str = "Eliminacion por nombre"
    ) -> dict:
        results = {"deleted": [], "errors": []}

        self.log_manager.log_action(
            f"Iniciando {operation}", f"Archivos a eliminar: {len(files)}"
        )

        for file in files:
            success, message = self.delete_file(file)
            if success:
                results["deleted"].append(file.name)
            else:
                results["errors"].append({"file": file.name, "error": message})

        self.log_manager.save_elimination_log(
            results["deleted"], results["errors"], str(self.directory), operation
        )

        return results

    def save_archive_list(self) -> Path:
        return self.log_manager.save_archive_list(self.files, str(self.directory))
