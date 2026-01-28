#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_root"

timestamp="$(date +"%Y%m%d-%H%M%S")"
keep_backups="${KEEP_BACKUPS:-3}"
if [ -d "docs" ] && [ "$keep_backups" -gt 0 ]; then
  mkdir -p "backup"
  backup_dir="backup/docs-${timestamp}"
  mkdir -p "$backup_dir"
  if ! command -v rsync >/dev/null 2>&1; then
    echo "rsync is required for publish. Please install it and retry." >&2
    exit 1
  fi
  rsync -a \
    --exclude "backup/" \
    --exclude "docs/" \
    "docs/" "${backup_dir}/"
fi

quarto render

mkdir -p "docs"
if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync is required for publish. Please install it and retry." >&2
  exit 1
fi
rsync -a --delete "site/" "docs/"

if [ -d "backup" ]; then
  backups=()
  while IFS= read -r line; do
    backups+=("$line")
  done < <(ls -dt backup/docs-* 2>/dev/null || true)

  if [ "${#backups[@]}" -gt "$keep_backups" ]; then
    for old in "${backups[@]:$keep_backups}"; do
      rm -rf "$old"
    done
  fi
fi

echo "Published site/ -> docs (backup kept: ${keep_backups}, latest: backup/docs-${timestamp})"
