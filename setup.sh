#!/bin/bash

set -e

echo "========================================"
echo "  Slidev Presentation Setup"
echo "========================================"
echo ""

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed. Please install Node.js 18+ first."
    echo "  https://nodejs.org/"
    exit 1
fi

echo "Node.js $(node -v) detected"
echo ""

# Install dependencies
echo "Installing dependencies..."
npm install

echo ""
echo "Installing Playwright Chromium (for PDF export)..."
npx playwright install chromium

echo ""
echo "========================================"
echo "  Setup complete!"
echo "========================================"
echo ""
echo "Usage:"
echo "  npx slidev slides.md              # Start dev server (localhost:3030)"
echo "  npx slidev build slides.md        # Build static SPA"
echo "  npx slidev export slides.md       # Export to PDF"
echo ""
