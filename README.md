# E³ Admin - Panel de Administración

Panel de administración completo para gestionar el contenido del sitio E³.

## 🚀 Inicio Rápido

```bash
# Navegar al proyecto
cd E3_Admin

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
python app.py
```

Abrir en el navegador: **http://localhost:5000**

## 🔐 Credenciales por Defecto

| Campo | Valor |
|-------|-------|
| Usuario | `root` |
| Contraseña | `root` |

> ⚠️ **Importante:** Cambia la contraseña del usuario root después del primer acceso.

## 📁 Estructura del Proyecto

```
E3_Admin/
├── app.py                  # Aplicación Flask + Rutas
├── requirements.txt         # Dependencias Python
├── e3_admin.db            # Base de datos SQLite (generada)
├── templates/              # Plantillas HTML
│   ├── base.html          # Plantilla base + Sidebar
│   ├── login.html         # Página de login
│   ├── dashboard.html     # Panel principal
│   ├── logs.html          # Registro de actividad
│   ├── socios/
│   │   ├── lista.html    # Lista de socios
│   │   └── form.html     # Formulario crear/editar socio
│   ├── componentes/
│   │   ├── lista.html   # Lista de componentes
│   │   └── form.html    # Formulario editar componente
│   └── usuarios/
│       ├── lista.html    # Lista de usuarios
│       └── form.html    # Formulario crear/editar usuario
└── README.md
```

## 🗺️ Mapa de Módulos y Funciones

