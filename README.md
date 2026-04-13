# E³ - Consultora Estratégica

Sitio web oficial de E³ Consultoría: Soluciones estratégicas de alta complejidad para transformar la incertidumbre en crecimiento.

## 🚀 Inicio Rápido

```bash
# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev

# Construir para producción
npm run build

# Previsualizar versión de producción
npm run preview
```

## 📁 Estructura del Proyecto

```
E_3/
├── public/
│   ├── e3.ico              # Logo favicon
│   ├── e3-background.png   # Imagen de fondo principal
│   ├── persona.png         # Imágenes de personal
│   └── persona-no-bg.png
├── src/
│   ├── components/         # Componentes reutilizables
│   ├── data/              # Archivos de datos
│   ├── layouts/           # Plantillas base
│   ├── pages/             # Rutas/páginas
│   └── styles/            # Estilos globales
├── package.json
└── README.md
```

## 🗺️ Mapa de Componentes y Dependencias

```
┌─────────────────────────────────────────────────────────────────────┐
│                         index.astro (Página Principal)                │
│                                                                     │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌────────────────────┐   │
│  │ Header  │  │  Hero   │  │Carousel │  │     Features        │   │
│  │         │  │         │  │         │  │  (usa Carousel)    │   │
│  │ Nav     │  │ Titulo  │  │ Items   │  │                    │   │
│  │ Links   │  │ Botón   │  │ Nav     │  │                    │   │
│  └─────────┘  └─────────┘  └─────────┘  └────────────────────┘   │
│                                                                     │
│  ┌─────────┐  ┌─────────────┐  ┌─────────┐  ┌────────────────┐   │
│  │AboutUs  │  │  Mision    │  │  CTA    │  │    Contact     │   │
│  │         │  │  Vision    │  │         │  │                │   │
│  │ Valores │  │            │  │WhatsApp │  │  Formulario    │   │
│  └─────────┘  └─────────────┘  └─────────┘  └────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                         Footer                              │    │
│  └─────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

## 🧩 Componentes y sus Funciones

### 📋 `Header.astro` - Navegación
| Elemento | Tipo | Descripción |
|----------|------|-------------|
| Logo E³ | Link | Vincula a `/` |
| Nav "Quiénes Somos" | Anchor | `#quienes-somos` |
| Nav "Misión y Visión" | Anchor | `#mision-vision` |
| Nav "Soluciones" | Anchor | `#soluciones` |
| Nav "Contacto" | Anchor | `#contacto` |
| Botón "Cotiza" | Link | `/cotizaciones` (nueva pestaña) |
| Menú móvil | Toggle | JavaScript inline |

---

### 📋 `Hero.astro` - Sección Principal
| Elemento | Descripción |
|----------|-------------|
| Título "Nosotros Resolvemos" | Texto estático |
| Subtítulo "Tus Problemas" | Texto estático |
| Descripción | Texto de valor |
| Botón "¿Te Interesa...?" | Link a `/cotizaciones` |
| Fondo | Usa `backgroundImages.ts` → `hero` |

**Dependencias:**
- `src/data/backgroundImages.ts` → configuración de fondo

---

### 📋 `Carousel.astro` - Carrusel de Socios
| Elemento | Tipo | Descripción |
|----------|------|-------------|
| Título | Prop | "La Arquitectura de la Certeza..." |
| Descripción | Prop | Texto introductorio |
| Cards de socios | Loop | Itera sobre `carouselItems.ts` |
| Imagen asesor | Dinámico | URL de `carouselItems` |
| Nombre | Dinámico | `carouselItems.title` |
| Descripción | Dinámico | `carouselItems.description` |
| Botón WhatsApp | Dinámico | `carouselItems.contact.link` |
| Navegación prev/next | JS | Flechas izquierda/derecha |
| Indicadores | JS | Puntos de navegación |
| Auto-rotación | JS | Cada 5 segundos |

**Dependencias:**
- `src/data/carouselItems.ts` → datos de asesores
- `src/data/backgroundImages.ts` → fondo del carrusel
- JavaScript (clase CarouselController)

---

### 📋 `Features.astro` - Características
| Elemento | Descripción |
|----------|-------------|
| Wrapper | Envuelve Carousel.astro |
| Props título | Obtiene del API (`componente.titulo`) |
| Props descripción | Obtiene del API (`componente.contenido`) |

