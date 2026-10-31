#!/bin/bash
# Build script for Render deployment
# This script installs dependencies and runs tests

set -e

echo "Installing dependencies..."
pip install -r requirements.txt --quiet

echo "Running tests..."
pytest tests/ --no-mistake-box -v

echo "Build completed successfully!"
