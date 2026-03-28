# Build y Deploy - Astro + Vercel

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

## Preview (Pre-visualización)

```bash
npm run preview
```
Sirve el build localmente para probar.

## Deploy a Vercel

### Opción 1: CLI (Recomendado)
```bash
vercel --prod --yes
```

### Opción 2: Git (Automático)
1. Hacer push a la rama `astro`
2. Vercel detecta automáticamente el deploy

## Notas

- El proyecto usa el adaptador `@astrojs/vercel`
- Configuración en `astro.config.mjs`
- La variable de entorno `PUBLIC_API_URL` debe estar en `.env`