**Dependencias:**
- `Carousel.astro` → reutilización
- `/api/componentes` (nombre: `Features`)
- `/api/socios` → datos del carrusel

---

### 📋 `AboutUs.astro` - Quiénes Somos
| Elemento | Descripción |
|----------|-------------|
| Título | "Quiénes Somos" |
| Texto principal | Descripción de E³ |
| Card de valores | Gradient navy→gold |
| Lista de valores | 5 valores fundacionales |
| Lema | Cita destacada |

---

### 📋 `MisionVision.astro` - Misión y Visión
| Elemento | Descripción |
|----------|-------------|
| Título | "Misión y Visión" |
| Card Misión | Borde izquierdo navy |
| Card Visión | Borde izquierdo gold |
| Lema principal | Cita destacada con borde gold |
| Sección Pilares | 3 columnas con iconos |

---

### 📋 `CTA.astro` - Llamada a la Acción
| Elemento | Descripción |
|----------|-------------|
| Título | "Listo Para Construir..." |
| Descripción | "Comienza a construir..." |
| Botón WhatsApp | Link hardcodeado `wa.me/526677800166` |
| Fondo | Usa `backgroundImages.ts` → `cta` |

**Dependencias:**
- `src/data/backgroundImages.ts` → fondo CTA

---

### 📋 `Contact.astro` - Formulario de Contacto
| Elemento | Tipo | Descripción |
|----------|------|-------------|
| Campos | Form | Nombre, Email, Teléfono, Asunto, Mensaje |
| Integración | Formspree | `https://formspree.io/f/YOUR_FORMSPREE_ID` |
| Botón enviar | Submit | Navega a Formspree |
| Info contacto | Estático | Email, Tel, Ubicación |

---

### 📋 `Cotizaciones.astro` - Página Cotizaciones
| Elemento | Tipo | Descripción |
|----------|------|-------------|
| Título | Estático | "¿Te Interesa Alguno...?" |
| Campos | Form | Nombre, Email, Tel, Empresa, Servicio, Descripción |
| Dropdown servicios | Select | 5 opciones |
| Integración | Formspree | Envío por fetch |
| Mensaje éxito | Hidden | "En breve uno de nuestros..." |
| Fondo | - | Usa `backgroundImages.ts` → `hero` |

**Dependencias:**
- `src/data/backgroundImages.ts` → fondo
- JavaScript → fetch y toggle mensaje

---

### 📋 `Footer.astro` - Pie de Página
| Elemento | Descripción |
|----------|-------------|
| Logo | Link a `/` |
| Links Empresa | Anchor links |
| Links Legal | Links a páginas |
| Redes sociales | Twitter, GitHub, LinkedIn |
| Copyright | "© 2026 E³ Consultoría" |

---

## 📊 Archivos de Datos

### `src/data/componentes.ts`
```typescript
// Afecta: Todos los componentes editables
// Función: Obtener datos editables desde E3_Admin API

interface Componente {
  nombre: string;
  titulo: string;
  subtitulo: string;
  contenido: string;
  link: string;
  extra_data: string; // JSON con datos adicionales específicos por componente
}
```

### `src/data/carouselItems.ts`
```typescript
// Afecta: Carousel.astro
// Nota: Ahora se obtiene dinámicamente del API /api/socios

interface CarouselItem {
  id: number;
  title: string;        // nombre del asesor
  description: string; // bio/perfil
  image: string;        // URL de imagen
  contact: {
    text: string;       // Texto del botón WhatsApp
    link: string;       // URL de WhatsApp
  };
}
```

---

### `src/data/backgroundImages.ts`
```typescript
// Afecta: Hero.astro, Carousel.astro, CTA.astro
// Función: Configurar fondos de cada sección

// Secciones:
// - hero: Sección principal (Hero, Cotizaciones)
// - carousel: Sección del carrusel
// - cta: Sección de llamada a la acción

interface BackgroundConfig {
  section: string;
  imageUrl: string;        // URL de imagen
  gradientOverlay: string;  // Gradiente CSS overlay
}
```

---

## 🎨 Paleta de Colores

### 📁 Archivo Principal de Colores

**`src/styles/global.css`** (Líneas 3-24)

Define todos los colores personalizados navy y gold del tema usando Tailwind CSS v4.

### Guía para Cambiar Colores

