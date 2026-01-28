#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_root"

keep_backups="${KEEP_BACKUPS:-3}"
if [ ! -d "backup" ]; then
  echo "No backup directory found."
  exit 0
fi

backups=()
while IFS= read -r line; do
  backups+=("$line")
done < <(ls -dt backup/docs-* 2>/dev/null || true)

if [ "${#backups[@]}" -le "$keep_backups" ]; then
  echo "Nothing to prune (keep ${keep_backups})."
  exit 0
fi

for old in "${backups[@]:$keep_backups}"; do
  rm -rf "$old"
done

echo "Pruned backups, kept ${keep_backups} newest."
