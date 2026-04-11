DOCUMENTACION DE FLUJO Y DEPENDENCIAS - PROYECTO E3
====================================================

ARQUITECTURA GENERAL
--------------------
El proyecto usa Astro con SSR (server-side rendering) y Tailwind CSS.
Consume datos de una API externa (e3-admin-api.onrender.com) y tiene fallback a datos locales.

FLUJO DE DATOS
--------------

1. API EXTERNA (e3-admin-api.onrender.com)
   La API proporciona datos dinamicos para componentes via endpoints:
   
   - GET /api/socios
     → Devuelve array de objetos para el carrusel (Features)
     → Estructura: { id, title, description, image, contact: { text, link } }
   
   - GET /api/componentes
     → Devuelve array de todos los componentes configurables
   
   - GET /api/componentes/{nombre}
     → Devuelve un componente especifico por nombre
   
   - GET /api/contenido/soluciones (NUEVO - 2026-04-11)
      → Devuelve datos para la pagina de soluciones/casos de exito
      → Estructura: { titulo, subtitulo, casos: CasoExito[] }
   
   - GET /api/contenido/soluciones/{slug} (NUEVO - 2026-04-11)
      → Devuelve detalle de un caso de exito especifico
      → Estructura: CasoDetalle

2. COMPONENTES QUE USAN getComponente():
   
   a) Hero.astro
      → usa: titulo, subtitulo, contenido, link, extra_data
      → Nombre en API: 'Hero'
   
   b) AboutUs.astro
      → usa: titulo, extra_data (JSON con valores)
      → extra_data contiene: valor1-5, lema
      → Nota: contenido unificado en el componente (2026-04-11)
      → Efecto: neon-backlight/biselado con box-shadows
      → Nombre en API: 'AboutUs'
   
   c) CTA.astro
      → usa: titulo, contenido, link, extra_data (texto del boton)
      → Nombre en API: 'CTA'
   
   d) Contact.astro
      → usa: titulo, contenido, link, extra_data (JSON)
      → extra_data contiene: email, telefono, ubicacion
      → Nombre en API: 'Contact'

3. PAGINA PRINCIPAL (index.astro)
   → Fetch independiente a /api/socios para el carrusel
   → Fetch independiente a /api/componentes/Features para titulo/descripcion
   → Timeout de 5 segundos
   → Fallback a defaultItems si la API falla

4. PAGINA SOLUCIONES (/soluciones - NUEVO 2026-04-11)
   → Archivo: src/pages/soluciones.astro
   → Fetch a /api/contenido/soluciones
   → Componente: src/components/Soluciones.astro
   → Timeout de 5 segundos
   → Fallback a datos locales si la API falla

INTERFAZ COMPONENTE (componentes.ts)
------------------------------------
interface Componente {
    nombre: string;      // Identificador unico (Hero, AboutUs, CTA, Contact)
    titulo: string;     // Titulo principal de la seccion
    subtitulo: string;  // Subtitulo (usado en Hero)
    contenido: string;  // Descripcion o texto principal
    link: string;       // URL de destino (WhatsApp, formulario, etc.)
    extra_data: string; // JSON stringificado con datos adicionales
}

USO DE extra_data POR COMPONENTE:
- Hero: texto del boton
- AboutUs: valores dinamicos (valores, lema)
- CTA: texto del boton
- Contact: datos de contacto (email, telefono, ubicacion)

INTERFAZ SOLUCIONES (soluciones.ts - NUEVO 2026-04-11)
-------------------------------------------------------
interface CasoExito {
    id: number;
    slug: string;       // URL amigable para el caso
    titulo: string;
    descripcion: string;
    imagen: string;
    testimonio: {
        autor: string;
        cargo: string;
        texto: string;
    } | null;
}

interface SolucionesData {
    titulo: string;
    subtitulo: string;
    casos: CasoExito[];
}

interface CasoDetalle extends CasoExito {
    contenido: string;    // Descripcion extendida del caso
    resultados: string[]; // Lista de resultados obtenidos
}

ARCHIVOS DE DATOS ESTATICOS
---------------------------

1. backgroundImages.ts
   → Configuracion de imagenes de fondo por seccion
   → Secciones: hero, carousel, cta
   → Define imageUrl y gradientOverlay

2. carouselItems.ts
   → Tipo CarouselItem para el carrusel
   → Exporta featureItems (datos por defecto, actualmente no usado)
   → Nota: index.astro define sus propios defaultItems

3. soluciones.ts (NUEVO 2026-04-11)
   → Interfaces para datos de casos de exito
   → Tipos: CasoExito, SolucionesData

NOTA SOBRE featureItems vs defaultItems
---------------------------------------
- carouselItems.ts exporta featureItems (datos locales del carrusel)
- index.astro define defaultItems (mismo contenido)
- Esta duplicacion deberia resolverse en el futuro

CONFIGURACION DE ENTORNO
------------------------
Variable de entorno: PUBLIC_API_URL
- Valor en produccion: https://e3-admin-api.onrender.com
- Fallback: https://e3-admin-api.onrender.com (unificado)

RUTAS DE PAGINAS
----------------
- / (index.astro) - Pagina principal
- /soluciones (soluciones.astro - NUEVO) - Pagina de casos de exito
- /soluciones/[slug] (soluciones/[slug].astro - NUEVO) - Detalle de caso de exito
- /cotizaciones (cotizaciones.astro) - Pagina de cotizaciones
- /api/* - Rutas de API internas

COMPONENTES
-----------
- Header.astro: Navegacion principal
- Hero.astro: Seccion hero con imagen de fondo
- Features.astro: Wrapper del carrusel
- Carousel.astro: Carrusel de socios/pillars
- AboutUs.astro: Seccion Quienes Somos con efecto neon-backlight
- MisionVision.astro: Mision y Vision
- Soluciones.astro (NUEVO): Grid de casos de exito con efecto neon
- SolucionesBanner.astro (NUEVO): Banner con preview de casos en index
- CTA.astro: Llamada a la accion
- Contact.astro: Formulario de contacto
- Footer.astro: Pie de pagina

DEPENDENCIAS PRINCIPALES
------------------------
- @astrojs/vercel: Adapter para deploy en Vercel
- astro: Framework principal
- tailwindcss: Estilos CSS

CAMBIOS RECIENTES
-----------------
2026-04-11:
- Creada pagina /soluciones con casos de exito
- Creado componente Soluciones.astro con efecto neon-backlight
- Creado archivo soluciones.ts con interfaces
- Implementado efecto neon-backlight/biselado en AboutUs.astro
- Texto unificado en AboutUs.astro (antes eran dos parrafos separados)
- Actualizado Header para enlazar a /soluciones
- Agregado endpoint /api/contenido/soluciones (pendiente de API)
- Efecto neon-backlight aplicado a: AboutUs, MisionVision, Contact, Soluciones
- Estilos neon unificados en todos los componentes con cuadro de informacion
- Tarjetas de soluciones convertidas en portales con botones "Ver Caso"
- Creada pagina dinamica /soluciones/[slug] para detalle de cada caso
- Agregado campo slug a CasoExito para URLs amigables
- Creada interfaz CasoDetalle para paginas de detalle de caso
- Creado componente SolucionesBanner para preview en pagina principal
