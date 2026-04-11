# Agentes - Reglas de Operación

## 1. Lectura Inicial al Iniciar Sesión

Al comenzar cada sesión, el agente DEBE:

- Escanear la estructura del proyecto
- Leer los archivos principales de cada proyecto (package.json, src/, etc.)
- Identificar las tecnologías utilizadas en cada proyecto
- Documentar brevemente la estructura de cada proyecto

## 2. Mantenimiento de Documentación - FLUJO_DEPENDENCIAS.md

El agente DEBE mantener actualizada la documentación `FLUJO_DEPENDENCIAS.md` después de cada cambio en el proyecto.

### Regla de Actualización

Después de implementar cualquier cambio que afecte:

1. **Componentes**: Agregar/eliminar/modificar componentes que usen `getComponente()`
2. **APIs/Rutas**: Nuevos endpoints, cambios en URLs, estructuras de datos
3. **Interfaces/Tipos**: Modificaciones en `componentes.ts`, `carouselItems.ts`, etc.
4. **Flujo de datos**: Cambios en cómo se obtienen o procesan los datos

### Regla de Eliminación

Si se elimina cualquier elemento del proyecto:

1. **Componente eliminado**: Remover su entrada de la documentación
2. **API endpoint eliminado**: Eliminarlo de la lista de endpoints
3. **Campo de interfaz eliminado**: Remover el campo de la documentación
4. **Archivo de datos eliminado**: Eliminarlo de la sección correspondiente

### Formato de Actualización

Al hacer cambios, el agente DEBE:
1. Leer `FLUJO_DEPENDENCIAS.md` antes de modificar código
2. Actualizar el archivo inmediatamente después del cambio
3. Usar el mismo formato y estilo de la documentación existente
4. Incluir notas sobre cambios si son significativos

## 3. Reglas de Git - Push

### Consulta Obligatoria Antes de Push

El agente DEBE consultar SIEMPRE antes de ejecutar cualquier comando `git push`. No está autorizado para hacer push automáticamente.

### Verificación Pre-Push

Si el usuario concede permiso para hacer push, el agente DEBE verificar:

1. **Limpieza de ramas**: Confirmar que no existan carpetas o proyectos de una rama en otra
   - Ejemplo: Si existe un sitio web de Astro, DEBE estar únicamente en la rama `astro` o similar, NO mezclado en otras ramas
   - Verificar que cada proyecto/carpeta esté en su rama correspondiente

2. **Archivos no relacionados**: Asegurarse de que no haya archivos de un proyecto en la rama de otro

3. **Estado del repositorio**: Verificar con `git status` y `git diff` antes de cualquier push

## 4. Gitignore - Limpieza de Ramas

El agente DEBE agregar al `.gitignore` todas las carpetas y archivos que NO sean parte del proyecto principal:

### Archivos y Carpetas a Ignorar

```
# Archivos del sistema
.DS_Store
Thumbs.db
Desktop.ini
*.log

# Carpetas de dependencias
node_modules/
vendor/
venv/
.venv/

# Builds y outputs
dist/
build/
out/
*.egg-info/

# Archivos de configuración local
.env.local
.env.*.local
*.local

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Archivos temporales
tmp/
temp/
*.tmp
nul

# Paquetes
package-lock.json (si no es necesario)
yarn.lock (si no es necesario)
pnpm-lock.yaml (si no es necesario)
```

### Regla General

Solo hacer commit de archivos que:
- Sean código fuente del proyecto
- Sean archivos de configuración esenciales
- Sean archivos de documentación necesarios
- Sean assets necesarios para el proyecto

TODO: Revisar y actualizar esta lista según las necesidades específicas de cada proyecto.
