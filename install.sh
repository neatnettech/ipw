#!/usr/bin/env bash

set -e

REPO_URL="https://github.com/neatnettech/ipw"
INSTALL_DIR="$HOME/.ipw-cli"
BIN_DIR="$HOME/.local/bin"
VENV_DIR="$INSTALL_DIR/.venv"

echo "📦 Installing ipw..."

# Clean install or update
if [ -d "$INSTALL_DIR/.git" ]; then
  echo "🔁 Updating existing install..."
  git -C "$INSTALL_DIR" pull
else
  echo "⬇️ Cloning repository..."
  rm -rf "$INSTALL_DIR"
  git clone "$REPO_URL" "$INSTALL_DIR"
fi

cd "$INSTALL_DIR"

# Safety check: pyproject.toml must exist
if [ ! -f "pyproject.toml" ]; then
  echo "❌ Error: pyproject.toml not found in $INSTALL_DIR. Aborting."
  exit 1
fi

# Install Poetry if missing
if ! command -v poetry &> /dev/null; then
  echo "❌ Poetry not found. Installing poetry..."
  curl -sSL https://install.python-poetry.org | python3 -
  export PATH="$HOME/.local/bin:$PATH"
fi

# Install the project
echo "📦 Installing dependencies..."
poetry install

# Link CLI to ~/.local/bin
mkdir -p "$BIN_DIR"
EXEC_PATH=$(poetry run which ipw)

if [ -z "$EXEC_PATH" ]; then
  echo "❌ ipw command not found after poetry install. Aborting."
  exit 1
fi

ln -sf "$EXEC_PATH" "$BIN_DIR/ipw"
echo "🔗 Linked ipw to $BIN_DIR/ipw"

echo "✅ Done! Run: ipw"
echo "🔁 Make sure $BIN_DIR is in your PATH."