#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$SCRIPT_DIR/skills"

if [[ ! -d "$SRC_DIR" ]]; then
	echo "Error: source directory not found: $SRC_DIR" >&2
	exit 1
fi

if [[ "$#" -eq 0 ]]; then
	set -- --skill '*' -y
fi

exec npx skills add "$SRC_DIR" "$@"
