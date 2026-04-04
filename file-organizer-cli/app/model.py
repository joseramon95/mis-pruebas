from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import hashlib
import os


@dataclass
class FileInfo:
    path: Path
    name: str
    extension: str
    size: int
    hash: Optional[str] = None

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int):
        self._index = value


class FileModel:
    def __init__(self, directory: str):
        self.directory = Path(directory)
        self.files: list[FileInfo] = []
        self.files_by_extension: dict[str, list[FileInfo]] = {}

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

        for i, file in enumerate(self.files, start=1):
            file.index = i

        return self.files

    def classify_by_extension(self) -> dict[str, list[FileInfo]]:
        self.files_by_extension = {}
        for file in self.files:
            if file.extension not in self.files_by_extension:
                self.files_by_extension[file.extension] = []
            self.files_by_extension[file.extension].append(file)
        return self.files_by_extension

    def get_file_by_index(self, index: int) -> Optional[FileInfo]:
        for file in self.files:
            if file.index == index:
                return file
        return None

    def get_files_by_pattern(self, pattern: str) -> list[FileInfo]:
        pattern_lower = pattern.lower().replace("*", "")
        return [f for f in self.files if pattern_lower in f.name.lower()]

    def get_files_by_extension(self, ext: str) -> list[FileInfo]:
        ext = ext if ext.startswith(".") else f".{ext}"
        return [f for f in self.files if f.extension.lower() == ext.lower()]

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
        results = {"deleted": [], "errors": [], "skipped": []}
        for file in files:
            success, message = self.delete_file(file)
            if success:
                results["deleted"].append(file.name)
            else:
                results["errors"].append({"file": file.name, "error": message})
        return results