#### 🔵 Serie Navy (Colores oscuros/principales)
| Clase Tailwind | Valor Hex | Usado en |
|----------------|-----------|----------|
| `navy-50` | `#e6e9ef` | Fondos claros, textos claros sobre oscuro |
| `navy-100` | `#c0c7d4` | Bordes claros, sombras |
| `navy-200` | `#96a2b7` | Textos secundarios claros |
| `navy-300` | `#6c7d9a` | Iconos sobre fondos claros |
| `navy-400` | `#4a5f7f` | Iconos principales |
| `navy-500` | `#2a4065` | Elementos decorativos |
| `navy-600` | `#1e3352` | Hover states |
| `navy-700` | `#152640` | Secciones secundarias |
| `navy-800` | `#0d1b2e` | **Sidebar, Header, fondos principales** |
| `navy-900` | `#050d17` | **Fondos oscuros, CTA, Footer** |

#### 🟡 Serie Gold (Colores de acento)
| Clase Tailwind | Valor Hex | Usado en |
|----------------|-----------|----------|
| `gold-50` | `#fffbeb` | Fondos muy claros |
| `gold-100` | `#fef3c7` | Hover de elementos claros |
| `gold-200` | `#fde68a` | Destacados suaves |
| `gold-300` | `#fcd34d` | Hover de botones |
| `gold-400` | `#eab308` | **Bordes de cards, elementos activos, links** |
| `gold-500` | `#ca8a04` | **Iconos, textos destacados, botones principales** |
| `gold-600` | `#a16207` | Botones hover |
| `gold-700` | `#854d0e` | Textos importantes |
| `gold-800` | `#713f12` | Textos oscuros sobre claro |
| `gold-900` | `#5c3409` | Textos muy oscuros |

### 🧩 Componentes por Color Principal

| Color | Valor | Componentes |
|-------|-------|-------------|
| Navy 800 | `#0d1b2e` | Header, Hero, AboutUs, MisionVision, CTA, Contact, Footer |
| Navy 900 | `#050d17` | Hero, CTA, Footer, Sidebar Admin |
| Gold 400 | `#eab308` | Bordes de cards, elementos activos |
| Gold 500 | `#ca8a04` | Iconos, acentos, botón avatar |

### ✏️ Cómo Cambiar un Color

1. **Abrir** `src/styles/global.css`
2. **Buscar** la línea del color que quieres cambiar (ej: `--color-navy-800`)
3. **Modificar** el valor hex
4. **Guardar** - los cambios se aplican automáticamente en desarrollo

**Ejemplo - Cambiar el color navy principal:**
```css
/* Antes */
--color-navy-800: #0d1b2e;

/* Después (ejemplo: azul más claro) */
--color-navy-800: #1a365d;
```

### 📱 Colores en Fondos de Secciones

Los fondos de las secciones (Hero, CTA, etc.) se configuran en:
- **Archivo:** `src/data/backgroundImages.ts`
- **Propiedad:** `gradientOverlay` - Define el gradiente que cubre la imagen de fondo

---

## 📄 Páginas

### `src/pages/index.astro`
```astro
Orden de componentes:
1. Header.astro
2. Hero.astro
3. Features.astro        → usa Carousel.astro
4. AboutUs.astro
5. MisionVision.astro
6. CTA.astro
7. Contact.astro
8. Footer.astro
```

### `src/pages/cotizaciones.astro`
```astro
Orden de componentes:
1. Header.astro
2. Cotizaciones.astro
3. Footer.astro
```

---

## 🔗 Integración con E3_Admin

### Requisitos de Ejecución

| Modo | E3_Admin debe estar corriendo |
|------|-------------------------------|
| `npm run dev` | ✅ Sí, hace fetch en tiempo real |
| `npm run build` | ✅ Sí, pero solo durante el build |
| Producción (sitio estático) | ❌ No, los datos ya están "incrustados" en el HTML |

> **Nota:** Los datos del carrusel se obtienen de `http://localhost:5000/api/socios` al momento del build. Si E3_Admin no está disponible durante el build, se mostrarán datos de respaldo.

### Variable de Entorno

```bash
# Crear archivo .env en la raíz de E_3
PUBLIC_API_URL=http://localhost:5000
```

### Modo Estático vs SSR

El proyecto usa **build estático** por defecto. Los datos del carrusel se incrustan en el HTML durante la compilación.

