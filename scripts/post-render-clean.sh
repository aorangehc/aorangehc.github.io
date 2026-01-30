#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output_dir="${project_root}/site"

rm -rf "${output_dir}/docs" "${output_dir}/docs2" "${output_dir}/backup"
