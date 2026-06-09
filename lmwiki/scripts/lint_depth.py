#!/usr/bin/env python3
"""Heuristic depth lint for LMWiki markdown pages.

This is a triage tool, not a substitute for editorial judgment. It flags
pages marked complete/stable that resemble annotated indexes or abstract-only
summaries.
"""
from pathlib import Path
import argparse
import re
import sys

COMPLETE = {"complete", "completo", "stable"}
HEADINGS = re.compile(r"^#{2,3}\s+(.+)$", re.M)
LINK = re.compile(r"\[[^\]]+\]\([^)]+\)|\[\[[^\]]+\]\]")

SIGNALS = {
    "mechanism": r"\b(mecanismo|como funciona|arquitetura|processo|fluxo|algoritmo|componentes?|modelo conceitual|pipeline|cadeia)\b",
    "variants": r"\b(taxonomia|variantes?|tipos?|familias?|paradigmas?|estrategias?)\b",
    "evaluation": r"\b(metricas?|avaliacao|evidencias?|resultados?|baselines?|experimentos?)\b",
    "limits": r"\b(limitacoes?|limites?|riscos?|falhas?|desafios?|ameacas?|questoes abertas|lacunas?|problemas?)\b",
    "relations": r"\b(relacao|relacoes|comparacao|compara|diverge|divergencias?|complementa|confirma|contribuicao|conexoes?|dependencias?|convergencias?|compromissos?|trade-offs?|dimensoes?|integrada|integrado)\b",
}

def frontmatter(text):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    block = text[4:end]
    data = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip("'\"").lower()
    return data

def plain_words(text):
    text = re.sub(r"---.*?---", "", text, count=1, flags=re.S)
    text = re.sub(r"`[^`]*`|<[^>]+>|https?://\S+", " ", text)
    return re.findall(r"\b[\wÀ-ÿ-]+\b", text)

def lint(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    meta = frontmatter(text)
    status = meta.get("status", "")
    kind = meta.get("type", "")
    words = len(plain_words(text))
    headings = HEADINGS.findall(text)
    links = len(LINK.findall(text))
    lower = text.lower()
    found = {name for name, pattern in SIGNALS.items() if re.search(pattern, lower)}
    issues = []
    if path.name.lower() in {"readme.md", "index.md"}:
        return words, issues

    if status in COMPLETE:
        minimum = 220
        if kind in {"fonte", "source"}:
            minimum = 450
        elif kind in {"sintese", "síntese", "synthesis"}:
            minimum = 280
        if words < minimum:
            issues.append(f"complete page has only {words} words; expected at least {minimum} as triage threshold")
        heading_minimum = 3 if kind in {"sintese", "síntese", "synthesis", "pesquisa-web", "research"} else 5
        if len(headings) < heading_minimum:
            issues.append(f"complete page has only {len(headings)} substantive headings")
        needed = set()
        if kind in {"fonte", "source"}:
            needed = {"mechanism", "limits"}
        elif kind in {"conceito", "concept"}:
            needed = {"mechanism", "limits", "relations", "evaluation"}
        elif kind in {"sintese", "síntese", "synthesis"}:
            needed = {"limits", "relations"}
        elif kind in {"pesquisa-web", "research"}:
            needed = {"limits", "relations"}
        missing = sorted(needed - found)
        if missing:
            issues.append("missing depth signals: " + ", ".join(missing))
        if links >= 4 and "relations" not in found:
            issues.append("multiple links without explicit comparison/contribution language")

    return words, issues

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root)
    wiki = root / "wiki" if (root / "wiki").is_dir() else root
    files = sorted(wiki.rglob("*.md"))
    failures = 0
    for path in files:
        words, issues = lint(path)
        if issues:
            failures += 1
            print(f"FAIL {path} ({words} words)")
            for issue in issues:
                print(f"  - {issue}")
    print(f"\nChecked {len(files)} markdown pages; depth failures: {failures}")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
