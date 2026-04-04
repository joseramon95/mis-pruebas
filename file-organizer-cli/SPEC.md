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

### 2.4 Visualización/Organización

- Mostrar los archivos agrupados por extensión en pantalla (solo visualización).
- NO mover ni crear carpetas.
- Generar archivo de log con la lista de archivos encontrados.
- Formato de salida: tabla o lista clara por extensión.

---

### 2.5 Sistema de Logs

- Crear carpeta `logs/` en el directorio del proyecto.
- Generar archivo con la lista de archivos encontrados (referencia).
- Generar archivo acumulable `eliminacion masiva de archivos.txt` con registro de eliminaciones.

**Formato del log de eliminación:**
```
Fecha: YYYY-MM-DD HH:MM:SS
Archivos eliminados:
  - archivo1.ext
  - archivo2.ext
---
```

---

### 2.6 Eliminación de archivos

**Flujo completo:**

1. Elegir ruta de la carpeta a procesar.
2. Escanear archivos y crear log de referencia en `logs/`.
3. Preguntar al usuario: "¿Eliminar duplicados o ingresar nombres?"
4. Si elige "duplicados": detectar y eliminar automáticamente.
5. Si elige "ingresar nombres":
   - Mostrar ubicación del log de referencia.
   - Solicitar nombres de archivos a eliminar.
   - Confirmar antes de eliminar.
6. Registrar todo en el log acumulable.

**Validaciones obligatorias:**

- Verificar que el archivo exista antes de eliminar.
- Verificar que no esté protegido/solo lectura.
- Manejar nombres con espacios o caracteres especiales.

**SEGURIDAD:** Siempre hay confirmación antes de eliminar.

---

### 2.7 Eliminación de duplicados

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

### 2.8 Visualización

Mostrar:
- Archivos encontrados
- Agrupación por extensión
- Archivos eliminados
- Duplicados detectados
- Acciones realizadas

---

### 2.9 Opciones de ejecución

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

### v0.2.0 (2026-04-04)
- Actualizado flujo de eliminación según nuevos requisitos
- Añadido sistema de logs en carpeta `logs/`
- Log acumulable para registro de eliminaciones masivas
- Organizador ahora solo muestra en pantalla (sin mover archivos)

### v0.1.0 (2026-04-04)
- Esqueleto MVC creado
- Implementación básica de:
  - Escaneo de directorios
  - Clasificación por extensión
  - Eliminación interactiva de archivos
  - Detección de duplicados por hash
- Documentación inicial
