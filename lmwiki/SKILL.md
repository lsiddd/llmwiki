---
name: lmwiki
description: 'Cria e opera uma "LLM Wiki" — uma base de conhecimento pessoal em markdown que um agente LLM constrói e mantém de forma incremental, cumulativa e interligada a partir de fontes (artigos, papers, transcrições, anotações), em vez de apenas buscar trechos no momento da consulta como num RAG tradicional. Use esta skill quando o usuário invocar /lmwiki, ou pedir explicitamente para montar uma wiki pessoal, de pesquisa ou de equipe mantida por IA; processar ("ingerir") uma fonte nova numa coleção já existente; fazer uma pergunta contra essa base e obter uma síntese com citações; pesquisar na web para enriquecer contexto e encontrar fontes relevantes; rodar uma checagem de saúde ("lint") numa coleção de páginas markdown interligadas; ou exportar a wiki como site HTML navegável, TeX ou PDF compilado.'
---

# LMWiki

## Ideia central

A maioria das interações entre LLMs e documentos segue o padrão RAG: o usuário envia um conjunto de arquivos, o modelo recupera trechos relevantes a cada pergunta e gera uma resposta. Isso funciona, mas o conhecimento nunca se acumula: a cada pergunta nova, o modelo monta os fragmentos relevantes do zero, sem lembrança do que já sintetizou antes.

A LMWiki propõe outra coisa. Em vez de só recuperar trechos brutos no momento da consulta, o agente constrói e mantém uma wiki persistente: uma coleção estruturada e interligada de páginas em markdown que fica entre o usuário e as fontes brutas. Quando chega uma fonte nova, o agente não apenas a indexa para depois. Ele lê, extrai o que importa e integra à wiki existente: atualiza páginas de entidades, revisa sínteses de tópicos, sinaliza onde dados novos contradizem afirmações antigas. O conhecimento é compilado uma vez e mantido atualizado, não rederivado a cada pergunta.

O usuário raramente escreve a wiki: cura fontes, dirige a investigação, faz as perguntas certas. O trabalho de manutenção (resumir, cruzar referências, arquivar, manter consistência entre dezenas de páginas) é do agente.

## As três camadas

Toda LMWiki tem três componentes principais, mais uma camada opcional de saída:

1. **Fontes brutas** (`raw/`): a coleção curada de documentos-fonte (artigos, papers, transcrições, imagens, dados). São imutáveis — o agente lê delas, mas nunca as modifica. É a fonte da verdade.
2. **A wiki** (`wiki/`): o diretório de páginas markdown geradas pelo agente (resumos, páginas de entidades e conceitos, comparações, sínteses). O agente é dono desta camada inteira: cria páginas, atualiza quando chegam fontes novas, mantém referências cruzadas e consistência. O usuário lê; o agente escreve.
3. **O esquema** (`AGENTS.md`, `CLAUDE.md`, `WIKI.md` ou `schema.md` dentro do diretório da wiki): documento que descreve a estrutura, as convenções e os fluxos de trabalho específicos dessa wiki. É o que transforma o agente num mantenedor disciplinado em vez de num chatbot genérico, e evolui em conjunto com o usuário ao longo do tempo.
4. **Pesquisa auxiliar** (web ou outras fontes externas): usada para descobrir contexto, preencher lacunas e encontrar fontes candidatas. Nada entra na wiki sem fonte rastreável e decisão explícita de integração.
5. **Saídas geradas** (`exports/`, opcional): artefatos derivados da wiki, como um site HTML navegável ou um projeto TeX/PDF. Essa camada nunca é fonte de verdade; quando a wiki muda, gere novamente.

Cada wiki é diferente — o domínio (pessoal, pesquisa, leitura de um livro, equipe...), os tipos de página, as convenções de nomenclatura e até as ferramentas variam conforme a necessidade. Não existe um esquema universal correto: existe o esquema que esse usuário, nesse domínio, decide em conjunto com o agente.

## Regra de autoridade

Em qualquer wiki existente, leia primeiro o esquema local da wiki. A skill genérica orienta o método; o esquema local governa a execução. Se houver conflito entre esta skill e o esquema local, siga o esquema local e mencione o conflito ao usuário quando ele afetar uma decisão relevante.

## Preflight obrigatório

Antes de escolher Bootstrap, Ingest, Query, Research, Lint ou Export:

1. Localize a raiz da wiki indicada pelo usuário ou inferida pelo diretório atual. Procure `raw/`, `wiki/`, `index.md`, `log.md` e um arquivo de esquema (`AGENTS.md`, `CLAUDE.md`, `WIKI.md` ou `schema.md`).
2. Se existir um esquema local, leia-o antes de qualquer edição ou resposta substantiva.
3. Se existirem `index.md` e `log.md`, leia `index.md` e as entradas recentes de `log.md` para entender a estrutura e o histórico recente.
4. Se a wiki estiver em um repositório git, verifique o estado do trabalho antes de editar. Não reverta alterações existentes sem pedido explícito do usuário.
5. Identifique o modo de operação e diga ao usuário, em uma frase curta, o que vai fazer. Se a intenção estiver ambígua, pergunte.

## Como decidir o modo

Ao ser invocado com `/lmwiki`, primeiro determine em que estado o usuário está:

- **Não existe wiki ainda** (não há `raw/`, `wiki/`, `index.md`, `log.md` ou arquivo de esquema no diretório indicado): proponha o modo **Bootstrap**.
- **Existe wiki e o usuário está trazendo material novo** (um link, um arquivo, um trecho colado, "processa isso aí"): modo **Ingest**.
- **Existe wiki e o usuário está fazendo uma pergunta sobre o conteúdo dela**: modo **Query**.
- **Existe wiki e o usuário pede para enriquecer contexto, pesquisar na web, encontrar fontes, atualizar lacunas externas, verificar estado atual ou descobrir material relevante ao tema**: modo **Research**.
- **Existe wiki e o usuário pede uma checagem de saúde, revisão geral, "dá uma olhada na wiki"**: modo **Lint**.
- **Existe wiki e o usuário pede saída navegável, HTML, TeX, LaTeX, PDF, livro, documentação estática ou compilação da base inteira**: modo **Export**.

Se não estiver claro, pergunte. Não assuma — o custo de uma pergunta de esclarecimento é baixo comparado ao custo de processar a fonte errada ou escrever em quinze páginas pelo motivo errado.

## Modo 1: Bootstrap (criar uma wiki nova)

Não existe um layout único certo: o objetivo desta etapa é uma conversa que produz uma estrutura sob medida para o domínio do usuário. Leia `references/bootstrap.md` para o roteiro completo de entrevista e os templates de arquivo. Resumo do fluxo:

1. Entenda o domínio e o objetivo — o que o usuário quer acumular e por quê (pesquisa, projeto pessoal, leitura, equipe, due diligence, hobby...).
2. Proponha a estrutura de diretórios (`raw/`, `wiki/`, `index.md`, `log.md`, arquivo de esquema) e ajuste conforme o gosto do usuário.
3. Escreva o arquivo de esquema (`AGENTS.md` para Codex, `CLAUDE.md` para Claude Code, ou outro nome escolhido pelo usuário) em colaboração com o usuário: tipos de página, convenções de nomenclatura e frontmatter, estilo de links, tratamento de contradições, fluxos de ingest/query/lint específicos desse domínio.
4. Crie `index.md` e `log.md` a partir dos templates (ver `references/conventions.md`).
5. Defina, se o usuário quiser, como pesquisas web devem ser usadas: fontes preferidas, fontes proibidas, critérios de confiabilidade, quando preservar snapshots em `raw/` e quando pedir aprovação antes de integrar.
6. Defina, se o usuário quiser, saídas geradas como site HTML e/ou TeX/PDF: diretórios de destino, ordem das páginas, estilo visual, ferramenta de compilação e o que entra ou fica fora da exportação.
7. Sugira, sem insistir, as dicas operacionais relevantes ao caso: Obsidian como interface de leitura, Web Clipper, anexos locais, Marp, Dataview, versionamento via git.

Termine o bootstrap com uma wiki vazia mas funcional, e um esquema que o agente vai seguir — e revisar — dali em diante.

## Modo 2: Ingest (processar uma fonte nova)

Leia `references/operations.md` para o roteiro detalhado. Princípios que guiam esse modo:

- **Processe uma fonte de cada vez**, salvo pedido explícito do usuário para processar em lote. Isso preserva o envolvimento dele: ele lê os resumos, confere as atualizações, orienta o que merece destaque. Processar em lote é possível, mas reduz a supervisão e deve ser escolha consciente do usuário, não um atalho seu.
- **Preserve a fonte bruta antes de sintetizar**: se o usuário trouxer link, arquivo ou texto colado, mantenha uma cópia/snapshot em `raw/` sempre que for viável. A página de fonte em `wiki/` deve apontar para esse item em `raw/`.
- **Uma fonte pode tocar de dez a quinze páginas**: resumo da fonte, páginas de entidades e conceitos relacionados, índice, log. Não hesite em tocar muitos arquivos — essa é justamente a vantagem de delegar a manutenção a um agente que não se cansa de atualizar referências cruzadas.
- **Discuta com o usuário antes de escrever**: o que essa fonte traz de novo, o que ela confirma, o que ela contradiz. Essa conversa não é burocracia — é o que decide o que vale a pena registrar e como.
- **Mantenha rastreabilidade**: afirmações substantivas em páginas de síntese devem apontar para uma página de fonte ou para a fonte bruta correspondente.
- Ao final, **sempre** atualize `index.md` (cataloga a página nova ou revisada) e acrescente uma entrada em `log.md` (registra o que aconteceu).

## Modo 3: Query (consultar a wiki)

Leia `references/operations.md` para o roteiro detalhado. Princípios:

- **Comece pelo índice** (`index.md`). Em escalas moderadas (algumas dezenas a centenas de páginas), ler o índice primeiro e depois mergulhar nas páginas relevantes funciona bem e evita a necessidade de infraestrutura de busca por embeddings.
- **Sintetize com citações**: aponte para as páginas da wiki e, quando fizer sentido, para as fontes brutas originais que sustentam cada afirmação.
- **O formato da resposta depende da pergunta, não de hábito**: pode ser uma página markdown, uma tabela comparativa, um deck de slides (Marp), um gráfico, um canvas.
- **Boas respostas merecem virar páginas da wiki**: uma comparação que o usuário pediu, uma análise, uma conexão descoberta na conversa — tudo isso tem valor de permanência. Ofereça arquivar de volta na wiki o que for valioso, em vez de deixar se perder no histórico do chat. É assim que as explorações do usuário também se acumulam, e não só as fontes ingeridas.

## Modo 4: Research (pesquisar e enriquecer contexto)

Leia `references/research.md` para o roteiro detalhado. Princípios:

- **Pesquise para descobrir, não para poluir a wiki**: resultados web são candidatos a fonte e contexto, não conhecimento integrado automaticamente.
- **Priorize fontes primárias e confiáveis**: papers, documentação oficial, relatórios originais, páginas institucionais, entrevistas primárias e dados publicados. Use fontes secundárias para orientação, não como base final quando uma fonte primária existe.
- **Preserve e cite**: quando uma fonte web for usada para atualizar a wiki, preserve link, data de acesso e, quando viável, snapshot/nota em `raw/`.
- **Separe achados preliminares de integração**: primeiro apresente o que a pesquisa encontrou; depois decida com o usuário o que deve virar ingest ou atualização de páginas.
- **Atualidade importa**: quando o assunto é temporalmente instável, registre datas concretas e prefira fontes recentes e verificáveis.
- Ao final, registre a pesquisa em `log.md`, mesmo que nada seja integrado.

## Modo 5: Lint (checagem de saúde da wiki)

Leia `references/operations.md` para o roteiro completo. O que procurar:

- Contradições entre páginas
- Afirmações desatualizadas que fontes mais recentes já superaram
- Páginas órfãs (sem links de entrada)
- Conceitos importantes mencionados repetidamente, mas sem página própria
- Referências cruzadas óbvias que faltam
- Lacunas de dados que uma busca na web poderia preencher

Ao final de um lint, não apenas relate: sugira ao usuário novas perguntas a investigar e novas fontes a procurar. Aplique correções de baixo risco (criar um link, criar um stub de página) com aprovação simples do usuário, e deixe para discussão as decisões que envolvem julgamento de síntese.

## Modo 6: Export (gerar HTML, TeX ou PDF)

Leia `references/export.md` para o roteiro detalhado. Princípios:

- **A wiki markdown continua sendo a fonte de verdade**. `exports/` é saída gerada; não corrija conhecimento editando HTML, TeX ou PDF.
- **HTML** deve gerar páginas navegáveis no navegador, com links internos relativos, índice, backlinks quando útil e navegação sem depender de servidor.
- **TeX/PDF** deve gerar um projeto compilável, com capítulos/seções derivados da estrutura da wiki, `\label{...}` estáveis e links internos via `hyperref` para navegar dentro do PDF.
- **Respeite a ordem e escopo definidos no esquema local**. Se não houver convenção, proponha uma ordem baseada no `index.md`: sínteses/visão geral primeiro, depois conceitos, entidades e fontes.
- Ao final, registre a exportação em `log.md` e informe os caminhos dos artefatos gerados.

