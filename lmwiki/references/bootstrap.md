# Bootstrap: roteiro de entrevista e templates

## Perguntas para entender o domínio

Não pule essa conversa — a estrutura certa depende inteiramente das respostas, e uma wiki montada sem essa base costuma exigir retrabalho mais tarde.

1. **Sobre o que é essa wiki?** (pesquisa num tema, autoconhecimento, leitura de um livro ou série, due diligence, base de equipe, hobby, planejamento de viagem...)
2. **Que tipos de fonte vão alimentá-la?** (artigos, papers, transcrições de podcast, anotações pessoais, threads de Slack, e-mails, imagens...) Isso determina se há necessidade de lidar com imagens, áudio transcrito, PDFs etc.
3. **Que tipos de página fazem sentido?** Pense em categorias recorrentes: pessoas/entidades, conceitos, eventos, lugares, comparações, sínteses temáticas. Uma wiki de pesquisa científica pede páginas diferentes de uma wiki sobre um romance.
4. **Qual o ritmo esperado?** Uma fonte por dia? Uma leva de cinquenta de uma vez? Isso influencia se o ingest deve ser supervisionado fonte a fonte ou pode ser feito em lote.
5. **O usuário vai navegar a wiki com Obsidian** (ou outro app de markdown interligado)? Se sim, vale configurar frontmatter, pastas de anexos e convenções compatíveis com os plugins que ele usa (Dataview, Excalidraw etc.).
6. **Qual agente vai operar a wiki na maior parte do tempo?** Use `AGENTS.md` para Codex, `CLAUDE.md` para Claude Code, ou outro nome se o usuário preferir. O importante é que o arquivo escolhido seja fácil de encontrar em sessões futuras.
7. **A wiki pode usar pesquisa web para enriquecer contexto?** Se sim, defina fontes preferidas, fontes proibidas, critérios de confiabilidade, nível de atualidade necessário e se resultados web precisam de aprovação antes de entrar na wiki.
8. **Quais saídas geradas o usuário quer?** Site HTML navegável, projeto TeX/PDF, ambos ou nenhum por enquanto. Pergunte também se a exportação deve incluir fontes processadas, apenas sínteses/conceitos, ou a wiki inteira.

## Estrutura de diretórios sugerida (ponto de partida, não dogma)

```
minha-wiki/
├── AGENTS.md          # ou CLAUDE.md/WIKI.md/schema.md: como operar essa wiki
├── index.md           # catálogo de tudo
├── log.md             # registro cronológico
├── raw/               # fontes brutas, imutáveis
│   └── assets/        # imagens baixadas localmente (opcional)
├── exports/           # saídas geradas, recriáveis
│   ├── html/          # site estático navegável (opcional)
│   └── tex/           # projeto TeX/PDF compilável (opcional)
└── wiki/
    ├── entidades/
    ├── conceitos/
    └── sinteses/
```

Adapte livremente: algumas wikis não precisam de subpastas dentro de `wiki/`; outras vão querer separar por projeto, por ano ou por fonte. A estrutura deve refletir como o usuário pensa sobre o domínio, não uma convenção genérica copiada daqui.

## Template do arquivo de esquema

Esse é o documento mais importante de toda a wiki: é ele que faz o agente operá-la de forma disciplinada em sessões futuras, mesmo sem lembrança da conversa de bootstrap. Escreva-o em conjunto com o usuário, não para ele — a colaboração na escrita já é parte do processo de descobrir as convenções certas. Um esqueleto de partida:

```markdown
# Esquema da wiki: [nome/tema]

## Sobre essa wiki
[uma ou duas frases sobre o domínio e o objetivo]

## Estrutura
- `raw/`: fontes brutas, nunca editar
- `wiki/`: páginas mantidas pelo agente
  - [categorias de página específicas desse domínio, com convenção de nome de arquivo]
- `index.md`: catálogo de páginas
- `log.md`: registro cronológico, formato `## [AAAA-MM-DD] tipo | título`
- `exports/`: saídas geradas; não é fonte de verdade

## Convenções de página
- Frontmatter: [quais campos usar — tipo, status, tags, data, fontes relacionadas...]
- Como nomear arquivos: [slug, prefixo de data etc.]
- Como linkar: [estilo de wikilink `[[Página]]`, quando criar um link versus apenas mencionar em texto]
- Como citar fontes: [quando linkar para página de fonte, fonte bruta em `raw/`, ou ambas]

## Frontmatter mínimo sugerido
Use ou adapte:

```yaml
---
type: conceito | entidade | fonte | sintese
status: draft | stable | needs-review | stub
sources:
  - raw/exemplo.md
updated: AAAA-MM-DD
---
```

## Fluxo de ingest
[passos específicos desse domínio: como preservar a fonte em `raw/`, que tipos de página costumam ser tocados por uma fonte nova, o que perguntar ao usuário antes de escrever, etc.]

## Fluxo de query
[formatos de resposta preferidos, convenção de citação, quando arquivar uma resposta de volta na wiki]

## Fluxo de research
- Quando pesquisar na web: [lacunas, atualização, descoberta de fontes, verificação externa]
- Fontes preferidas: [papers, documentação oficial, sites institucionais, jornais específicos etc.]
- Fontes evitadas/proibidas: [fóruns, redes sociais, blogs sem autoria, conteúdo gerado por IA etc.]
- Como registrar achados: [nota temporária, página de fonte, atualização direta, lista de candidatos]
- Como integrar: [sempre pedir aprovação, integrar automaticamente fontes primárias, preservar snapshot em `raw/` etc.]

## Fluxo de lint
[com que frequência rodar, o que esse domínio em particular tende a degradar — contradições entre fontes? páginas órfãs? dados que ficam desatualizados rápido?]

## Fluxo de export
- Saídas desejadas: [html, tex_pdf]
- Escopo: [wiki inteira, apenas sínteses/conceitos, excluir fontes processadas etc.]
- Ordem: [seguir `index.md`, ordem manual, por data, por categoria]
- HTML: gerar em `exports/html/`, com links relativos entre páginas e `index.html`
- TeX/PDF: gerar em `exports/tex/`, com `wiki.tex`, labels estáveis e navegação via `hyperref`
- Compilação: [latexmk, tectonic, pdflatex, ou apenas gerar TeX]

## Critérios de decisão
- Quando criar página nova versus só mencionar
- Quando criar stub
- Quando pedir aprovação antes de reorganizar
- Como registrar contradições e mudanças de evidência
```

Esse arquivo deve crescer e mudar conforme o usuário e o agente descobrem o que funciona na prática. Não o escreva como se fosse definitivo na primeira versão — apresente-o como um rascunho vivo, e diga isso ao usuário explicitamente, para que ele saiba que pode (e deve) pedir ajustes mais adiante.

## index.md e log.md iniciais

Ver `conventions.md` para os templates desses dois arquivos.

## Ao final do bootstrap

Confirme com o usuário que a estrutura faz sentido antes de criar os arquivos. Depois de criá-los, ofereça um resumo do que foi montado e do que esperar das próximas sessões — por exemplo, "da próxima vez que você trouxer um artigo, eu vou seguir o fluxo de ingest descrito no esquema: preservar a fonte em raw, ler, conversar sobre os pontos-chave, atualizar as páginas afetadas e registrar no log". Isso ajuda o usuário a calibrar expectativas e a saber o que pedir.