**Para datos dinámicos en producción**, se requiere cambiar a **SSR**:

```bash
# Instalar adapter
npx astro add node

# En astro.config.mjs:
import node from '@astrojs/node';

export default defineConfig({
  output: 'server',
  adapter: node({ mode: 'standalone' }),
  vite: {
    plugins: [tailwindcss()]
  }
});
```

Con SSR, E3_Admin debe estar corriendo siempre para servir los datos actualizados.

### Endpoints de API
| Endpoint | Método | Respuesta | Afecta en Frontend |
|----------|--------|-----------|-------------------|
| `GET /api/socios` | Lista socios activos | `[{id, title, description, image, contact: {text, link}}]` | Carousel.astro |
| `GET /api/componentes` | Todos componentes | `[{nombre, titulo, subtitulo, contenido, link}]` | Todos |

### Estructura del API `/api/socios`

```json
[
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
]
```

### Cómo se obtienen los datos

En `Features.astro`:
```astro
const response = await fetch(`${API_URL}/api/socios`);
const items = await response.json();
```

Los datos se pasan al componente `Carousel.astro` como prop `items`.

---

## 📦 Dependencias

| Paquete | Versión | Componentes que usa |
|---------|---------|---------------------|
| astro | ^6.0.8 | Todos |
| tailwindcss | ^4.2.2 | Todos |
| @tailwindcss/vite | ^4.2.2 | Compilación CSS |

---

## 🌐 Scripts Disponibles

| Comando | Descripción | E3_Admin requerido |
|---------|-------------|-------------------|
| `npm run dev` | Servidor desarrollo localhost:4321 | ✅ Sí |
| `npm run build` | Construir `./dist/` | ✅ Sí |
| `npm run preview` | Previsualizar producción | ❌ No |

> **Durante desarrollo y build:** E3_Admin debe estar corriendo en `http://localhost:5000` para obtener los datos del carrusel.

---

## 📝 Configuración Manual

| Elemento | Archivo | Línea | Cambiar |
|----------|---------|-------|---------|
| Formspree Cotizaciones | `Cotizaciones.astro` | 15 | `YOUR_FORMSPREE_ID` |
| Formspree Contacto | `Contact.astro` | 14 | `YOUR_FORMSPREE_ID` |
| WhatsApp CTA | `CTA.astro` | 35 | Número teléfono |
| Colores tema | `global.css` | 3-26 | Valores hex |
| Fondos secciones | `backgroundImages.ts` | 8-24 | URLs y gradientes |

---

## 🚀 Despliegue en Vercel

### Flujo de Trabajo

Este proyecto usa **2 ramas**:
- `main` → Rama de desarrollo (ignorar builds)
- `astro` → Rama de producción (despliegue real)

### Configuración Inicial

#### 1. Configurar Vercel (primera vez)

