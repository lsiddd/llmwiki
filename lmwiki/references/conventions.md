# Convenções: páginas, index.md e log.md

## Frontmatter mínimo

Use o esquema local quando ele existir. Se ainda não existir convenção, comece com este frontmatter simples e ajuste no bootstrap:

```yaml
---
type: conceito | entidade | fonte | sintese
status: draft | stable | needs-review | stub
sources:
  - raw/exemplo.md
updated: AAAA-MM-DD
---
```

Para páginas de fonte, `sources` normalmente aponta para a fonte bruta preservada em `raw/`. Para sínteses, `sources` pode apontar para páginas de fonte, arquivos brutos, ou ambos. Afirmações substantivas em sínteses devem ser rastreáveis.

## Pesquisa web

Pesquisa web é uma etapa auxiliar. Ela pode produzir achados, candidatos a fonte e contexto, mas não substitui ingestão curada.

Quando uma fonte web for integrada:

- registre URL, título, autoria/organização, data de publicação quando existir e data de acesso;
- preserve snapshot, cópia markdown ou nota de fonte em `raw/` quando viável;
- marque incerteza, limitação ou conflito com fontes existentes;
- prefira fonte primária quando disponível.

## Saídas geradas

Use `exports/` para artefatos derivados da wiki. Eles são recriáveis e não devem substituir as páginas markdown como fonte de verdade.

Estrutura sugerida:

```text
exports/
├── html/
│   ├── index.html
│   ├── assets/
│   └── ...
└── tex/
    ├── wiki.tex
    ├── chapters/
    └── wiki.pdf
```

Ao exportar, preserve links internos quando possível:

- Wikilinks `[[Nome da Página]]` viram links relativos no HTML.
- No TeX/PDF, páginas exportadas devem receber labels estáveis, e referências internas devem usar `\hyperref[label]{texto}` ou `\ref{label}` conforme o contexto.
- Links quebrados devem ser reportados. Corrija links óbvios na wiki, não apenas na saída gerada.

## index.md

Catálogo orientado a conteúdo. Organize por categoria e mantenha cada entrada curta: link, resumo de uma linha, metadados opcionais.

Template inicial:

```markdown
# Índice

## Entidades
- [[Nome da Pessoa]]: uma linha resumindo quem é e por que importa aqui. (3 fontes)

## Conceitos
- [[Nome do Conceito]]: uma linha de definição ou contexto. (5 fontes, atualizado em AAAA-MM-DD)

## Fontes processadas
- [[Resumo: Título da Fonte]]: uma linha sobre o que a fonte trouxe.

## Sínteses
- [[Síntese: Tema X]]: uma linha sobre o estado atual do entendimento sobre X.
```

Atualize este arquivo a cada ingest. Ao responder uma pergunta, leia-o primeiro para decidir quais páginas abrir — ele é o mapa da wiki, não um arquivo histórico.

Mantenha as entradas curtas. O índice deve ajudar o agente a decidir onde mergulhar, não duplicar o conteúdo das páginas.

## log.md

Registro cronológico, só de acréscimo (append-only). Use um prefixo consistente em cada entrada, de forma que o arquivo vire algo manipulável com ferramentas unix simples:

```markdown
# Log

## [2026-04-02] ingest | Título do Artigo
Resumo de uma a duas linhas: o que foi processado, quais páginas foram tocadas, o que se destacou.

## [2026-04-03] query | "Pergunta resumida"
O que foi perguntado, que páginas foram consultadas, se a resposta foi arquivada de volta como página nova.

## [2026-04-04] research | pergunta ou lacuna pesquisada
Fontes encontradas, quais foram aceitas para ingest, quais foram descartadas e por quê.

## [2026-04-05] lint | resumo dos achados
Contradições encontradas, páginas órfãs identificadas, ações tomadas ou propostas.

## [2026-04-06] export | html + tex_pdf
Saídas geradas, escopo usado, caminhos dos artefatos e problemas encontrados.
```

Esse formato permite comandos como `grep "^## \[" log.md | tail -5` para ver as últimas entradas, ou filtros por tipo, como `grep "^## \[.*\] ingest" log.md` para ver só os ingests.

Sempre acrescente ao final do arquivo. Nunca reescreva entradas antigas — o log é uma linha do tempo, não um documento vivo como as páginas da wiki.
