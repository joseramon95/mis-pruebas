# Especificaciones del Proyecto

## PROYECTO: ORGANIZADOR DE ARCHIVOS POR EXTENSIÓN (CLI)
## ARQUITECTURA: MVC (Modelo - Vista - Controlador)

---

## 1. OBJETIVO GENERAL

Desarrollar una aplicación que lea los archivos de una ruta especificada por el usuario, los clasifique por extensión, permita eliminarlos mediante una lista interactiva y detecte/elimine duplicados, manteniendo una arquitectura MVC clara y escalable.

---

## 2. REQUERIMIENTOS FUNCIONALES

### 2.1 Entrada del usuario

- El usuario debe poder proporcionar una ruta de carpeta.
- El sistema debe validar que la ruta exista.
- Debe permitir recibir opciones adicionales:
  - Escanear archivos
  - Clasificar por extensión
  - Eliminar archivos
  - Eliminar duplicados

---

### 2.2 Lectura de archivos

- Listar todos los archivos dentro de la carpeta.
- Ignorar carpetas (solo procesar archivos).
- Detectar archivos sin extensión.
- Soportar modo recursivo.

---

### 2.3 Clasificación

- Identificar la extensión de cada archivo.
- Agrupar los archivos por extensión.
- Manejar extensiones en minúsculas.

---

### 2.4 Visualización/Organización (VERSIÓN ACTUAL)

- Mostrar los archivos agrupados por extensión en pantalla.
- NO mover ni crear carpetas (futura implementación).
- Formato de salida: tabla o lista clara por extensión.

---

### 2.5 Eliminación de archivos (EN DESARROLLO)

El sistema debe permitir eliminar archivos mediante una lista interactiva.

**Flujo de eliminación:**

1. El sistema muestra TODOS los archivos encontrados en la carpeta.
2. Cada archivo tiene un número/índice asociado.
3. El usuario introduce los índices de los archivos a eliminar (ej: 1,3,5-7,9).
4. El sistema muestra PREVIEW de lo que se eliminará.
5. El usuario confirma con "yes" para proceder.
6. El sistema elimina y muestra reporte final.

**Métodos de selección de archivos:**

| Método | Ejemplo | Descripción |
|--------|---------|-------------|
| Por índice | `3` | Archivo #3 |
| Múltiple | `1,3,5` | Archivos 1, 3 y 5 |
| Rango | `1-10` | Archivos del 1 al 10 |
| Patrón | `rom*gba*` | Archivos que coincidan |
| Extensión | `.gba` | Todos los .gba |
| Todos | `all` | Seleccionar todos |

**Validaciones obligatorias:**

- Verificar que el archivo exista antes de intentar eliminar.
- Verificar que no esté protegido/solo lectura.
- Manejar nombres con espacios o caracteres especiales.
- Si un archivo no existe, warn y continuar con los demás.

**Registro:**

- Guardar lista de archivos eliminados con timestamp.
- Mostrar resumen: eliminados, errores, skipped.

**SEGURIDAD:** No hay eliminación automática. Siempre hay confirmación.

---

### 2.6 Eliminación de duplicados

El sistema debe detectar y eliminar archivos duplicados.

**Definición de duplicado:**
- Archivos con el mismo contenido (no solo nombre).

**Proceso:**
- Comparar archivos mediante:
  - Tamaño
  - Contenido (hash MD5)
- Agrupar archivos duplicados.
- Conservar uno y eliminar los demás.

---

### 2.7 Visualización

Mostrar:
- Archivos encontrados
- Agrupación por extensión
- Archivos eliminados
- Duplicados detectados
- Acciones realizadas

---

### 2.8 Opciones de ejecución

- Modo solo lectura (escanear/clasificar)
- Modo eliminación
- Modo eliminación de duplicados
- Modo recursivo

---

## 3. REQUERIMIENTOS NO FUNCIONALES

- Uso de arquitectura MVC.
- Código modular y mantenible.
- Manejo robusto de errores.
- Compatibilidad multiplataforma.
- Soporte para pruebas automatizadas.
- Seguridad en operaciones de eliminación.

---

## 4. ARQUITECTURA MVC

### 4.1 Modelo (Model)
**Responsabilidades:**
- Acceso a archivos.
- Lectura de directorios.
- Clasificación por extensión.
- Eliminación de archivos.
- Detección de duplicados.
- Cálculo de hashes o comparaciones.

El modelo NO debe:
- Mostrar datos al usuario.

---

### 4.2 Vista (View)
**Responsabilidades:**
- Mostrar información al usuario.
- Mostrar advertencias.
- Mostrar resultados de eliminación y duplicados.
- Solicitar confirmaciones.

La vista NO debe:
- Manipular archivos directamente.

---

### 4.3 Controlador (Controller)
**Responsabilidades:**
- Recibir parámetros del usuario.
- Validar entradas.
- Decidir qué acciones ejecutar:
  - Organizar
  - Eliminar
  - Detectar duplicados
- Coordinar modelo y vista.

---

## 5. CASOS ESPECIALES

- Archivos inexistentes en lista de eliminación
- Archivos protegidos
- Archivos sin extensión
- Nombres duplicados pero contenido diferente
- Permisos insuficientes

---

## 6. SEGURIDAD Y PREVENCIÓN

- Confirmación antes de eliminar archivos.
- Opción de simulación (modo prueba).
- Registro de archivos eliminados.
- Evitar eliminación accidental masiva.

---

## 7. PRUEBAS (QA)

Se deben validar:
- Eliminación correcta por selección interactiva
- Detección correcta de duplicados
- No eliminación de archivos únicos
- Manejo de errores
- Integridad de archivos restantes

---

## 8. MEJORAS FUTURAS

- [ ] Organizar archivos en carpetas por extensión
- [ ] Interfaz gráfica
- [ ] Papelera de reciclaje interna
- [ ] Reportes en formato JSON o CSV
- [ ] Integración con nube
- [ ] Historial de operaciones
- [ ] Pruebas automatizadas

---

## HISTORIAL DE CAMBIOS

### v0.1.0 (2026-04-04)
- Esqueleto MVC creado
- Implementación básica de:
  - Escaneo de directorios
  - Clasificación por extensión
  - Eliminación interactiva de archivos
  - Detección de duplicados por hash
- Documentación inicial
