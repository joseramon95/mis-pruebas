# Organizador de Archivos CLI

Herramienta CLI para organizar y gestionar archivos por extensión con detección de duplicados.

## Características

- **Escaneo de directorios**: Lee archivos de forma recursiva o superficial
- **Clasificación por extensión**: Agrupa archivos por su tipo
- **Eliminación interactiva**: Selecciona archivos por índice, rango, patrón o extensión
- **Detección de duplicados**: Encuentra archivos con contenido idéntico mediante hash MD5
- **Confirmación de seguridad**: Vista previa y confirmación antes de eliminar

## Estructura del Proyecto

```
├── app/
│   ├── __init__.py
│   ├── model.py      # Lógica de archivos, hashes, eliminación
│   ├── view.py       # Interfaz de usuario en consola
│   └── controller.py # Coordinación y parseo de entrada
├── main.py           # Punto de entrada
├── README.md         # Este archivo
└── SPEC.md           # Especificaciones del proyecto
```

## Requisitos

- Python 3.10+

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

### Uso básico con directorio como argumento

```bash
python main.py "C:\carpeta\roms"
```

### Uso interactivo

```bash
python main.py
# Luego introduce la ruta cuando se solicite
```

### Menú de opciones

```
1. Escanear carpeta
2. Clasificar por extensión
3. Eliminar archivos
4. Buscar duplicados
5. Mostrar archivos
0. Salir
```

## Eliminación de archivos

### Métodos de selección

| Método | Ejemplo | Descripción |
|--------|---------|-------------|
| Individual | `3` | Elimina archivo #3 |
| Múltiple | `1,3,5` | Elimina archivos 1, 3 y 5 |
| Rango | `1-10` | Elimina archivos del 1 al 10 |
| Patrón | `rom*gba*` | Elimina archivos que contengan "rom*gba*" |
| Extensión | `.gba` | Elimina todos los .gba |
| Todos | `all` | Selecciona todos los archivos |

### Flujo de eliminación

1. Selecciona archivos a eliminar
2. Ver preview de archivos a borrar
3. Confirma con `yes` para proceder
4. Revisa el reporte de resultados

## Arquitectura MVC

- **Model**: Gestiona lectura de archivos, clasificación, hashing y eliminación
- **View**: Maneja toda la salida por consola y prompts al usuario
- **Controller**: Coordina modelo y vista, procesa entrada del usuario

## Licencia

MIT
