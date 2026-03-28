# Sistema de Logging

## Dependencias

```json
"@astrojs/vercel": "^7.x.x"
```

## Archivos

| Archivo | Descripción |
|---------|-------------|
| `src/utils/logger.ts` | Utilidad para guardar logs en archivos |
| `src/middleware.ts` | Middleware que registra visitas automáticamente |
| `src/pages/api/log.ts` | Endpoint API para logging desde formularios |

## Uso

### Logging automático de visitas

El middleware registra:
- **IP** del cliente
- **Path** visitado
- **User-Agent**
- **Método** HTTP

### Logging desde formularios

```javascript
await fetch('/api/log', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ 
    action: 'NOMBRE_ACCION', 
    dato1: 'valor1',
    dato2: 'valor2'
  })
});
```

## Formato de Log

```
[2026-03-27T22:45:00.000Z] VISIT | {"ip":"192.168.1.1","method":"GET","path":"/","userAgent":"..."}
[2026-03-27T22:45:00.000Z] COTIZACION | {"ip":"192.168.1.1","nombre":"Juan","email":"juan@email.com",...}
```

## Ubicación de Archivos

| Entorno | Ruta |
|---------|------|
| Local | `./logs/YYYY-MM-DD.log` |
| Vercel | `/tmp/logs/YYYY-MM-DD.log` |

## Ver logs en local

```bash
# Ver log de hoy
type logs\2026-03-27.log

# Follow en tiempo real (PowerShell)
Get-Content logs\2026-03-27.log -Wait
```

## Integraciones existentes

- **Contact.astro** → Registra `CONTACTO`
- **Cotizaciones.astro** → Registra `COTIZACION`