```
┌─────────────────────────────────────────────────────────────────────┐
│                         app.py (Aplicación Principal)                │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                     MODELOS (SQLAlchemy)                      │  │
│  │  ┌─────────┐  ┌─────────┐  ┌────────────┐  ┌────────────┐  │  │
│  │  │Usuario  │  │  Socio  │  │Componente  │  │    Log    │  │  │
│  │  └────┬────┘  └────┬────┘  └─────┬──────┘  └─────┬──────┘  │  │
│  │       │            │             │                │           │  │
│  │       ▼            ▼             ▼                ▼           │  │
│  │  ┌────────────────────────────────────────────────────────┐  │  │
│  │  │               RUTAS / ENDPOINTS                        │  │  │
│  │  │                                                        │  │  │
│  │  │  /login        → login.html                            │  │  │
│  │  │  /dashboard    → dashboard.html                       │  │  │
│  │  │  /socios       → socios/lista.html                    │  │  │
│  │  │  /socios/nuevo → socios/form.html                     │  │  │
│  │  │  /componentes  → componentes/lista.html               │  │  │
│  │  │  /usuarios     → usuarios/lista.html                  │  │  │
│  │  │  /logs         → logs.html                            │  │  │
│  │  │  /api/socios   → JSON (público)                      │  │  │
│  │  │  /api/componentes → JSON (público)                   │  │  │
│  │  └────────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

## 🧩 Módulos y sus Funciones

### 📋 `app.py` - Aplicación Principal

#### Configuración (Líneas 1-15)
```python
# Configura Flask y SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e3-admin-secret-key-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///e3_admin.db'
```
| Elemento | Descripción |
|----------|-------------|
| SECRET_KEY | Clave para sesiones |
| SQLALCHEMY_DATABASE_URI | Ubicación de SQLite |

---

#### Modelos SQLAlchemy (Líneas 17-65)

**Usuario (17-25)**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | Identificador único |
| username | String(50) | Usuario único |
| password_hash | String(200) | Contraseña encriptada |
| rol | String(20) | admin o editor |
| activo | Boolean | Estado |
| created_at | DateTime | Fecha creación |

**Socio (27-35)**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | Identificador único |
| nombre | String(100) | Nombre del asesor |
| descripcion | Text | Bio/perfil |
| imagen | String(200) | URL imagen |
| whatsapp | String(200) | Link WhatsApp |
| activo | Boolean | Visible en carrusel |
| orden | Integer | Posición en carrusel |

**Componente (37-45)**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | Identificador único |
| nombre | String(50) | ID del componente (Hero, CTA, etc.) |
| titulo | String(200) | Título principal |
| subtitulo | String(200) | Subtítulo |
| contenido | Text | Contenido principal |
| link | String(200) | Link/botón |
| extra_data | Text | JSON extra |
| updated_at | DateTime | Última modificación |

**Log (47-56)**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | Identificador único |
| usuario_id | Integer FK | Usuario que realizó acción |
| accion | String(50) | LOGIN, CREAR, EDITAR, etc. |
| componente_afectado | String(100) | Qué se afectó |
| detalle | Text | Detalles adicionales |
| ip_address | String(50) | IP del cliente |
| timestamp | DateTime | Momento del evento |

---

#### Rutas y sus Funciones

**Autenticación**
| Ruta | Función | Archivo Template | Descripción |
|------|---------|-----------------|-------------|
| `/` | `index()` | - | Redirige a /login |
| `/login` | `login()` | login.html | Login de usuarios |
| `/logout` | `logout()` | - | Cerrar sesión |

**Dashboard**
| Ruta | Función | Archivo Template | Descripción |
|------|---------|-----------------|-------------|
| `/dashboard` | `dashboard()` | dashboard.html | Panel principal con stats |

**Socios** (Afecta: Carousel en E³)
| Ruta | Función | Archivo Template | Descripción |
|------|---------|-----------------|-------------|
| `/socios` | `listar_socios()` | socios/lista.html | Lista todos |
| `/socios/nuevo` | `nuevo_socio()` | socios/form.html | Crear nuevo |
| `/socios/editar/<id>` | `editar_socio()` | socios/form.html | Editar existente |
| `/socios/eliminar/<id>` | `eliminar_socio()` | - | Eliminar |
| `/socios/toggle/<id>` | `toggle_socio()` | - | Activar/Desactivar |

**Componentes** (Afecta: Todos los componentes en E³)
| Ruta | Función | Archivo Template | Descripción |
|------|---------|-----------------|-------------|
| `/componentes` | `listar_componentes()` | componentes/lista.html | Lista todos |
| `/componentes/editar/<id>` | `editar_componente()` | componentes/form.html | Editar existente |

**Usuarios** (Afecta: Acceso al admin)
| Ruta | Función | Archivo Template | Descripción |
|------|---------|-----------------|-------------|
| `/usuarios` | `listar_usuarios()` | usuarios/lista.html | Lista todos |
| `/usuarios/nuevo` | `nuevo_usuario()` | usuarios/form.html | Crear nuevo |
| `/usuarios/editar/<id>` | `editar_usuario()` | usuarios/form.html | Editar existente |
| `/usuarios/eliminar/<id>` | `eliminar_usuario()` | - | Eliminar |

**Logs** (Lee: Todas las tablas)
| Ruta | Función | Archivo Template | Descripción |
|------|---------|-----------------|-------------|
| `/logs` | `ver_logs()` | logs.html | Ver historial |

**API** (Para consumo externo)
| Ruta | Función | Descripción | Afecta |
|------|---------|-------------|--------|
| `/api/socios` | `api_socios()` | JSON socios activos | E³ Carousel |
| `/api/componentes` | `api_componentes()` | JSON componentes | E³ Componentes |

---

#### Funciones Auxiliares (Líneas 67-90)

**`login_required(f)`**
- Decorador que protege rutas
- Verifica `session['user_id']`
- Redirige a `/login` si no hay sesión

**`log_accion(accion, componente, detalle)`**
- Registra acciones en tabla Log
- Guarda: usuario_id, accion, componente, detalle, ip
- Se llama desde todas las rutas de modificación

---

### 📋 Templates y su Función

#### `base.html` - Plantilla Base
| Sección | Descripción |
|---------|-------------|
| Sidebar | Navegación lateral con iconos |
| Menu items | Dashboard, Socios, Componentes, Usuarios, Logs |
| User info | Avatar + nombre + logout |
| Flash messages | Notificaciones de éxito/error |
| Content block | Contenido específico por página |

#### `login.html`
- Formulario: username + password
- Valida contra tabla Usuario
- Crea sesión si es correcto
- Registra LOGIN en Log

#### `dashboard.html`
- Stats cards: Socios, Componentes, Usuarios, Logs hoy
- Tabla: Actividad reciente (últimos 10 logs)
- Link: "Ver todos" → /logs

#### `socios/lista.html`
- Tabla: Orden, Nombre, Descripción, WhatsApp, Estado, Acciones
- Botón crear nuevo
- Toggle para activar/desactivar
- Editar/Eliminar por fila

#### `socios/form.html`
- Campos: nombre, descripción, imagen, whatsapp, orden
- Validación: todos obligatorios excepto orden

#### `componentes/lista.html`
- Cards: uno por componente
- Muestra: nombre, título, subtítulo, contenido (truncado)
- Botón "Editar" por card

#### `componentes/form.html`
- Campos: título, subtítulo, contenido, link, extra_data
- Guardado automático en tabla Componente

#### `usuarios/lista.html`
- Tabla: Usuario (avatar), Rol, Estado, Creado, Acciones
- Solo admin puede ver esta sección
- No permite eliminarse a sí mismo

#### `usuarios/form.html`
- Campos: username, password, rol, activo (solo editar)
- Username no editable en edición

#### `logs.html`
- Tabla: Fecha, Usuario, Acción, Componente, Detalle, IP
- Paginación (50 por página)
- Colores por tipo de acción

---

## 🗄️ Base de Datos

### Modelo Entidad-Relación

```
┌─────────────┐     ┌─────────────┐
│   Usuario   │     │     Log     │
├─────────────┤     ├─────────────┤
│ id (PK)    │────┐│ id (PK)    │
│ username   │    ││ usuario_id │──→ Usuario.id
│ password   │    ││ accion     │
│ rol        │    ││ componente │
│ activo     │    ││ detalle    │
│ created_at │    ││ ip_address │
└─────────────┘    ││ timestamp  │
                   │└─────────────┘
       ┌──────────┘
       │
