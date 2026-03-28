# Deploy - E³ Consultoría

## Resumen

Este documento describe la arquitectura de deploy del proyecto E³.

## Arquitectura

```
┌─────────────────────────────┐         ┌─────────────────────────────┐
│         VERCEL             │         │          RENDER             │
│    (Frontend - Astro)      │         │    (API - Flask)           │
│                            │         │                            │
│  https://mis-pruebas       │  ────── │  https://e3-admin-api      │
│  .vercel.app               │   API   │  .onrender.com            │
└─────────────────────────────┘         └─────────────────────────────┘
```

## URLs de Producción

| Servicio | URL |
|----------|-----|
| Frontend (Vercel) | https://mis-pruebas.vercel.app |
| API/Admin (Render) | https://e3-admin-api.onrender.com |

## Credenciales Admin

- **URL:** https://e3-admin-api.onrender.com/login
- **Usuario:** `root`
- **Contraseña:** `root`

## Ramas Git

| Rama | Contenido |
|------|-----------|
| `master` | Proyecto principal (antes de mover E3_Admin) |
| `astro` | Frontend Astro (sitio web) |
| `api` | API Flask (admin + endpoints) |

## Cómo Actualizar el Sitio

Cada vez que haces cambios en el admin (agregar/editar socios o componentes), debes hacer rebuild del sitio:

```bash
# En la carpeta del proyecto (rama astro)
vercel --prod --yes
```

El build toma ~20-30 segundos.

## Endpoints de la API

| Endpoint | Descripción |
|----------|-------------|
| `/api/socios` | Lista socios activos |
| `/api/componentes` | Lista todos los componentes |

## Variables de Entorno

En el proyecto Astro (rama `astro`), crear `.env`:

```bash
PUBLIC_API_URL=https://e3-admin-api.onrender.com
```

## Archivos de Configuración

### Render (rama `api`)

- `runtime.txt` - `python-3.11.0`
- `Procfile` - `web: gunicorn app:app --bind 0.0.0.0:$PORT`
- `requirements.txt` - Flask + gunicorn

### Vercel (rama `astro`)

- `astro.config.mjs` - Configuración con @astrojs/vercel
- `.env` - PUBLIC_API_URL

## Notas

- El tier gratuito de Render hace que la API "duerma" después de 15 min de inactividad
- Se activa automáticamente con el primer request (~10-30 seg)
- Los datos del sitio se "incrustan" en build time - no se consultan en tiempo real
- SQLite se usa en Render (limitación del tier gratuito)

## Comandos Útiles

```bash
# Switch a rama astro para hacer deploy
git switch astro

# Deploy a Vercel
vercel --prod --yes

# Switch a rama api para modificar API
git switch api

# Deploy API a Render (desde rama api)
./render.exe deploys create srv-ID --wait --confirm
```

## Solución de Problemas

### La API no responde
- Render puede tardar 10-30 seg en despertar del modo sleep
- Verifica que el servicio esté activo en https://dashboard.render.com

### Los cambios no aparecen en el sitio
- Debes hacer rebuild con `vercel --prod --yes`
- Los datos se incrustan en build time

### Error en deploy de Render
- Verificar que el Start Command sea: `gunicorn app:app --bind 0.0.0.0:$PORT`
- Verificar requirements.txt tenga gunicorn
