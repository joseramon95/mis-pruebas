# Documentación de API - Proyecto E3

API externa para el frontend de E³ Consultora.

**URL Base:** `https://e3-admin-api.onrender.com`

---

## Endpoints

### GET /api/socios

Devuelve array de objetos para el carrusel de Features/Pillars.

**Respuesta:**
```json
[
  {
    "id": 1,
    "title": "string",
    "description": "string",
    "image": "string (URL)",
    "contact": {
      "text": "string",
      "link": "string (URL)"
    }
  }
]
```

---

### GET /api/componentes

Devuelve array de todos los componentes configurables.

**Respuesta:**
```json
[
  {
    "nombre": "string",
    "titulo": "string",
    "subtitulo": "string",
    "contenido": "string",
    "link": "string",
    "extra_data": "string (JSON)"
  }
]
```

---

### GET /api/componentes/{nombre}

Devuelve un componente específico por nombre.

**Parámetros:**
- `nombre` - Identificador del componente

**Componentes disponibles:**
- `Hero`
- `AboutUs`
- `MisionVision`
- `CTA`
- `Contact`
- `Features`

**Respuesta:**
```json
{
  "nombre": "string",
  "titulo": "string",
  "subtitulo": "string",
  "contenido": "string",
  "link": "string",
  "extra_data": "string (JSON)"
}
```

---

### GET /api/contenido/soluciones

Devuelve la lista de casos de éxito para la página de soluciones.

**Respuesta:**
```json
{
  "titulo": "Casos de Éxito",
  "subtitulo": "string",
  "casos": [
    {
      "id": 1,
      "slug": "string",
      "titulo": "string",
      "descripcion": "string",
      "imagen": "string (URL)",
      "testimonio": null | {
        "autor": "string",
        "cargo": "string",
        "texto": "string"
      }
    }
  ]
}
```

---

### GET /api/contenido/soluciones/{slug}

Devuelve el detalle de un caso de éxito específico.

**Parámetros:**
- `slug` - URL amigable del caso (ej: `transformacion-empresarial`)

**Respuesta:**
```json
{
  "id": 1,
  "slug": "string",
  "titulo": "string",
  "descripcion": "string",
  "imagen": "string (URL)",
  "contenido": "string (HTML)",
  "resultados": ["string"],
  "testimonio": null | {
    "autor": "string",
    "cargo": "string",
    "texto": "string"
  }
}
```

---

## Estructura de extra_data

Campo `extra_data` para componentes (JSON stringified):

### AboutUs
```json
{
  "valor1": "string",
  "valor2": "string",
  "valor3": "string",
  "valor4": "string",
  "valor5": "string",
  "lema": "string"
}
```

### Contact
```json
{
  "email": "string",
  "telefono": "string",
  "ubicacion": "string"
}
```

### Hero / CTA
```json
"string (texto del botón)"
```

### MisionVision
```json
{
  "mision": "string",
  "vision": "string",
  "lema": "string",
  "lemaAdicional": "string",
  "lemaFinal": "string"
}
```

---

## Notas de Implementación

1. Todos los endpoints deben manejar timeout de 5 segundos
2. Si la API falla, el frontend usa datos locales (fallback)
3. Los campos opcionales pueden ser `null` o no existir
4. Los slugs deben ser URL-friendly (kebab-case)
5. Las imágenes deben ser URLs válidas accesibles públicamente
