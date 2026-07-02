#!/bin/bash

set -e

echo "========================================"
echo "  diapo_creator setup"
echo "  Slidev + reveal.js coexistence"
echo "========================================"
echo ""

if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed. Please install Node.js 18+ first."
    echo "  https://nodejs.org/"
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "Node.js $(node -v) detected"
echo "Python $(python3 -V | cut -d' ' -f2) detected"
echo ""

echo "Installing npm dependencies (Slidev, Marp, reveal.js skill)..."
npm install

echo ""
echo "Installing Playwright Chromium (for Slidev PDF export)..."
npx playwright install chromium

echo ""
echo "========================================"
echo "  Setup complete!"
echo "========================================"
echo ""
echo "Slidev (clases existentes):"
echo "  npx slidev slides.md              # Start dev server (localhost:3030)"
echo "  npx slidev build slides.md        # Build static SPA"
echo "  npx slidev export slides.md       # Export to PDF"
echo ""
echo "reveal.js (nuevas presentaciones):"
echo "  cd nombre_presentacion/"
echo "  python3 -m http.server 8080       # Start dev server"
echo "  npx decktape reveal \"http://localhost:8080/index.html\" output.pdf --screenshots"
echo ""
