#!/bin/bash
# Railway build script

set -e

echo "📦 Installing uv..."
pip install uv==0.11.2

echo "📦 Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

echo "✓ Build complete"
