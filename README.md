# E³ Admin - API Flask

## URLs de Producción

| Servicio | URL |
|----------|-----|
| API/Admin | https://e3-admin-api.onrender.com |

## Credenciales

- **Usuario:** root
- **Contraseña:** root

## Setup Local

```bash
pip install -r requirements.txt
python app.py
```

## Deploy a Render

### Archivos de Configuración

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

# Listar servicios
./cli_vX.X.X.exe services

# Deploy
./cli_vX.X.X.exe deploys create SERVICIO_ID --wait --confirm

# Ver logs
./cli_vX.X.X.exe logs -r SERVICIO_ID --limit 50
```

### Variables de Entorno

En Render, agregar:
- Key: `DATABASE_URL`
- Value: URL de PostgreSQL

## PostgreSQL

- **Host:** dpg-d7436pq4d50c73c0iav0-a.oregon-postgres.render.com
- **Database:** base_de_datos_eta3
- **Usuario:** jose
- **Password:** 94VDOGBzyCj6qexcKFGNtSUnW3NtCSlT

## API Endpoints

| Endpoint | Descripción |
|----------|-------------|
| `/api/socios` | Lista socios activos |
| `/api/componentes` | Lista todos los componentes |

## Notas

- El tier gratuito de Render hace que la API "duerma" después de 15 min de inactividad
- Se activa automáticamente con el primer request (~10-30 seg)
- PostgreSQL persiste los datos entre deploys
