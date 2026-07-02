# AGENTS.md

## Contexto del Proyecto

Herramienta para crear presentaciones para clases y tesis en la **Universidad Adolfo Ibáñez**.
Profesor: Mateo Taito Stambuk. Todo el contenido debe estar en **español**.

El repositorio usa **dos stacks en coexistencia**:

- **Slidev** (Markdown → SPA) para clases de programación y proyectos existentes.
- **reveal.js** (HTML + CSS) para presentaciones nuevas, defensas de tesis y materiales pulidos.

> Las nuevas presentaciones se crean en **reveal.js**. Las clases existentes (`Clase_MMDD/`) siguen en Slidev y no se migran.

## Convenciones Fundamentales

- **Todo en español**: textos, comentarios, nombres de variables, explicaciones
- **Python simple**: usar solo `random` y, para gráficos, `PIL/Pillow` (ambos preinstalados)
- **Propósito didáctico**: cada diapositiva debe enseñar un concepto de forma clara y progresiva
- **Paleta de colores obligatoria**:
  - Azul: `#1a2744`, `#2d3e5f` (títulos, conceptos principales)
  - Magenta: `#8b1a6e` (destacados, conceptos clave)
  - Naranja: `#c45200` (alertas, ejemplos, énfasis)
- Definir las variables CSS en `:root` y usarlas en todo el archivo

## Estructura de Directorios

### Clases en Slidev (legado)
- `Clase_MMDD/` - cada clase es un directorio con fecha (ej: `Clase_2705/`)
  - `slides.md` - Presentación principal
  - `slides_alt.md` - Versión alternativa (generada por scripts Python)
  - `*.py` - Soluciones de ejercicios en Python
  - `diagramas/` - Imágenes de diagramas PlantUML
- `demo-slidev/` - Presentación de referencia Slidev

### Presentaciones en reveal.js (nuevo estándar)
- `nombre_presentacion/` - cada deck es un directorio
  - `index.html` - Diapositivas (estructura HTML)
  - `styles.css` - Estilos personalizados
  - `assets/` - Imágenes y figuras (PNG, SVG)
  - `generar_grafico_*.py` - Scripts opcionales para regenerar figuras
- `demo-revealjs/` - Plantilla de referencia con paleta, layouts y comandos

## Comandos

### Slidev (clases existentes)

```bash
# Setup inicial (ejecutar una vez)
./setup.sh

# Desarrollo
npx slidev slides.md              # Servidor en localhost:3030

# Build y Exportación
npx slidev build slides.md        # Build SPA estática (output: dist/)
npx slidev export slides.md       # Exportar a PDF (requiere playwright-chromium)

# Diagramas
node generate_diagrams.js         # Generar diagramas PlantUML (requiere internet)
```

### reveal.js (nuevo estándar)

```bash
# Desarrollo: servir carpeta con servidor estático
cd nombre_presentacion/
python3 -m http.server 8080       # Abrir http://localhost:8080

# Verificación de overflow
node .agents/skills/revealjs/scripts/check-overflow.js index.html

# Generar PDF + screenshots por lámina
npx decktape reveal "http://localhost:8080/index.html" output.pdf --screenshots

# Editar texto en navegador (opcional)
node .agents/skills/revealjs/scripts/edit-html.js index.html
```

## Sintaxis reveal.js

- Diapositivas separadas por `<section>` dentro de `<div class="slides">`
- Sin paso de build: las dependencias (reveal.js, fuentes) se cargan por CDN
- Layouts mediante CSS grid/flex inline (no hay layouts predefinidos como en Slidev)
- Tamaños de fuente en `pt` (puntos), no `px` ni `rem`
- Referencia completa: `.agents/skills/revealjs/SKILL.md`

## Creación de Contenido

### Para clases nuevas en Slidev
1. Crear directorio `Clase_MMDD/`
2. Archivo principal: `slides.md`
3. Colocar soluciones Python junto a las diapositivas
4. Diagramas vía `generate_diagrams.js` (PlantUML)

### Para presentaciones nuevas en reveal.js
1. Crear directorio con nombre descriptivo
2. Copiar `index.html` y `styles.css` desde `demo-revealjs/`
3. Definir la paleta en `:root` con los 3 colores del proyecto
4. Una `<section>` por lámina, con `id` único
5. Para imágenes, generar PNG con `generar_grafico_X.py` usando Pillow
6. Verificar overflow y generar PDF antes de presentar

## Plantilla de Diapositiva reveal.js

```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Mi Presentación</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reset.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <section id="slide-1">
        <h2>Título</h2>
        <p>Contenido...</p>
      </section>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
  <script>
    Reveal.initialize({ width: 1280, height: 720, controls: true, progress: true, slideNumber: true, hash: true });
  </script>
</body>
</html>
```

## Problemas Conocidos

- `generate_diagrams.js` (Slidev) requiere `plantuml-encoder` que no está en `package.json`
- `.gitignore` es mínimo (solo `node_modules/`); considerar ignorar `dist/`, `*-export.pdf`, `diagramas/*.png`, `screenshots/`
- `check-overflow.js` del skill `revealjs` requiere `puppeteer` (no instalado). Alternativa: `npx decktape` + revisión visual de screenshots
- Reveal.js no detecta cambios automáticamente en el navegador: refrescar manualmente (Ctrl+R)