┌──────┴──────────┐     ┌─────────────────┐
│     Socio       │     │   Componente    │
├─────────────────┤     ├─────────────────┤
│ id (PK)        │     │ id (PK)         │
│ nombre         │     │ nombre          │
│ descripcion    │     │ titulo          │
│ imagen         │     │ subtitulo       │
│ whatsapp       │     │ contenido       │
│ activo         │     │ link           │
│ orden          │     │ extra_data     │
│ created_at     │     │ updated_at     │
└─────────────────┘     └─────────────────┘
```

---

## 🎛️ Funcionalidades

### 📊 Dashboard
| Elemento | Fuente de datos | Descripción |
|----------|----------------|-------------|
| Socios | `Socio.query.count()` | Total de socios |
| Componentes | `Componente.query.count()` | Total de componentes |
| Usuarios | `Usuario.query.count()` | Total menos actual |
| Logs hoy | `Log.query.filter(date=hoy)` | Acciones del día |
| Actividad | `Log.query.limit(10)` | Últimos 10 logs |

### 👥 Socios (CRUD)
| Acción | Ruta | Función | Afecta |
|--------|------|---------|--------|
| Listar | GET `/socios` | `listar_socios()` | Tabla Socio |
| Crear | POST `/socios/nuevo` | `nuevo_socio()` | INSERT Socio |
| Editar | POST `/socios/editar/<id>` | `editar_socio()` | UPDATE Socio |
| Eliminar | POST `/socios/eliminar/<id>` | `eliminar_socio()` | DELETE Socio |
| Toggle | POST `/socios/toggle/<id>` | `toggle_socio()` | UPDATE Socio.activo |

**Afecta en E³ Frontend:**
- Si usas API: `/api/socios` → Carousel.astro
- Si usas datos estáticos: `carouselItems.ts`

### 🧩 Componentes (CRUD)
| Acción | Ruta | Función | Afecta |
|--------|------|---------|--------|
| Listar | GET `/componentes` | `listar_componentes()` | Tabla Componente |
| Editar | POST `/componentes/editar/<id>` | `editar_componente()` | UPDATE Componente |

**Componentes editables:**
| Nombre | Campos editables | Afecta en E³ |
|--------|------------------|---------------|
| Hero | titulo, subtitulo, contenido, link, extra_data | Hero.astro |
| Features | titulo, contenido | Features.astro |
| AboutUs | titulo, contenido, extra_data (JSON) | AboutUs.astro |
| MisionVision | titulo, contenido, extra_data (JSON) | MisionVision.astro |
| CTA | titulo, contenido, link, extra_data | CTA.astro |
| Contact | titulo, contenido, link, extra_data (JSON) | Contact.astro |

### Estructura de `extra_data` por componente

**AboutUs (`extra_data`):**
```json
{
  "subtituloSeccion": "Solidez Económica y Estrategia Política",
  "descripcion1": "Texto de descripción 1",
  "descripcion2": "Texto de descripción 2",
  "valor1": "Precisión en el análisis económico",
  "valor2": "Integridad en la acción estratégica",
  "valor3": "Solidez estructural garantizada",
  "valor4": "Resiliencia ante cualquier crisis",
  "valor5": "Ética como pilar fundamental",
  "lema": "Cita destacada"
}
```

**MisionVision (`extra_data`):**
```json
{
  "mision": "Texto de la misión",
  "vision": "Texto de la visión",
  "lema": "Lema principal",
  "lemaAdicional": "Descripción adicional",
  "lemaFinal": "Cierre con cita"
}
```

**Contact (`extra_data`):**
```json
{
  "email": "correo@ejemplo.com",
  "telefono": "+52 000 000-0000",
  "ubicacion": "Culiacan, Sinaloa"
}
```

**Hero (`extra_data`):**
Texto del botón CTA (ej: "¿Te Interesa Alguno de Nuestros Servicios?")

**CTA (`extra_data`):**
Texto del botón (ej: "Comienza a Construir Ahora")

### 👤 Usuarios (CRUD)
| Acción | Ruta | Función | Afecta |
|--------|------|---------|--------|
| Listar | GET `/usuarios` | `listar_usuarios()` | Tabla Usuario |
| Crear | POST `/usuarios/nuevo` | `nuevo_usuario()` | INSERT Usuario |
| Editar | POST `/usuarios/editar/<id>` | `editar_usuario()` | UPDATE Usuario |
| Eliminar | POST `/usuarios/eliminar/<id>` | `eliminar_usuario()` | DELETE Usuario |

### 📋 Logs
| Acción | Registra | Campos |
|--------|---------|--------|
| LOGIN | `log_accion('LOGIN')` | usuario, IP |
| LOGOUT | `log_accion('LOGOUT')` | usuario, IP |
| CREAR | `log_accion('CREAR', componente, detalle)` | quién, qué |
| EDITAR | `log_accion('EDITAR', componente, detalle)` | quién, qué |
| ELIMINAR | `log_accion('ELIMINAR', componente, detalle)` | quién, qué |
| TOGGLE | `log_accion('TOGGLE', componente, detalle)` | quién, qué |

---

## 🔌 API REST

### Endpoints Públicos

| Endpoint | Método | Respuesta | Afecta en E³ |
|----------|--------|-----------|---------------|
| `/api/socios` | GET | `[{"id", "title", "description", "image", "contact": {"text", "link"}}]` | Carousel.astro |
| `/api/componentes` | GET | `[{"nombre", "titulo", "subtitulo", "contenido", "link"}]` | Todos |

### Estructura de Respuesta `/api/socios`

```json
{
  "id": 1,
  "title": "Nombre del Asesor",
  "description": "Biografía o perfil del asesor",
  "image": "https://ejemplo.com/imagen.jpg",
  "contact": {
    "text": "Contactar por WhatsApp",
    "link": "https://wa.me/521234567890"
  }
}
```

### Ejemplo de uso
```javascript
// En E³ (Features.astro)
const response = await fetch('http://localhost:5000/api/socios');
const socios = await response.json();