## index.md e log.md: convenções

Os dois arquivos têm propósitos diferentes e não devem ser confundidos:

- **`index.md`** é orientado a conteúdo: um catálogo de tudo que existe na wiki, organizado por categoria (entidades, conceitos, fontes, sínteses...), com link, resumo de uma linha e, opcionalmente, metadados (data, contagem de fontes). Atualize a cada ingest. É o primeiro arquivo a consultar ao responder uma pergunta.
- **`log.md`** é cronológico e só de acréscimo (append-only): um registro do que aconteceu e quando — ingests, queries, passes de lint. Use um prefixo consistente em cada entrada, por exemplo `## [2026-04-02] ingest | Título do Artigo`, de forma que o log vire algo manipulável com ferramentas unix simples (`grep "^## \[" log.md | tail -5` traz as últimas cinco entradas).

Veja `references/conventions.md` para os templates completos.

## Critérios de decisão

- **Crie página nova** quando um conceito, entidade, fonte ou síntese aparecer como assunto recorrente, receber múltiplas referências, ou for necessário para responder perguntas futuras.
- **Crie um stub** quando o tópico é claramente importante, mas ainda há pouco material. Marque como `status: stub` ou equivalente no frontmatter se o esquema local permitir.
- **Apenas mencione** quando o tópico é detalhe contextual, aparece uma vez, ou ainda não justifica manutenção própria.
- **Marque contradição** quando uma fonte nova desafia uma afirmação anterior. Não apague a afirmação antiga sem registrar a mudança de evidência, salvo quando o esquema local mandar corrigir diretamente.
- **Aplique sem interromper** edições de baixo risco, como corrigir links quebrados, adicionar backlinks óbvios, atualizar `index.md` e registrar `log.md`.
- **Peça aprovação** para reorganizações de estrutura, renomeações em massa, sínteses interpretativas fortes, descarte de páginas e decisões sobre qual fonte contraditória deve prevalecer.

## Dicas operacionais (ofereça quando fizer sentido — não empurre)

- **Obsidian** como interface de leitura: o usuário acompanha em tempo real enquanto o agente edita. A visão de grafo é a melhor forma de enxergar a forma da wiki — o que está conectado, o que é hub, o que é órfão.
- **Obsidian Web Clipper** converte artigos da web em markdown — útil para alimentar `raw/`.
- **Baixar imagens localmente**: configurar uma pasta fixa de anexos evita depender de URLs que quebram. Vale lembrar o usuário de que o agente não lê markdown com imagens inline numa única passada — primeiro lê o texto, depois visualiza as imagens referenciadas separadamente.
- **Marp** para gerar decks de slides a partir do conteúdo da wiki; **Dataview** para consultas dinâmicas sobre o frontmatter das páginas.
- **git**: a wiki é só um repositório de arquivos markdown. Histórico de versões, branches e colaboração vêm de graça.
- **HTML/TeX/PDF** como saídas geradas: um site estático facilita leitura no navegador; um PDF compilado em TeX facilita leitura linear, sumário, referências internas e distribuição.
- **Pesquisa web** para enriquecer contexto: útil para encontrar fontes novas e preencher lacunas, mas deve entrar na wiki pelo mesmo padrão de rastreabilidade de qualquer fonte curada.
- **Ferramentas de busca dedicadas** (como [qmd](https://github.com/tobi/qmd)) só ficam necessárias quando a wiki cresce além do ponto em que o índice basta. Não introduza complexidade de busca antes que o usuário sinta a necessidade.

## Por que isso funciona

A parte tediosa de manter uma base de conhecimento não é ler ou pensar — é a burocracia: atualizar referências cruzadas, manter resumos em dia, registrar quando dados novos contradizem afirmações antigas, manter consistência entre dezenas de páginas. Pessoas abandonam wikis porque o custo de manutenção cresce mais rápido que o valor entregue. Um agente não se cansa, não esquece de atualizar uma referência cruzada e consegue tocar quinze arquivos numa só passada. A wiki se mantém porque o custo de mantê-la é próximo de zero.

O trabalho do usuário é curar fontes, dirigir a análise, fazer boas perguntas e pensar no que tudo isso significa. O trabalho do agente é o resto.
