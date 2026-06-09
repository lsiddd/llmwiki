# LMWiki Skill

Skill para agentes que leem `SKILL.md`, incluindo **Codex** e **Claude Code**. Ela cria e opera uma **LLM Wiki**: uma base de conhecimento em markdown mantida por agente, cumulativa, interligada e rastreável. A ideia é transformar fontes brutas em páginas persistentes de wiki, em vez de redescobrir conhecimento do zero a cada pergunta.

## O Que Ela Faz

- **Bootstrap**: cria uma wiki nova com `raw/`, `wiki/`, `index.md`, `log.md` e um esquema local de operação.
- **Ingest**: preserva fontes brutas, cria páginas de fonte, atualiza conceitos/entidades/sínteses e mantém provenance.
- **Query**: responde perguntas contra a wiki com citações e pode arquivar respostas duráveis.
- **Research**: pesquisa na web para enriquecer contexto e encontrar fontes candidatas sem poluir a wiki automaticamente.
- **Lint**: encontra contradições, afirmações antigas, páginas órfãs, links faltando e lacunas.
- **Depth lint**: rejeita páginas superficialmente "completas" e exige mecanismo, evidência, limitações e relações explicadas.
- **Export**: gera site HTML navegável ou projeto TeX/PDF com referências internas.

## Estrutura Do Repositório

```text
.
├── lmwiki/                 # fonte editável da skill
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   └── scripts/lint_depth.py
├── evals/evals.json        # prompts para avaliar qualidade da skill
├── lmwiki.skill            # pacote zip pronto para instalar
├── docs/llm-wiki.md        # nota conceitual original
└── scripts/package.sh      # recria lmwiki.skill a partir de lmwiki/
```

## Instalação

### Codex

Instale a skill em `~/.codex/skills/lmwiki`:

```bash
rm -rf ~/.codex/skills/lmwiki
unzip -q lmwiki.skill -d ~/.codex/skills
```

Reinicie o Codex depois da instalação.

### Claude Code

Instale a mesma pasta da skill em `~/.claude/skills/lmwiki`:

```bash
rm -rf ~/.claude/skills/lmwiki
mkdir -p ~/.claude/skills
cp -a lmwiki ~/.claude/skills/lmwiki
```

Reinicie o Claude Code depois da instalação. Em projetos específicos, você também pode copiar `lmwiki/` para uma pasta de skills do próprio projeto, se esse for o padrão configurado no seu ambiente.

### Outros Agentes

Use `lmwiki/SKILL.md` como arquivo principal da skill e mantenha a pasta `lmwiki/references/` ao lado dele. A skill foi escrita de forma neutra: o esquema local da wiki pode ser `AGENTS.md`, `CLAUDE.md`, `WIKI.md` ou `schema.md`.

## Recriar O Pacote

Depois de editar arquivos em `lmwiki/`, gere novamente o pacote:

```bash
scripts/package.sh
```

O script escreve `lmwiki.skill` na raiz do repositório e valida o zip.

## Padrão De Profundidade

A skill trata profundidade como parte da correção da wiki. Uma página de conceito não pode ser apenas definição + links; ela deve explicar mecanismos, variantes, métricas, limitações e a contribuição específica das fontes. Páginas de fonte devem refletir o corpo completo, não apenas o abstract.

Para fazer uma triagem determinística:

```bash
python lmwiki/scripts/lint_depth.py /caminho/para/wiki
```

O lint usa heurísticas e não substitui revisão editorial, mas impede que páginas obviamente rasas sejam silenciosamente tratadas como completas.