// socios tiene la estructura:
// [{ id, title, description, image, contact: { text, link } }]

// Renderizar en Carousel.astro
```

### Verificar que la API funciona

```bash
# Desde terminal
curl http://localhost:5000/api/socios

# Resultado esperado:
# [{"id":1,"title":"Nombre","description":"Desc","image":"url","contact":{"text":"...","link":"..."}}]
```

---

## 🔒 Seguridad

### Contraseñas
- `werkzeug.security.generate_password_hash()` → pbkdf2:sha256
- `werkzeug.security.check_password_hash()` → verificación

### Sesiones
- `Flask session` con SECRET_KEY
- Timeout: al cerrar navegador
- Cookie: `session` (firmada)

### Roles
| Permiso | Admin | Editor |
|---------|-------|--------|
| Dashboard | ✅ | ✅ |
| Socios CRUD | ✅ | ✅ |
| Componentes CRUD | ✅ | ✅ |
| Usuarios CRUD | ✅ | ❌ |
| Ver Logs | ✅ | ✅ |

---

## 📦 Dependencias

| Paquete | Versión | Uso |
|---------|---------|-----|
| Flask | 3.0.0 | Framework web |
| Flask-SQLAlchemy | 3.1.1 | ORM base de datos |
| Werkzeug | 3.0.1 | Seguridad contraseñas |

---

## 🛠️ Comandos Útiles

```bash
# Iniciar servidor
python app.py

