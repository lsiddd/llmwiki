#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

if [[ ! -f "lmwiki/SKILL.md" ]]; then
  echo "error: lmwiki/SKILL.md not found" >&2
  exit 1
fi

rm -f lmwiki.skill
zip -qr lmwiki.skill lmwiki
unzip -t lmwiki.skill >/dev/null

echo "Built lmwiki.skill"