1. Ir a [vercel.com/dashboard](https://vercel.com/dashboard)
2. Importar el repositorio desde GitHub
3. Framework: **Astro**
4. Root Directory: `./E_3` (o la carpeta del proyecto)
5. Build Command: `npm run build`
6. Deploy

#### 2. Ignorar Builds de `main`

Para que push a `main` no dispare builds:

1. Ir al proyecto en Vercel
2. **Settings** → **Build & Development Settings**
3. Buscar **Ignore Build Step**
4. Seleccionar **"Run my bash script"**
5. Pegar:
   ```bash
   echo "Ignoring build" && exit 0
   ```
6. **Save**

#### 3. Crear Deploy Hook para `astro`

1. Ir al proyecto en Vercel
2. **Settings** → **Git**
3. **Deploy Hooks**
4. Nombre: `Deploy Astro`
5. Branch: `astro`
6. **Create Hook**
7. Copiar la URL del hook

#### 4. Configurar GitHub Actions (opcional)

Crear `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches:
      - astro

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

### Comandos de Deploy

#### Desde Terminal (CLI de Vercel)

```bash
# Deploy preview
vercel

# Deploy a producción
vercel --prod

# Ver proyectos
vercel projects

# Ver deployments
vercel ls
```

#### Con Deploy Hook (desde cualquier servicio)

```bash
# Trigger deploy de astro
curl -X POST "URL_DEL_DEPLOY_HOOK"
```

### Deploy Manual Paso a Paso

#### Opción 1: Terminal

```bash
# 1. Asegurarse de estar en la rama correcta
git checkout astro

# 2. Hacer cambios y commit
git add .
git commit -m "tu mensaje"

# 3. Push a GitHub
git push origin astro

# 4. Opcional: deploy inmediato con CLI
vercel --prod
```

#### Opción 2: Solo GitHub

```bash
# 1. Hacer cambios y commit
git add .
git commit -m "tu mensaje"

# 2. Push a astro
git push origin astro

# 3. GitHub Actions triggered automáticamente → deploy a producción
```

#### Opción 3: Deploy Hook (desde CMS o externo)

```bash
# Cuando el CMS actualiza contenido
curl -X POST "https://api.vercel.com/v1/integrations/deploy/HOOK_ID"
```

### Resumen de Ramas

| Rama | Acción | Resultado |
|------|--------|-----------|
| `main` | Push | Solo preview (ignora build) |
| `astro` | Push | Deploy a producción |
| `astro` | Deploy hook | Deploy a producción |

### Enlaces

- **Dashboard:** [vercel.com/dashboard](https://vercel.com/dashboard)
- **Proyecto:** [vercel.com/e-e-e1/mis-pruebas](https://vercel.com/e-e-e1/mis-pruebas)
- **Producción:** https://mis-pruebas.vercel.app

---

---

## 📋 Requisitos del Sistema

- **Node.js** >= 22.12.0
- **npm** o **yarn**

---

## 🧩 Componentes de Soluciones (Nuevos)

### 📋 `SolucionesBanner.astro` - Banner de Casos de Éxito
| Elemento | Descripción |
|----------|-------------|
| Título | "Casos de Éxito" (configurable) |
| Subtítulo | Descripción del banner (configurable) |
| Imagen fondo | URL configurable con overlay |
| Grid preview | 4 mini-cards con imágenes |
| Botón CTA | Enlace a `/soluciones` |

**Props:**
```typescript
interface Props {
    titulo?: string;      // default: 'Casos de Éxito'
    subtitulo?: string;   // default: texto descriptivo
    imagen?: string;      // URL de imagen de fondo
}
```

---

### 📋 `Soluciones.astro` - Grid de Casos de Éxito
| Elemento | Descripción |
|----------|-------------|
| Título | Título de la sección |
| Subtítulo | Descripción de la sección |
| Cards casos | Grid de casos con efecto neon gold |
| Imagen | Thumbnail del caso |
| Testimonio | Quote con borde gold (opcional) |
| Botón | Enlace a `/soluciones/[slug]` |

**Props:**
```typescript
interface Props {
    casos: CasoExito[];
    titulo: string;
    subtitulo: string;
}
```

**Estilos especiales:**
- Borde exterior: gradiente gold
- Efecto neon: `box-shadow` con tonos gold
- Hover: intensifica el glow y eleva

---

## 📁 Archivos de Datos - Soluciones

### `src/data/soluciones.ts`

```typescript
export interface CasoExito {
    id: number;
    slug: string;
    titulo: string;
    descripcion: string;
    imagen: string;
    testimonio: {
        autor: string;
        cargo: string;
        texto: string;
    } | null;
}

export interface SolucionesData {
    titulo: string;
    subtitulo: string;
    casos: CasoExito[];
}

export interface CasoDetalle extends CasoExito {
    contenido: string;
    resultados: string[];
}
```

---

## 📄 Páginas de Soluciones

### `src/pages/soluciones.astro` - Página Principal
```
Orden de componentes:
1. Header.astro
2. Soluciones.astro (carga datos via JS fetch)
3. CTA.astro
4. Footer.astro
```

**Funcionalidad:**
- Carga datos del API `${API_URL}/api/contenido/soluciones`
- Renderiza cards con efecto glass/blur
- Muestra testimonios si existen
- Fallback a datos locales si API no disponible

**API URL:**
- Desarrollo: `http://localhost:5000`
- Producción: `https://e3-admin-api.onrender.com`

---

### `src/pages/soluciones/[slug].astro` - Detalle de Caso
```
Orden de componentes:
1. Header.astro
2. Artículo (contenido del caso)
3. CTA.astro
4. Footer.astro
```

**Funcionalidad:**
- Genera páginas dinámicas basadas en slugs
- Obtiene datos del API `${API_URL}/api/contenido/soluciones/${slug}`
- Muestra: imagen, título, descripción, contenido, resultados, testimonio
- Timeout de 30 segundos para fallback
- Botón "Volver a Soluciones"
- CTA final para cotizaciones

**API Endpoint:**
- `GET /api/contenido/soluciones/[slug]`

---

## 📝 Sistema de Logging

### `src/utils/logger.ts`
```typescript
// Funciones exportadas:

logAction(action: string, details: Record<string, unknown>): Promise<void>
// Registra una acción en logs/[fecha].log

createRequestLogger(): Function
// Crea middleware para logging de requests
```

**Ubicación de logs:**
- Desarrollo: `./logs/[fecha].log`
- Vercel: `/tmp/logs/[fecha].log`

**Formato:**
```
[2024-01-15T10:30:00.000Z] VISIT | {"ip":"192.168.1.1","method":"GET","path":"/","userAgent":"..."}
```

---

### `src/middleware.ts` - Middleware de Visitas
```typescript
// Registra cada visita automáticamente
// Captura: IP, método, path, user-agent
// Usa logAction() del utils/logger
```

---

### `src/pages/api/log.ts` - API de Logging
```
POST /api/log

Body:
{
    "action": "CLICK" | "FORM_SUBMIT" | etc,
    ...details
}

Respuesta: { "success": true } | { "error": "Invalid request" }
```

**Uso desde frontend:**
```javascript
fetch('/api/log', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        action: 'CTA_CLICK',
        element: 'ver-casos-button'
    })
});
```

---

## 🗺️ Mapa de Dependencias Actualizado

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         index.astro (Página Principal)                  │
│                                                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌────────────────────┐        │
│  │ Header  │  │  Hero   │  │Carousel │  │     Features        │        │
│  └─────────┘  └─────────┘  └─────────┘  └────────────────────┘        │
│                                                                         │
│  ┌─────────┐  ┌─────────────────────┐  ┌──────────────────────────┐     │
│  │AboutUs  │  │   MisionVision      │  │   SolucionesBanner       │     │
│  └─────────┘  └─────────────────────┘  └──────────────────────────┘     │
│                                                                         │
│  ┌─────────┐  ┌─────────────┐  ┌─────────┐  ┌────────────────┐       │
│  │  CTA    │  │  Contact     │  │ Footer  │  │                  │       │
│  └─────────┘  └─────────────┘  └─────────┘  └────────────────┘       │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                    soluciones.astro (Página Casos de Éxito)             │
│                                                                         │
│  ┌─────────┐  ┌─────────────────────┐  ┌─────────┐  ┌─────────┐       │
│  │ Header  │  │     Soluciones      │  │   CTA   │  │ Footer  │       │
│  │         │  │  (fetch API datos)   │  │         │  │         │       │
│  └─────────┘  └─────────────────────┘  └─────────┘  └─────────┘       │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│               soluciones/[slug].astro (Detalle de Caso)                 │
│                                                                         │
│  ┌─────────┐  ┌─────────────────────────────┐  ┌─────────┐  ┌────────┐ │
│  │ Header  │  │   Artículo (contenido)      │  │   CTA   │  │ Footer │ │
│  │         │  │   - imagen                  │  │         │  │        │ │
│  │         │  │   - titulo/descripcion       │  └─────────┘  └────────┘ │
│  │         │  │   - contenido                │                          │
│  │         │  │   - resultados               │                          │
│  │         │  │   - testimonio (opcional)    │                          │
│  └─────────┘  └─────────────────────────────┘                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔗 API Endpoints Completos

| Endpoint | Método | Descripción | Afecta |
|----------|--------|-------------|--------|
| `GET /api/socios` | Lista | Socios activos | Carousel.astro |
| `GET /api/componentes` | Lista | Textos editables | Todos |
| `GET /api/contenido/soluciones` | Lista | Casos de éxito | Soluciones.astro |
| `GET /api/contenido/soluciones/[slug]` | Detalle | Un caso | soluciones/[slug].astro |
| `POST /api/log` | Log | Registrar acciones | Sistema |

---

## 👥 Panel de Administración

Ver [E3_Admin](../E3_Admin/README.md) para:
- CRUD Socios → `carouselItems.ts` o API
- CRUD Casos de Éxito → Soluciones
- Editar textos → componentes
- Gestionar usuarios admin

---

## 📝 Licencia

Proyecto privado para E³ Consultoría.
