# Deploy - E³ Consultoría

## Resumen

Este documento describe la arquitectura de deploy del proyecto E³.

## Arquitectura

```
┌─────────────────────────────┐         ┌─────────────────────────────┐
│         VERCEL              │         │          RENDER             │
│    (Frontend - Astro)       │         │    (API - Flask)            │
│                             │         │                             │
│  https://mis-pruebas        │  ────── │  https://e3-admin-api       │
│  .vercel.app                │   API   │  .onrender.com              │
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

## Proceso de Setup (Historial)

### 1. Situación Inicial
- Proyecto E³ basado en Astro con Tailwind
- API Flask local en carpeta `E3_Admin` (Puerto 5000)
- Frontend consumía datos de `localhost:5000` en desarrollo

### 2. Problema
- Al hacer deploy en Vercel, la API no existía en producción
- El sitio intentaba conectar a `localhost:5000` que no existía
- Errores: `ECONNREFUSED 127.0.0.1:5000`

### 3. Solución Implementada
Se decidió separar en dos servicios:

1. **Frontend (Vercel):** Proyecto Astro
2. **API/Admin (Render):** Flask con SQLite

### 4. Pasos Realizados

#### Para Render (API):
1. Se crearon archivos de configuración:
   - `runtime.txt` → especifica Python 3.11
   - `Procfile` → comando de inicio para gunicorn
   - `requirements.txt` → agregado gunicorn

2. Se creó rama `api` en GitHub con solo archivos de Flask

3. Se configuró el servicio en Render con:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - Rama: `api`

#### Para Vercel (Frontend):
1. Se creó archivo `.env` con:
   ```
   PUBLIC_API_URL=https://e3-admin-api.onrender.com
   ```

2. El código ya usaba `import.meta.env.PUBLIC_API_URL` para consumir la API

3. Se hace rebuild después de cada cambio en el admin

### 5. Problemas Técnicos Resueltos

#### Error 1: "Module not found: your_application"
- **Causa:** Render intentaba usar `gunicorn your_application.wsgi`
- **Solución:** Especificar correctamente en Start Command: `gunicorn app:app`

#### Error 2: "unrecognized arguments: --host 0.0.0.0 --port $PORT"
- **Causa:** Sintaxis incorrecta de gunicorn
- **Solución:** Usar `--bind` en lugar de `--host` y `--port`:
  ```
  gunicorn app:app --bind 0.0.0.0:$PORT
  ```

#### Error 3: El Start Command no se actualizaba
- **Causa:** Render cacheaba la configuración anterior
- **Solución:** Se eliminó el servicio y se creó uno nuevo con la configuración correcta

### 6. Render CLI

Se instaló Render CLI para gestionar el servicio:
- Descarga directa desde GitHub releases
- Login: `./render.exe login`
- Comandos útiles:
  ```bash
  ./render.exe services              # Listar servicios
  ./render.exe deploys create SRV_ID --wait --confirm  # Deploy
  ./render.exe logs SRV_ID -r SRV_ID --limit 50  # Ver logs
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

---

## ⚠️ PROBLEMA: Datos se Borran

### Causa
El tier gratuito de Render usa **SQLite en sistema de archivos efímero**. Cada vez que el servicio:
- Se reinicia
- Hace deploy nuevo
- Entra en modo sleep

...los datos se pierden porque SQLite se almacena localmente.

### Solución: Usar PostgreSQL

PostgreSQL tiene tier gratuito en Render que persiste los datos.

#### Pasos para Migrar a PostgreSQL

1. **Crear PostgreSQL en Render:**
   - Ir a https://dashboard.render.com
   - **New → PostgreSQL**
   - Configurar:
     - Name: `e3-admin-db`
     - Plan: Free
     - Region: Oregon (misma que el servicio)
   - Click **Create Database**

2. **Obtener conexión:**
   - Cuando termine, ir a la DB en el dashboard
   - Buscar **Internal Database URL** o **External Database URL**
   - Tiene formato: `postgres://user:pass@host:5432/database`

3. **Actualizar la API:**
   
   En la rama `api`, modificar `app.py`:
   
   ```python
   # Cambiar de SQLite a PostgreSQL
   import os
   
   # Antes (SQLite)
   app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///e3_admin.db"
   
   # Después (PostgreSQL)
   DATABASE_URL = os.environ.get("DATABASE_URL")
   app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
   ```
   
   También agregar al `requirements.txt`:
   ```
   psycopg2-binary==2.9.9
   ```

4. **Agregar variable de entorno en Render:**
   - Ir al servicio `e3-admin-api` en dashboard
   - **Environment** → **Add Environment Variable**
   - Key: `DATABASE_URL`
   - Value: (la URL de PostgreSQL creada en paso 2)

5. **Hacer deploy de la API:**
   ```bash
   # Desde rama api
   git add . && git commit -m "Migrate to PostgreSQL" && git push origin api
   
   # Deploy con Render CLI
   ./render.exe deploys create srv-d73oq324d50c73bqhih0 --wait --confirm
   ```

6. **Migrar datos existentes:**
   - Una vez conectado a PostgreSQL, los datos不会再 se borran
   - Si había datos en SQLite local, exportarlos e importarlos manualmente

#### Notas Importantes

- PostgreSQL gratis tiene límite de 1 GB
- Los datos persistirán aunque el servicio se reinicie
- No hacer deploy frecuente para evitar interrupciones

#### Alternativa: Supabase

Si se prefiere, también se puede usar Supabase (PostgreSQL externo):
- https://supabase.com
- Cuenta gratis
- Se conecta igual con `DATABASE_URL`
