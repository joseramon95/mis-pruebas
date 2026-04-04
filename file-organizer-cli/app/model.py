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
        self.logs_dir.mkdir(exist_ok=True)

    def save_file_list(self, files: list[FileInfo], directory: str):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"archivos_{timestamp}.txt"
        filepath = self.logs_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Directorio: {directory}\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total archivos: {len(files)}\n")
            f.write("=" * 50 + "\n\n")

            for i, file in enumerate(files, 1):
                f.write(f"{i}. {file.name}\n")

        return filepath

    def append_elimination_log(self, deleted_files: list[str], directory: str):
        filepath = self.logs_dir / "eliminacion masiva de archivos.txt"

        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Directorio: {directory}\n")
            f.write("Archivos eliminados:\n")
            for name in deleted_files:
                f.write(f"  - {name}\n")
            f.write("---\n\n")

    def get_log_path(self) -> Path:
        return self.logs_dir / "eliminacion masiva de archivos.txt"


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
                ext = path.suffix.lower() if path.suffix else "(sin extensión)"
                file_info = FileInfo(
                    path=path, name=path.name, extension=ext, size=path.stat().st_size
                )
                self.files.append(file_info)

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
        for file in self.files:
            file.hash = self.calculate_hash(file.path)

        hash_groups: dict[str, list[FileInfo]] = {}
        for file in self.files:
            file_hash = file.hash or ""
            if file_hash not in hash_groups:
                hash_groups[file_hash] = []
            hash_groups[file_hash].append(file)

        return [group for group in hash_groups.values() if len(group) > 1]

    def delete_file(self, file_info: FileInfo) -> tuple[bool, str]:
        try:
            if not file_info.path.exists():
                return False, "El archivo no existe"
            if not os.access(file_info.path, os.W_OK):
                return False, "El archivo está protegido"
            file_info.path.unlink()
            return True, "Eliminado correctamente"
        except PermissionError:
            return False, "Permiso denegado"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def delete_files(self, files: list[FileInfo]) -> dict:
        results = {"deleted": [], "errors": []}
        for file in files:
            success, message = self.delete_file(file)
            if success:
                results["deleted"].append(file.name)
            else:
                results["errors"].append({"file": file.name, "error": message})
        return results

    def save_file_list(self) -> Path:
        return self.log_manager.save_file_list(self.files, str(self.directory))

    def log_elimination(self, deleted_files: list[str]):
        self.log_manager.append_elimination_log(deleted_files, str(self.directory))

    def get_elimination_log_path(self) -> Path:
        return self.log_manager.get_log_path()