# Reiniciar base de datos
del e3_admin.db
python app.py

# Ver logs en consola
python app.py 2>&1 | tee app.log

# Con Gunicorn (producción)
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 🎨 Paleta de Colores

### 📁 Archivo Principal de Colores

**`templates/base.html`** (Líneas 9-13, 20-22)

Los estilos del panel admin usan **Tailwind CSS v2.2** y están definidos de forma **inline** en la plantilla base.

### Guía para Cambiar Colores

#### 🟢 Colores del Sidebar

| Elemento | Clase Tailwind | Valor Hex | Línea |
|----------|----------------|-----------|-------|
| Fondo sidebar | `bg-slate-950` | `#020617` | 20 |
| Borde separador | `border-gold-500` | `#ca8a04` | 21 |
| Título logo | `text-gold-400` | `#eab308` | 22 |
| Link activo/hover bg | inline | `#eab308` | 11-12 |
| Link activo/hover texto | inline | `#050d17` | 11-12 |

#### 🔵 Cambiar Fondo del Sidebar
```html
<!-- Línea 20 -->
<aside class="w-64 bg-slate-950 text-white flex flex-col">
<!-- Cambiar bg-slate-950 por cualquier color Tailwind -->
<aside class="w-64 bg-navy-900 text-white flex flex-col">
```

#### 🟡 Cambiar Color de Acento (Gold)

