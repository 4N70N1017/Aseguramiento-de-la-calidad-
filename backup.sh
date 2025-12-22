#!/usr/bin/env bash
# Simple backup script for PostgreSQL using pg_dump
# Usage: copy .env values or set DATABASE_URL env var

set -euo pipefail
NOW=$(date +"%Y%m%d_%H%M%S")
OUT_DIR="backups"
mkdir -p "$OUT_DIR"

if [ -z "${DATABASE_URL:-}" ]; then
  echo "DATABASE_URL no está definida. Exporta DATABASE_URL o ajusta la conexión." >&2
  exit 1
fi

FNAME="$OUT_DIR/backup_$NOW.sql"
echo "Creando backup en $FNAME"
pg_dump "$DATABASE_URL" -F p -f "$FNAME"
echo "Backup completado"
