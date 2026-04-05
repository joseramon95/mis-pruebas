# Eliminador Masivo de Archivos

Aplicación CLI/GUI para eliminación masiva de archivos con soporte para excepciones.

## Características

- **Selección de carpeta**: Escanea recursively todos los archivos en una carpeta
- **Clasificación por extensión**: Agrupa archivos por tipo de extensión
- **Eliminación masiva con excepciones**: Conserva archivos específicos y elimina el resto
- **Excepciones persistentes**: Las excepciones se guardan y cargan automáticamente
- **Interfaz GUI moderna**: Tema violeta con botones dorados e iconos
- **Logging completo**: Registra todas las operaciones en archivos de log

## Requisitos

- Python 3.10+
- tkinter (incluido en Python)

## Uso

### GUI (por defecto)

```bash
python main.py
```

### CLI

```bash
python main.py --cli
python main.py --cli /ruta/a/carpeta
```

## Estructura del Proyecto

```
file-organizer-cli/
├── app/
│   ├── gui.py              # Interfaz gráfica (Tkinter)
│   ├── gui_controller.py   # Controlador de la GUI
│   ├── model.py            # Modelo de datos y lógica de archivos
│   ├── controller.py       # Controlador CLI
│   └── view.py             # Vista CLI
├── tests/
│   ├── test_app.py         # Tests de modelo/controlador
│   └── test_gui.py         # Tests de GUI
├── logs/
│   ├── archivos/           # Listas de archivos escaneados
│   ├── eliminaciones/      # Registros de eliminaciones
│   └── sesiones/           # Registros de sesiones
└── main.py                 # Punto de entrada
```

## Guía de Uso (GUI)

1. **Seleccionar Carpeta**: Carga todos los archivos de la carpeta seleccionada
2. **Clasificar**: Muestra los archivos agrupados por tipo de extensión
3. **Mostrar Todos**: Vuelve a mostrar la lista completa de archivos
4. **Eliminar**: 
   - Si hay excepciones configuradas: elimina todos los archivos EXCEPTO los exceptuados
   - Si no hay excepciones: abre diálogo para seleccionar archivos a eliminar
5. **Excepciones**: Define qué archivos NO se deben eliminar (se pueden editar posteriormente)
6. **Limpiar**: Borra todas las excepciones configuradas

## Excepciones

Las excepciones son nombres de archivos que se preservarán durante la eliminación masiva. Se guardan en `logs/archivos/excepciones.txt` y se cargan automáticamente al seleccionar una carpeta.

### Formato de excepciones
Un nombre de archivo por línea:
```
archivo_importante.txt
foto_navidad.jpg
documento.pdf
```

## Logging

- **Sesiones**: `logs/sesiones/sesion_YYYYMMDD_HHMMSS.txt`
- **Listas de archivos**: `logs/archivos/lista_YYYYMMDD_HHMMSS_CARPETA.txt`
- **Excepciones**: `logs/archivos/excepciones.txt`
- **Eliminaciones**: `logs/eliminaciones/eliminaciones_YYYYMMDD.txt`

## Tests

```bash
pytest file-organizer-cli/tests/ -v
```

## API Pública (Modelo)

### FileModel

```python
model = FileModel(ruta_carpeta, logs_dir)
model.validate_path()        # Valida que la ruta existe
model.scan_files(recursive)  # Escanea archivos
model.classify_by_extension() # Clasifica por extensión
model.delete_files(files, operacion, excluded)  # Elimina archivos
model.load_exclusion_list()   # Carga excepciones
model.save_exclusion_list(exceptions)  # Guarda excepciones
```

### GUIController

```python
controller = GUIController()
controller.set_directory(ruta)  # Configura la carpeta
controller.on_select_folder()    # Escanea carpeta
controller.on_delete_selection() # Elimina archivos (usa excepciones si existen)
controller.on_exceptions()       # Abre diálogo de excepciones
controller.on_clear()            # Limpia excepciones
```
