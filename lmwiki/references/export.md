# Export: HTML, TeX e PDF

Use este modo quando o usuário pedir para visualizar a wiki no navegador, gerar um site estático, produzir TeX/LaTeX, compilar PDF, ou criar uma versão navegável da base inteira.

## Princípios

- A wiki em markdown é a fonte de verdade. `exports/` é saída gerada e pode ser apagada/recriada.
- Leia o esquema local antes de exportar. Se ele define escopo, ordem, templates, tema, ferramenta ou exclusões, siga essas regras.
- Se não houver convenção de exportação, proponha uma configuração simples e registre-a no esquema se o usuário quiser.
- Valide links internos e reporte links quebrados. Corrija a wiki quando o problema estiver na wiki, não só no HTML ou TeX.
- Registre a exportação em `log.md`.

## Preflight de export

1. Leia `index.md`, o esquema local e as entradas recentes de `log.md`.
2. Determine o escopo: wiki inteira, apenas páginas de `wiki/`, excluir fontes, excluir stubs, incluir anexos, etc.
3. Determine a ordem: a ordem explícita do esquema, a ordem do `index.md`, ou uma ordem proposta por categoria.
4. Determine o formato: `html`, `tex`, `pdf`, ou combinação.
5. Verifique ferramentas disponíveis quando for compilar: prefira `latexmk -pdf`, depois `tectonic`, depois `pdflatex`. Se nenhuma existir, gere apenas o projeto TeX e diga que não compilou.
6. Antes de uma exportação apresentada como "completa", rode o lint estrutural e, quando disponível, `scripts/lint_depth.py <raiz-da-wiki>`. Exportar páginas rasas não as torna completas; corrija ou marque a limitação.

## HTML

Objetivo: gerar uma versão navegável da wiki para abrir no navegador, com linkagem interna fluida.

Destino padrão: `exports/html/`.

Regras:

- Gere `exports/html/index.html` como ponto de entrada.
- Gere uma página HTML para cada página markdown incluída no escopo, preservando estrutura ou usando slugs estáveis.
- Converta wikilinks:
  - `[[Página]]` -> link relativo para a página HTML correspondente.
  - `[[Página|Texto]]` -> link relativo com o texto indicado.
- Preserve links externos como links externos.
- Copie anexos necessários para `exports/html/assets/` quando eles existirem localmente.
- Inclua navegação básica: link para índice, links de anterior/próximo quando houver ordem definida, e backlinks quando forem úteis.
- Se o usuário não pediu estilo específico, use HTML simples, legível e estático. Não introduza framework pesado sem necessidade.
- O site deve funcionar abrindo `exports/html/index.html` diretamente no navegador sempre que possível.

## TeX/PDF

Objetivo: gerar um documento compilável que represente a wiki inteira ou o escopo escolhido, com sumário, capítulos/seções e navegação interna no PDF.

Destino padrão: `exports/tex/`.

Arquivos sugeridos:

```text
exports/tex/
├── wiki.tex
├── chapters/
└── wiki.pdf
```

Regras:

- Gere `wiki.tex` como arquivo principal.
- Use `hyperref` para links internos e navegação no PDF.
- Crie labels estáveis para páginas: por exemplo `sec:conceitos-nome-do-conceito`.
- Converta wikilinks internos para `\hyperref[label]{texto}` quando a página referenciada estiver no escopo.
- Quando a página referenciada estiver fora do escopo, mantenha a menção em texto e registre o link omitido.
- Escape caracteres especiais de TeX (`#`, `%`, `&`, `_`, `{`, `}`, `$`, `~`, `^`, `\`) quando converter texto markdown.
- Preserve a hierarquia da wiki:
  - Visões gerais e sínteses podem virar `\chapter` ou `\section`.
  - Conceitos, entidades e fontes podem virar capítulos, seções ou subseções conforme o tamanho e o esquema local.
- Inclua sumário (`\tableofcontents`) e, quando útil, uma seção de índice de páginas.
- Se compilar PDF, rode a ferramenta apropriada no diretório `exports/tex/` e mantenha os arquivos gerados ali.

## Ordem padrão quando não há esquema

1. Página inicial ou síntese geral, se existir.
2. Sínteses.
3. Conceitos.
4. Entidades/pessoas/lugares.
5. Eventos/cronologias.
6. Fontes processadas.
7. Stubs ou páginas `needs-review`, se o usuário quiser incluir.

## Log

Ao final, acrescente uma entrada como:

```markdown
## [AAAA-MM-DD] export | html + tex_pdf
Escopo: wiki inteira. Gerado `exports/html/index.html` e `exports/tex/wiki.pdf`. Links quebrados: 2.
```

Informe ao usuário os caminhos finais e qualquer limitação: PDF não compilado, links quebrados, imagens omitidas, páginas fora do escopo, ou ferramenta ausente.
