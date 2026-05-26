# diapo_creator

Create presentations with **Slidev** — Markdown-based slides with animations, code highlighting, diagrams, and more.

## Quick Start

```bash
./setup.sh              # Install dependencies
npx slidev slides.md    # Start dev server at localhost:3030
```

## Commands

| Command | Description |
|---------|-------------|
| `npx slidev slides.md` | Start dev server with live reload |
| `npx slidev build slides.md` | Build static SPA (output: `dist/`) |
| `npx slidev export slides.md` | Export to PDF |
| `npx slidev export slides.md --format pptx` | Export to PowerPoint |

## Keyboard Shortcuts (during presentation)

| Key | Action |
|-----|--------|
| `→` / `Space` | Next slide |
| `←` | Previous slide |
| `C` | Toggle drawing mode |
| `B` / `.` | Black screen |
| `W` | White screen |
| `D` | Toggle dark mode |
| `F` | Fullscreen |
| `O` | Overview mode |
| `?` | Show all shortcuts |

## Slide Syntax

```markdown
---
theme: default
title: My Presentation
---

# First Slide

Content here

---

# Second Slide

<div v-click>Appears on click</div>

```ts {1|2-3|all}
// Click-through code highlighting
const x = 42
```
```

## Resources

- [Slidev Docs](https://sli.dev)
- [Theme Gallery](https://sli.dev/resources/theme-gallery)
