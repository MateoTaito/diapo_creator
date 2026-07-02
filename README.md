# diapo_creator

Herramienta para crear presentaciones en la **Universidad Adolfo Ibáñez**.

El repositorio mantiene **dos stacks en coexistencia**:

- **Slidev** (Markdown → SPA) — clases de programación existentes
- **reveal.js** (HTML + CSS) — presentaciones nuevas, defensas de tesis

## Quick Start

```bash
./setup.sh              # Instala dependencias
```

## Estructura

```
.
├── Clase_2705/         # Clases Slidev (legado, no se migra)
├── Clase_0506/
├── Clase_0306/
├── demo-slidev/        # Plantilla de referencia Slidev
├── demo-revealjs/      # Plantilla de referencia reveal.js
├── lamina_final_taller_1/   # Tesis en reveal.js
├── generate_diagrams.js
├── setup.sh
└── AGENTS.md
```

## Comandos

### Slidev (clases existentes)

```bash
cd Clase_2705/
npx slidev slides.md              # Servidor en localhost:3030
npx slidev build slides.md        # Build estático
npx slidev export slides.md       # PDF
```

### reveal.js (presentaciones nuevas)

```bash
cd nombre_presentacion/
python3 -m http.server 8080       # Servidor local

# Generar PDF + screenshots por lámina
npx decktape reveal "http://localhost:8080/index.html" output.pdf --screenshots
```

## Crear una presentación nueva (reveal.js)

1. Copia `demo-revealjs/` a un nuevo directorio con nombre descriptivo
2. Edita `index.html` — una `<section id="...">` por lámina
3. Personaliza `styles.css` — la paleta UAI ya está definida en `:root`
4. Imágenes en `assets/`
5. Genera el PDF con `decktape` antes de presentar

## Paleta de colores obligatoria

| Color | Hex | Uso |
|-------|-----|-----|
| Azul oscuro | `#1a2744` | Títulos, conceptos principales |
| Azul medio | `#2d3e5f` | Variantes |
| Magenta | `#8b1a6e` | Destacados, conceptos clave |
| Naranja | `#c45200` | Alertas, ejemplos, énfasis |

## Atajos de teclado (durante la presentación)

| Tecla | Acción |
|-------|--------|
| `→` / `Space` | Siguiente lámina |
| `←` | Lámina anterior |
| `F` | Pantalla completa |
| `O` | Vista general |
| `?` | Ver todos los atajos |

## Más información

- [`AGENTS.md`](AGENTS.md) — convenciones y contexto del proyecto
- [reveal.js](https://revealjs.com) — documentación oficial
- [Slidev](https://sli.dev) — documentación oficial
