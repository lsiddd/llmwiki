# LMWiki Skill

Skill para Codex que cria e opera uma **LLM Wiki**: uma base de conhecimento em markdown mantida por agente, cumulativa, interligada e rastreável. A ideia é transformar fontes brutas em páginas persistentes de wiki, em vez de redescobrir conhecimento do zero a cada pergunta.

## O Que Ela Faz

- **Bootstrap**: cria uma wiki nova com `raw/`, `wiki/`, `index.md`, `log.md` e um esquema local de operação.
- **Ingest**: preserva fontes brutas, cria páginas de fonte, atualiza conceitos/entidades/sínteses e mantém provenance.
- **Query**: responde perguntas contra a wiki com citações e pode arquivar respostas duráveis.
- **Research**: pesquisa na web para enriquecer contexto e encontrar fontes candidatas sem poluir a wiki automaticamente.
- **Lint**: encontra contradições, afirmações antigas, páginas órfãs, links faltando e lacunas.
- **Export**: gera site HTML navegável ou projeto TeX/PDF com referências internas.

## Estrutura Do Repositório

```text
.
├── lmwiki/                 # fonte editável da skill
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── lmwiki.skill            # pacote pronto para instalar
├── docs/llm-wiki.md        # nota conceitual original
└── scripts/package.sh      # recria lmwiki.skill a partir de lmwiki/
```

## Instalação Local

A partir deste repositório:

```bash
rm -rf ~/.codex/skills/lmwiki
unzip -q lmwiki.skill -d ~/.codex/skills
```

Reinicie o Codex depois da instalação para ele carregar a skill.

## Recriar O Pacote

Depois de editar arquivos em `lmwiki/`, gere novamente o pacote:

```bash
scripts/package.sh
```

O script escreve `lmwiki.skill` na raiz do repositório e valida o zip.

## Publicação

- Mantenha `lmwiki/` como fonte de verdade da skill.
- Mantenha `lmwiki.skill` versionado se quiser permitir download direto do artefato empacotado.
- Adicione um `LICENSE` antes de distribuição pública se quiser definir explicitamente permissões de reutilização.
