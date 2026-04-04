# Organizador de Archivos CLI

Herramienta CLI para gestionar y eliminar archivos con detección de duplicados y sistema de logs.

## Características

- **Escaneo de directorios**: Lee archivos de forma recursiva o superficial
- **Clasificación por extensión**: Agrupa archivos por su tipo (solo visualización)
- **Sistema de logs**: Registra archivos encontrados y eliminaciones
- **Eliminación por nombres**: Elimina archivos especificando sus nombres
- **Detección de duplicados**: Encuentra archivos con contenido idéntico mediante hash MD5
- **Confirmación de seguridad**: Siempre pide confirmación antes de eliminar

## Estructura del Proyecto

```
file-organizer-cli/
├── app/
│   ├── __init__.py
│   ├── model.py      # Lógica de archivos, hashes, eliminación
│   ├── view.py       # Interfaz de usuario en consola
│   └── controller.py # Coordinación y flujo
├── logs/             # Carpeta de logs (se crea automáticamente)
├── main.py           # Punto de entrada
├── README.md         # Este archivo
└── SPEC.md           # Especificaciones completas
```

## Requisitos

- Python 3.10+

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

## Flujo de eliminación

1. Elegir ruta de la carpeta a procesar
2. Escanear archivos → se genera log de referencia en `logs/`
3. Elegir opción:
   - **Eliminar duplicados**: Detecta y elimina automáticamente
   - **Ingresar nombres**: Escribir nombres de archivos a eliminar
4. Confirmar eliminación
5. Ver registro en log acumulable

## Sistema de Logs

La carpeta `logs/` contiene:

- **Archivos encontrados**: Lista de todos los archivos en la carpeta escaneada
- **eliminacion masiva de archivos.txt**: Registro acumulativo de eliminaciones

**Formato del log:**
```
Fecha: 2026-04-04 13:30:00
Archivos eliminados:
  - archivo1.ext
  - archivo2.ext
---
```

## Arquitectura MVC

- **Model**: Gestiona lectura de archivos, clasificación, hashing y eliminación
- **View**: Maneja toda la salida por consola y prompts al usuario
- **Controller**: Coordina modelo y vista, controla el flujo principal

## Seguridad

- Siempre pide confirmación antes de eliminar
- Genera logs de todas las operaciones
- Manejo de archivos protegidos/solo lectura
