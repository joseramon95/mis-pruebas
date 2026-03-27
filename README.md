# Portafolio Profesional - José Ramón Madrid Valdez

![Status](https://img.shields.io/badge/status-Activo-brightgreen)
![Last Update](https://img.shields.io/badge/last%20update-2025-blue)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

> Portafolio profesional de QA Engineer especializado en automatización de pruebas de software.

---

## Tabla de Contenidos

1. [Descripción General](#descripción-general)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Tecnologías Utilizadas](#tecnologías-utilizadas)
4. [Configuración](#configuración)
5. [Descripción de Secciones](#descripción-de-secciones)
6. [Formulario de Contacto](#formulario-de-contacto)
7. [Componentes JavaScript](#componentes-javascript)
8. [Personalización](#personalización)
9. [Despliegue](#despliegue)
10. [Mantenimiento](#mantenimiento)

---

## Descripción General

Este portafolio es un sitio web estático desarrollado para mostrar mi perfil profesional como QA Engineer. Utiliza tecnologías web estándar (HTML, CSS, JavaScript) sin dependencias de frameworks, lo que lo hace ligero, rápido y fácil de mantener.

### Características Principales

- ✅ Diseño responsivo (móvil, tablet, escritorio)
- ✅ Tema oscuro profesional
- ✅ Animaciones sutiles con CSS
- ✅ Navegación suave con scroll
- ✅ Formulario de contacto funcional
- ✅ Iconografía consistente con Font Awesome
- ✅ SEO optimizado
- ✅ Accesibilidad mejorada

---

## Estructura del Proyecto

```
mis-pruebas/
├── index.html              # Página principal
├── style.css               # Estilos globales
├── package.json            # Dependencias (si las hay)
├── robots.txt              # Configuración para crawlers
├── sitemap.xml             # Mapa del sitio para SEO
├── README.md               # Este archivo
│
├── src/                    # Scripts JavaScript
│   ├── script_navbar.js    # Navegación y scroll
│   ├── script_tooltips.js  # Tooltips informativos
│   └── validación_formulario.js  # Validación de contacto
│
├── proyectos/              # Páginas de proyectos
│   ├── styles.css          # Estilos de proyectos
│   ├── tests_creados.html  # Suite de pruebas automatizadas
│   ├── proyecto_railways.html # Gestor de tareas Flask
│   ├── descargador_yt.html # API Testing Postman
│   └── prueba_gif.html     # (Archivo de prueba)
│
├── img/                    # Recursos imágenes
│   ├── jose ramon.png      # Foto de perfil
│   ├── icono.png           # Favicon
│   └── fondoportafolio.png # Imagen de fondo
│
└── docs/                   # Documentos
    ├── jose ramon madrid valdez cv.pdf
    └── jose ramon madrid valdez cover letter.pdf
```

---

## Tecnologías Utilizadas

### Frontend

| Tecnología | Propósito | Versión |
|------------|-----------|---------|
| HTML5 | Estructura semántica | - |
| CSS3 | Estilos y animaciones | - |
| JavaScript | Interactividad | ES6+ |
| Font Awesome | Iconografía | 6.5.1 |

### Fuentes Web

- **Inter**: Tipografía principal (sans-serif)
- **JetBrains Mono**: Código y elementos monospace

### CDNs Externos

```html
<!-- Font Awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

<!-- Google Fonts -->
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
```

### Servicios Externos

- **Formspree**: Gestión del formulario de contacto

---

## Configuración

### Requisitos Previos

- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- Editor de código (VS Code recomendado)
- Git para control de versiones

### Instalación Local

1. **Clonar el repositorio**
```bash
git clone https://github.com/joseramon95/mis-pruebas.git
cd mis-pruebas
```

2. **Abrir en navegador**
```bash
# Opción 1: Doble clic en index.html

# Opción 2: Usando servidor local
# Con Python
python -m http.server 8000

# Con Node.js
npx serve

# Con PHP
php -S localhost:8000
```

3. **Ver en el navegador**
```
http://localhost:8000
```

---

## Descripción de Secciones

### 1. Encabezado (Header)

**Ubicación:** `index.html` líneas 19-36

El header es sticky (fijo en la parte superior) y contiene:
- Logo con enlace al inicio
- Navegación principal con 6 secciones
- Menú hamburguesa para móvil

**Funcionamiento:**
- Se mantiene visible al hacer scroll
- Se reduce ligeramente su padding cuando se desplaza
- El menú se oculta/mostrar en dispositivos móviles

```html
<header class="contenedor-header">
    <div class="logo"><a href="#">JRMV</a></div>
    <nav id="nav">
        <ul>
            <li><a href="#sobremi">...</a></li>
            <!-- más enlaces -->
        </ul>
    </nav>
</header>
```

### 2. Sección Inicio (Hero)

**Ubicación:** `index.html` líneas 38-52

Presentación principal con:
- Fotografía de perfil con efecto de borde gradient
- Nombre y título profesional
- Redes sociales con iconos animados

### 3. Sobre Mí

**Ubicación:** `index.html` líneas 54-122

Contiene:
- Biografía profesional
- Resumen del perfil
- Experiencia laboral destacada
- Educación y certificaciones
- Habilidades técnicas y blandas

**Tarjetas informativas:**
- `perfil-profesional`: Resumen del perfil
- `resumen-profesional`: Experiencia en Coppel Afore
- `educacion`: Formación académica
- `habilidades-tecnicas`: Lenguajes y herramientas
- `habilidades-blandas`: Competencias suaves

### 4. Datos Profesionales (Skills)

**Ubicación:** `index.html` líneas 124-162

**Subsecciones:**

#### Certificaciones
Lista de cursos y certificaciones obtenidas:
- Inglés B1
- Preparación ISTQB
- Python para automatización
- Testing estático
- Fundamentos QA
- Automatización con Selenium

#### Áreas de Especialización
Herramientas y tecnologías con tooltips informativos:
- Selenium WebDriver
- PyTest
- API Testing
- CI/CD
- SQL
- Testing Manual

### 5. Experiencia Profesional

**Ubicación:** `index.html` líneas 164-191

Historial laboral con tarjetas para cada puesto:
- **APinterfaces (Coppel Afore)**: Feb 2022 - Dic 2023
- **Pascal Solutions**: Jul 2025

Cada tarjeta incluye:
- Título del puesto
- Período de trabajo
- Lista de responsabilidades

### 6. Proyectos

**Ubicación:** `index.html` líneas 193-241

Galería de proyectos con tarjetas que incluyen:
- Icono representativo
- Título del proyecto
- Descripción breve
- Enlace a página detallada

**Proyectos actuales:**
1. Suite de Pruebas Automatizadas (Selenium + PyTest)
2. Gestor de Tareas Flask (Railway)
3. API Testing con Postman

### 7. Curriculum

**Ubicación:** `index.html` líneas 243-263

Sección con botones de descarga:
- CV en español (PDF)
- Cover Letter en inglés (PDF)

### 8. Contacto

**Ubicación:** `index.html` líneas 265-283

Formulario funcional conectado a Formspree:
- Campo nombre
- Campo email
- Campo mensaje
- Botón de envío

### 9. Footer

**Ubicación:** `index.html` líneas 285-309

Pie de página con:
- Descripción breve
- Enlaces de navegación
- Tecnologías utilizadas
- Redes sociales
- Copyright

---

## Formulario de Contacto

### Configuración

El formulario utiliza **Formspree** para recibir mensajes:

```html
<form action="https://formspree.io/f/mjkvvowb" method="POST">
```

### Personalizar el Endpoint

1. Regístrate en [Formspree](https://formspree.io)
2. Crea un nuevo formulario
3. Copia tu ID de formulario
4. Actualiza el atributo `action`:

```html
<!-- Cambiar mjkvvowb por tu ID -->
<form action="https://formspree.io/f/TU_ID_AQUI" method="POST">
```

### Campos del Formulario

| Campo | Name | Tipo | Requerido |
|-------|------|------|-----------|
| Nombre | `nombre` | text | Sí |
| Email | `email` | email | Sí |
| Mensaje | `mensaje` | textarea | Sí |

---

## Componentes JavaScript

### 1. script_navbar.js

**Ubicación:** `src/script_navbar.js`

**Funcionalidades:**

```javascript
// Efectos del header
- Navbar se reduce al hacer scroll
- Clase 'scrolled' añadida cuando scrollY > 100

// Menú móvil
- Toggle del menú hamburguesa
- Animación de icono (bars ↔ times)
- Cierre automático al hacer clic en enlace

// Navegación activa
- Highlight del enlace según sección visible
- Offset de 150px para compensación del header
```

### 2. script_tooltips.js

**Ubicación:** `src/script_tooltips.js`

**Funcionamiento:**

```javascript
// Objeto con textos de ayuda
const tooltips = {
    selenium: "Descripción...",
    pytest: "Descripción...",
    // más...
}

// Agrega tooltip a elementos con clase 'tooltip'
// Busca data-tooltip y muestra texto informativo
```

**Uso en HTML:**
```html
<span class="tooltip" data-tooltip="selenium">
    <strong>Selenium:</strong>
</span>
```

### 3. validación_formulario.js

**Ubicación:** `src/validación_formulario.js`

**Validaciones implementadas:**

| Campo | Validación | Mensaje |
|-------|-------------|---------|
| Nombre | Mínimo 2 caracteres | "El nombre debe tener al menos 2 caracteres" |
| Email | Formato válido | "Por favor, ingresa un email válido" |
| Mensaje | Mínimo 10 caracteres | "El mensaje debe tener al menos 10 caracteres" |

**Características:**
- Validación en tiempo real (blur)
- Validación al enviar (submit)
- Feedback visual (verde/rojo)
- Estados de carga
- Mensaje de éxito

---

## Personalización

### Cambiar Información Personal

Edita `index.html`:

```html
<!-- Cambiar nombre -->
<h1>Tu Nombre</h1>

<!-- Cambiar título -->
<h2>Tu Título</h2>

<!-- Cambiar bio -->
<p>Tu descripción...</p>
```

### Cambiar Colores

Edita `style.css` - Sección `:root`:

```css
:root {
    /* Colores principales */
    --accent-primary: #6366f1;      /* Color principal */
    --accent-secondary: #8b5cf6;    /* Color secundario */
    --accent-tertiary: #a855f7;     /* Color terciario */
    
    /* Fondos */
    --bg-primary: #0a0a0f;          /* Fondo principal */
    --bg-secondary: #12121a;        /* Fondo secundario */
    --bg-card: #1a1a24;             /* Fondo de tarjetas */
    
    /* Textos */
    --text-primary: #f8fafc;        /* Texto principal */
    --text-secondary: #94a3b8;      /* Texto secundario */
    --text-muted: #64748b;          /* Texto terciario */
}
```

### Cambiar Imagen de Perfil

1. Reemplaza `img/jose ramon.png`
2. Mantén el nombre o actualiza en `index.html`:
```html
<img src="img/tu-foto.png" alt="Tu Nombre" />
```

### Agregar Nuevos Proyectos

1. Crea una nueva página HTML en `proyectos/`
2. Incluye los estilos compartidos:
```html
<link rel="stylesheet" href="styles.css">
```

3. Agrega la tarjeta en `index.html`:
```html
<div class="proyecto">
    <a href="proyectos/nuevo-proyecto.html">
        <div class="proyecto-card">
            <i class="fas fa-icono"></i>
            <h4>Título del Proyecto</h4>
            <p>Descripción breve</p>
        </div>
    </a>
</div>
```

### Agregar Tooltips

Edita `src/script_tooltips.js`:

```javascript
const tooltips = {
    // Agregar nueva entrada
    nueva_herramienta: "Descripción de la herramienta.",
};
```

Luego úsalo en HTML:
```html
<span class="tooltip" data-tooltip="nueva_herramienta">
    <strong>Nueva Herramienta:</strong>
</span>
```

---

## Despliegue

### GitHub Pages (Recomendado)

1. Sube tu código a GitHub
2. Ve a Settings > Pages
3. Selecciona la rama `main` y carpeta `/ (root)`
4. Guarda los cambios
5. Tu sitio estará disponible en:
   ```
   https://tu-usuario.github.io/mis-pruebas/
   ```

### Netlify

1. Crea cuenta en [Netlify](https://netlify.com)
2. Arrastra la carpeta del proyecto
3. ¡Listo! Obtén URL automática

### Vercel

1. Crea cuenta en [Vercel](https://vercel.com)
2. Importa tu repositorio de GitHub
3. Deploy automático

### Dominio Personalizado

Si tienes un dominio:

1. **GitHub Pages:**
   - Settings > Pages > Custom domain
   - Configura los registros DNS

2. **Netlify/Vercel:**
   - Agrega tu dominio en la configuración
   - Sigue las instrucciones para DNS

---

## Mantenimiento

### Actualizar Contenido

**Experiencia laboral:**
```html
<!-- Buscar sección experiencia-profesional -->
<!-- Agregar/modificar tarjetas -->
<div class="card">
    <h3>Nuevo Puesto</h3>
    <p>Descripción...</p>
</div>
```

**Proyectos:**
```html
<!-- Buscar sección proyectos -->
<!-- Agregar nueva tarjeta de proyecto -->
```

**Habilidades:**
```html
<!-- En script_tooltips.js -->
<!-- Agregar nueva entrada al objeto -->
```

### Revisar Links

Periódicamente verifica que todos los links funcionen:
- ✅ Links internos (secciones)
- ✅ Links externos (LinkedIn, GitHub)
- ✅ Descargas de PDF
- ✅ Enlaces a proyectos

### Actualizar SEO

Edita los meta tags en `<head>`:

```html
<meta name="description" content="Tu nueva descripción">
<meta name="keywords" content="nuevas, palabras clave">
```

### Backup

Recomendaciones:
- Mantén un repositorio Git actualizado
- Haz commits regulares con mensajes descriptivos
- Guarda copias locales de imágenes y documentos

---

## Comandos Útiles

```bash
# Clonar repositorio
git clone https://github.com/joseramon95/mis-pruebas.git

# Actualizar cambios
git add .
git commit -m "Descripción del cambio"
git push origin main

# Ver cambios localmente
python -m http.server 8000
```

---

## Solución de Problemas

### El menú no funciona en móvil

Verifica que:
1. El archivo `script_navbar.js` está enlazado
2. El elemento `.nav-responsive` existe en el HTML
3. Los media queries están correctos en CSS

### El formulario no envía

1. Verifica el endpoint de Formspree
2. Revisa la consola del navegador (F12)
3. Confirma que los campos tienen los `name` correctos

### Las fuentes no cargan

1. Verifica conexión a internet
2. Comprueba las URLs de Google Fonts
3. Considera descargar fuentes localmente

### Imágenes no aparecen

1. Verifica que las rutas sean correctas
2. Confirma que los archivos existen
3. Usa rutas relativas desde index.html

---

## Recursos Adicionales

- [Documentación Font Awesome](https://fontawesome.com/docs)
- [Guía de Formspree](https://formspree.io/docs)
- [CSS Tricks - Guía de CSS](https://css-tricks.com)
- [MDN Web Docs](https://developer.mozilla.org)

---

## Contacto

- **Email:** joserramonmadridvaldez@gmail.com
- **LinkedIn:** [joseramonmadridvaldez](https://www.linkedin.com/in/joseramonmadridvaldez)
- **GitHub:** [joseramon95](https://github.com/joseramon95)
- **WhatsApp:** [+52 667 780 0166](https://wa.me/+526677800166)

---

## Licencia

Este proyecto es de código abierto. Puedes usarlo y modificarlo bajo tu propia responsabilidad.

---

*Última actualización: 2025*