| Ubicación | Línea | Color actual |
|-----------|-------|--------------|
| Borde logo | 21 | `border-gold-500` (#ca8a04) |
| Título logo | 22 | `text-gold-400` (#eab308) |
| Link activo/hover | 11-12 | `#eab308` |
| Avatar usuario | 73 | `bg-gold-500` (#ca8a04) |
| Link logout hover | 78 | `text-gold-400` (#eab308) |

**Para cambiar todos los acentos gold:**
```html
<!-- Buscar y reemplazar en base.html -->
gold-400 → gold-300 (más claro)
gold-500 → gold-600 (más oscuro)
```

#### ⚪ Colores de Botones y Estados

| Elemento | Clase Tailwind | Valor Hex | Archivo |
|----------|----------------|-----------|---------|
| Botón primario | `bg-blue-600` | - | Componentes/lista.html |
| Botón éxito | `bg-green-600` | - | Componentes/lista.html |
| Botón peligro | `bg-red-600` | - | Componentes/lista.html |
| Hover botón | `hover:bg-blue-700` | - | Componentes/lista.html |

### ✏️ Cómo Cambiar un Color

1. **Abrir** `templates/base.html`
2. **Buscar** la clase de color que quieres cambiar
3. **Reemplazar** por otra clase Tailwind
4. **Guardar** - recargar la página

**Ejemplo - Cambiar sidebar a navy oscuro:**
```html
<!-- Antes (línea 20) -->
<aside class="w-64 bg-slate-950 text-white flex flex-col">

<!-- Después -->
<aside class="w-64 bg-navy-900 text-white flex flex-col">
```

**Ejemplo - Cambiar acentos a azul:**
```html
<!-- Antes -->
<aside class="w-64 bg-slate-950 text-white flex flex-col">
<div class="p-6 border-b border-gold-500">

<!-- Después -->
<aside class="w-64 bg-slate-950 text-white flex flex-col">
<div class="p-6 border-b border-blue-500">
```

### 📁 Archivos con Estilos Inline Adicionales

| Archivo | Descripción |
|---------|-------------|
| `componentes/lista.html` | Botones CRUD con colores inline |
| `componentes/form.html` | Inputs y labels |
| `socios/lista.html` | Tabla con colores de estado |
| `usuarios/lista.html` | Badges de roles |

---

## 🔧 Configuración

| Elemento | Archivo | Línea | Cambiar a |
|----------|---------|-------|-----------|
| Puerto | app.py | 207 | `port=5001` |
| SECRET_KEY | app.py | 7 | `'tu-clave-unica'` |
| DB URI | app.py | 8 | `'sqlite:///otro.db'` |

---

## 📱 Integración con E³

```
┌─────────────────┐         ┌─────────────────┐
│     E3_Admin    │  API   │       E³        │
│                 │ ────── │   (Frontend)    │
│  Puerto: 5000   │        │   Puerto: 4321  │
│                 │        │                 │
│  Gestiona:      │        │  Muestra:       │
│  - Socios       │ ────── │  - Carousel     │
│  - Componentes  │        │  - Textos       │
│  - Usuarios     │        │                 │
│  - Logs         │        │                 │
└─────────────────┘        └─────────────────┘
```

### Flujo de datos

1. Admin crea/edita socio → `Socio` tabla en SQLite
2. E³ (en dev/build) hace GET a `http://localhost:5000/api/socios`
3. Los datos se renderizan en el Carousel de E³

### Requisitos

| Condición | Resultado |
|-----------|-----------|
| E3_Admin corriendo + E³ dev | ✅ Datos dinámicos en tiempo real |
| E3_Admin corriendo + E³ build | ✅ Datos "incrustados" en HTML |
| E3_Admin apagado + E³ dev | ⚠️ Muestra datos de respaldo |
| E3_Admin apagado + E³ prod | ✅ Funciona (datos ya embebidos) |

> Para datos **siempre dinámicos** en producción, E³ debe usar [modo SSR](#-api-rest).

---

## ❓ Solución de Problemas

| Problema | Solución |
|----------|----------|
| "Module not found" | `pip install -r requirements.txt` |
| Base corrupta | `del e3_admin.db` + reiniciar |
| Login falla | Verificar cookies del navegador |
| API no responde | Verificar servidor corriendo |
| No ve cambios | Limpiar cache navegador |

---

---

## ☁️ Deploy en Render

### Requisitos Previos

- Cuenta en [Render.com](https://render.com) vinculada a GitHub
- Código subido en rama `api` del repositorio

### Archivos de Configuración

El proyecto ya incluye los archivos necesarios:

| Archivo | Contenido |
|---------|-----------|
| `runtime.txt` | `python-3.11.0` |
| `Procfile` | `web: gunicorn app:app --bind 0.0.0.0:$PORT` |
| `requirements.txt` | Flask + gunicorn |

### Pasos para Deploy

1. **Crear Web Service en Render:**
   - Ir a https://dashboard.render.com
   - Click **New → Web Service**
   - Conectar repositorio `joseramon95/mis-pruebas`
   - Branch: `api`
   - Build Command: (vacío)
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - Click **Create Web Service**

2. **Esperar Deploy:**
   - Render instalará dependencias automáticamente
   - Dará una URL como: `https://tu-app.onrender.com`

3. **Verificar Endpoints:**
   ```
   https://tu-app.onrender.com/api/socios
   https://tu-app.onrender.com/api/componentes
   ```

### Configurar E³ Frontend

Crear archivo `.env` en la raíz de E³:
```bash
PUBLIC_API_URL=https://tu-app.onrender.com
```

Luego hacer rebuild de E³:
```bash
vercel --prod --yes
```

### Free Tier Limitaciones

- **El servicio duerme** después de 15 min de inactividad
- Se activa automáticamente con el primer request
- Tiempo de activación: ~10-30 segundos
- Si necesitas uptime constante, usar plan de pago

---

## 📝 Licencia

Proyecto privado para E³ Consultoría.
