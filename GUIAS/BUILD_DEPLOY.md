# Build y Deploy - E³ Consultoría

## URLs de Producción

| Servicio | URL |
|----------|-----|
| Frontend (Vercel) | https://mis-pruebas.vercel.app |
| API/Admin (Render) | https://e3-admin-api.onrender.com |

## Credenciales Admin

- **URL:** https://e3-admin-api.onrender.com/login
- **Usuario:** `root`
- **Contraseña:** `root`

---

# Astro (Frontend)

## Requisitos Previos

```bash
npm install
```

## Development (Desarrollo local)

```bash
npm run dev
```
Abre http://localhost:4321

## Build (Compilación)

```bash
npm run build
```
Genera la carpeta `dist/` con los archivos estáticos.

## Deploy a Vercel

### CLI (Recomendado)
```bash
vercel --prod --yes
```

### Git (Automático)
1. Hacer push a la rama `astro`
2. Vercel detecta automáticamente el deploy

## Cache

La página usa ISR (Incremental Static Regeneration) con cache de 1 semana.
Cada vez que se hace deploy, los datos se fetchear de la API y se cachean por 7 días.

---

# Flask (API)

## Requisitos

- Python 3.12+
- PostgreSQL (usar psycopg2-binary)

## Development local

```bash
pip install -r requirements.txt
python app.py
```

## Deploy a Render

### Archivos necesarios

- `runtime.txt`: `python-3.12.0`
- `Procfile`: `web: gunicorn app:app --bind 0.0.0.0:$PORT`
- `requirements.txt`: Flask + gunicorn + psycopg2-binary

### Deploy con CLI

```bash
# Descargar CLI
curl -L -o render-cli.zip "https://github.com/render-oss/cli/releases/latest/download/cli_latest_windows_amd64.zip"
unzip render-cli.zip

# Login
./cli_vX.X.X.exe login

# Deploy
./cli_vX.X.X.exe deploys create SERVICIO_ID --wait --confirm
```

### Variables de Entorno

En Render, agregar:
- Key: `DATABASE_URL`
- Value: `postgresql://jose:password@host/base_de_datos`

---

# Proceso de Actualización

1. **Cambios en el admin (socios/componentes):**
   - Editar en https://e3-admin-api.onrender.com
   - Hacer deploy del sitio: `vercel --prod --yes`

2. **Cambios en el código:**
   - Rama `astro`: cambios en el frontend
   - Rama `api`: cambios en la API

---

# Solución de Problemas

## La API no responde
- Render puede tardar 10-30 seg en despertar del modo sleep
- Verifica que el servicio esté activo en https://dashboard.render.com

## Los cambios no aparecen en el sitio
- Debes hacer rebuild con `vercel --prod --yes`
- Los datos se incrustan en build time (ISR)

## Error en deploy de Render
- Verificar que el Start Command sea: `gunicorn app:app --bind 0.0.0.0:$PORT`
- Verificar requirements.txt tenga psycopg2-binary
