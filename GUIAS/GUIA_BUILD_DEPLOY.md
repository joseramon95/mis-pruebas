# Guía: Build y Deploy - Proyecto Astro en Vercel

## 1. Instalar dependencias

```bash
npm install
```

## 2. Probar localmente

```bash
npm run dev
```
Abre http://localhost:4321

## 3. Build local

```bash
npm run build
```
Genera la carpeta `dist/` y `.vercel/`

## 4. Deploy a producción

```bash
vercel --prod --yes
```

## 5. Verificar en Vercel Dashboard

https://vercel.com/dashboard

---

## Solución de problemas

### Error: "astro is not recognized"
→ Ejecutar `npm install` primero

### Error: "vercel is not recognized"
→ Instalar Vercel CLI: `npm i -g vercel`

### Cambios no aparecen
→ Esperar 1-2 min o ejecutar `vercel --prod --yes` nuevamente

### Ver deploys
→ `vercel ls`
