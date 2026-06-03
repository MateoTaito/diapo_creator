# AGENTS.md

## Contexto del Proyecto

Herramienta para crear presentaciones con **Slidev** para clases de programación en la UAI.
Profesor: Mateo Taito Stambuk. Todo el contenido debe estar en **español**.

## Convenciones Fundamentales

- **Todo en español**: textos, comentarios, nombres de variables, explicaciones
- **Python simple**: usar solo `random` como módulo externo; no usar numpy, pandas, etc.
- **Propósito didáctico**: cada diapositiva debe enseñar un concepto de forma clara y progresiva
- **Paleta de colores obligatoria**:
  - Azul: `#1a2744`, `#2d3e5f` (títulos, conceptos principales)
  - Magenta: `#8b1a6e` (destacados, conceptos clave)
  - Naranja: `#c45200` (alertas, ejemplos, énfasis)
- Usar clases CSS `.highlight-blue`, `.highlight-magenta`, `.highlight-orange` para aplicar colores

## Estructura de Directorios

- `Clase_MMDD/` - Cada clase es un directorio con fecha (ej: `Clase_2705/` para 27 de mayo)
- Dentro de cada clase:
  - `slides.md` - Presentación principal
  - `slides_alt.md` - Versión alternativa (generada por scripts Python)
  - `*.py` - Soluciones de ejercicios en Python
  - `diagramas/` - Imágenes de diagramas PlantUML generados
- `demo-slidev/` - Presentación de referencia

## Comandos

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

## Sintaxis Slidev

- Diapositivas separadas por `---`
- Primer bloque frontmatter = configuración del deck (theme, title, etc.)
- Comentarios HTML `<!-- -->` = notas del presentador
- `v-click` para animaciones por clic
- `::left::` y `::right::` para layouts de dos columnas
- Bloques de código con resaltado: `` ```python {all|1-2|3-4|all} ``
- Referencia completa: `.agents/skills/slidev/SKILL.md`

## Creación de Contenido para Clases

1. Crear directorio siguiendo formato `Clase_MMDD/`
2. Archivo principal debe ser `slides.md`
3. Usar patrón de `update_slides.py` para generar versiones alternativas mediante reemplazo de strings
4. Colocar soluciones Python junto a las diapositivas
5. Generar diagramas añadiendo código PlantUML a `generate_diagrams.js` y ejecutándolo

## Plantilla de Diapositiva

```markdown
---
theme: default
title: "Título de la Clase"
class: text-left
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
mdc: true
---
```

## Problemas Conocidos

- `generate_diagrams.js` requiere `plantuml-encoder` que no está en `package.json`
- `.gitignore` es mínimo (solo `node_modules/`); considerar ignorar `dist/`, `*-export.pdf`, `diagramas/*.png`
