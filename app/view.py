from datetime import datetime
from app.model import FileInfo


class View:
    def __init__(self):
        self.delete_log: list[dict] = []

    def show_banner(self):
        print("\n" + "=" * 50)
        print("  ORGANIZADOR DE ARCHIVOS CLI")
        print("=" * 50 + "\n")

    def show_menu(self):
        print("Opciones:")
        print("  1. Escanear carpeta")
        print("  2. Clasificar por extensión")
        print("  3. Eliminar archivos")
        print("  4. Buscar duplicados")
        print("  5. Mostrar archivos")
        print("  0. Salir")
        print()

    def show_files(self, files: list[FileInfo]):
        print(f"\n📁 Archivos encontrados: {len(files)}\n")
        print(f"{'#':<5} {'Nombre':<40} {'Ext':<15} {'Tamaño'}")
        print("-" * 75)
        for file in files:
            size = self._format_size(file.size)
            print(f"{file.index:<5} {file.name:<40} {file.extension:<15} {size}")

    def show_by_extension(self, classified: dict[str, list[FileInfo]]):
        print(f"\n📂 Clasificación por extensión ({len(classified)} tipos)\n")
        for ext, files in sorted(classified.items()):
            print(f"  [{ext}] ({len(files)} archivos)")
            for f in files[:5]:
                print(f"    - {f.name}")
            if len(files) > 5:
                print(f"    ... y {len(files) - 5} más")
            print()

    def show_duplicates(self, duplicates: list[list[FileInfo]]):
        if not duplicates:
            print("\n✅ No se encontraron duplicados\n")
            return

        print(f"\n⚠️  Duplicados encontrados: {len(duplicates)} grupos\n")
        for i, group in enumerate(duplicates, 1):
            print(f"Grupo {i} ({len(group)} archivos, mismo hash):")
            for f in group:
                print(f"  - {f.path}")
        print()

    def show_delete_preview(self, files: list[FileInfo]):
        print("\n🗑️  PREVIEW - Archivos a eliminar:")
        print("-" * 50)
        total_size = 0
        for f in files:
            print(f"  {f.index}. {f.name}")
            total_size += f.size
        print("-" * 50)
        print(f"Total: {len(files)} archivos ({self._format_size(total_size)})")
        print()

    def show_delete_results(self, results: dict):
        print("\n📊 RESULTADO DE ELIMINACIÓN:")
        print("-" * 50)

        if results["deleted"]:
            print(f"✅ Eliminados: {len(results['deleted'])}")
            for name in results["deleted"]:
                print(f"   - {name}")

        if results["errors"]:
            print(f"\n❌ Errores: {len(results['errors'])}")
            for item in results["errors"]:
                print(f"   - {item['file']}: {item['error']}")

        self.delete_log.append(
            {"timestamp": datetime.now().isoformat(), "results": results}
        )
        print()

    def show_error(self, message: str):
        print(f"\n❌ Error: {message}\n")

    def show_success(self, message: str):
        print(f"\n✅ {message}\n")

    def show_info(self, message: str):
        print(f"\nℹ️  {message}\n")

    def prompt(self, message: str) -> str:
        return input(f"{message}: ").strip()

    def confirm(self, message: str) -> bool:
        response = input(f"{message} (yes/no): ").strip().lower()
        return response in ["yes", "y", "si", "s"]

    def show_help_delete(self):
        print("\n📖 Ayuda para eliminación:")
        print("  - Escribe números separados por coma: 1,3,5")
        print("  - Rangos con guíon: 1-10")
        print("  - Patrón: rom*gba*")
        print("  - Extensión: .gba")
        print("  - 'all' para seleccionar todos")
        print("  - 'q' para cancelar")
        print()

    @staticmethod
    def _format_size(size: int) -> str:
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"
