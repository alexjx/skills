#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$SCRIPT_DIR/skills"
DST_DIR="$SCRIPT_DIR/.agents/skills"
CLAUDE_DIR="$SCRIPT_DIR/.claude"
LINK_PATH="$CLAUDE_DIR/skills"
REL_TARGET="../.agents/skills"

if [[ ! -d "$SRC_DIR" ]]; then
	echo "Error: source directory not found: $SRC_DIR" >&2
	exit 1
fi

mkdir -p "$DST_DIR"

# Remove only entries that will be installed to avoid clobbering unrelated content.
while IFS= read -r -d '' entry; do
	name="$(basename "$entry")"
	rm -rf "$DST_DIR/$name"
done < <(find "$SRC_DIR" -mindepth 1 -maxdepth 1 -print0)

cp -av "$SRC_DIR/." "$DST_DIR/"

mkdir -p "$CLAUDE_DIR"

if [[ -e "$LINK_PATH" || -L "$LINK_PATH" ]]; then
	rm -rf "$LINK_PATH"
fi

ln -s "$REL_TARGET" "$LINK_PATH"

echo "Installed skills from $SRC_DIR to $DST_DIR"
echo "Created symlink: $LINK_PATH -> $REL_TARGET"
