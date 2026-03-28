# Deploy con CLI de Render

## 1. Descargar CLI de Render

```bash
# Descargar la última versión (Windows)
curl -L -o render-cli.zip "https://github.com/render-oss/cli/releases/latest/download/cli_latest_windows_amd64.zip"

# O versiÃ³n especÃ­fica (ejemplo v2.15.0)
curl -L -o render-cli.zip "https://github.com/render-oss/cli/releases/download/v2.15.0/cli_2.15.0_windows_amd64.zip"
```

## 2. Extraer

```bash
unzip render-cli.zip
```

## 3. Login (primera vez)

```bash
./cli_v2.15.0.exe login
```

## 4. Listar servicios

```bash
./cli_v2.15.0.exe services
```

## 5. Ver logs

```bash
./cli_v2.15.0.exe logs -r SERVICIO_ID --limit 50
```

## 6. Hacer deploy

```bash
./cli_v2.15.0.exe deploys create SERVICIO_ID --wait --confirm
```

## Notas

- ID del servicio: `srv-d73oq324d50c73bqhih0`
- El flag `--wait` espera a que termine el deploy
- El flag `--confirm` confirma automÃ¡ticamente
