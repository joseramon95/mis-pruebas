from pathlib import Path
from app.model import FileInfo


class View:
    def show_banner(self):
        print("\n" + "=" * 50)
        print("  ELIMINADOR MASIVO DE ARCHIVOS")
        print("=" * 50 + "\n")

    def show_main_menu(self):
        print("¿Qué deseas hacer?")
        print("  1. Escanear carpeta")
        print("  2. Mostrar archivos encontrados")
        print("  3. Clasificar por extensión")
        print("  4. Eliminar duplicados")
        print("  5. Eliminar por nombre")
        print("  0. Salir")
        print()

    def show_files(self, files: list[FileInfo]):
        print(f"\n📁 Archivos encontrados: {len(files)}\n")
        print(f"{'#':<5} {'Nombre':<50} {'Ext':<15} {'Tamaño'}")
        print("-" * 80)
        for i, file in enumerate(files, 1):
            size = self._format_size(file.size)
            print(f"{i:<5} {file.name:<50} {file.extension:<15} {size}")
        print()

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
            print(f"Grupo {i} ({len(group)} archivos):")
            for f in group:
                print(f"  - {f.name}")
            print()

    def show_delete_preview(self, files: list[FileInfo]):
        print("\n🗑️  PREVIEW - Archivos a eliminar:")
        print("-" * 50)
        for f in files:
            print(f"  - {f.name}")
        print(f"\nTotal: {len(files)} archivos")
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

        print()

    def show_log_saved(self, filepath: Path):
        print(f"\n📝 Log guardado en: {filepath}\n")

    def show_log_location(self, filepath: Path):
        print(f"\n📁 Ubicación del log: {filepath}\n")

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

    def ask_delete_option(self) -> str:
        print("\n¿Eliminar duplicados o ingresar nombres?")
        print("  1. Eliminar duplicados")
        print("  2. Ingresar nombres de archivos")
        return self.prompt("Elige una opción (1/2)")

    @staticmethod
    def _format_size(size: int) -> str:
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"
