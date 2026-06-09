# Operações: ingest, query, research, lint e export

## Preflight

Antes de qualquer operação em uma wiki existente:

1. Leia o esquema local (`AGENTS.md`, `CLAUDE.md`, `WIKI.md` ou `schema.md`) e trate-o como autoridade.
2. Leia `index.md` para entender a organização atual.
3. Leia as entradas recentes de `log.md` para evitar repetir trabalho ou ignorar decisões recentes.
4. Se houver git, verifique o estado da árvore de trabalho antes de editar.

## Ingest

Roteiro sugerido para processar uma fonte nova:

1. **Preserve a fonte bruta** antes de sintetizar. Se o usuário trouxe link, arquivo ou texto colado, salve uma cópia/snapshot em `raw/` quando for viável. Não modifique fontes brutas depois disso.
2. **Leia a fonte inteira** antes de escrever qualquer coisa. Não trabalhe a partir de um resumo de segunda mão nem de um trecho parcial.
   - Para documentos longos, inventarie headings/seções primeiro.
   - Leia no mínimo introdução, método/arquitetura, resultados/evidências, discussão, conclusão e as seções diretamente relevantes.
   - Registre taxonomias, mecanismos, hipóteses, métricas, baselines, resultados, limitações e agenda futura. Abstract é orientação, não ingest completo.
3. **Converse com o usuário sobre os pontos-chave**: o que essa fonte traz de novo, em que ela concorda ou diverge do que já está na wiki, o que merece virar página própria e o que é só um detalhe a registrar de passagem. Essa conversa é o que torna a integração inteligente em vez de mecânica — pule-a e o resultado vira um amontoado de resumos desconexos.
4. **Escreva (ou atualize) a página da fonte** em `wiki/`, com link para o arquivo correspondente em `raw/`. Siga o contrato de `depth.md`: preserve a estrutura intelectual da fonte e distinga demonstrado, proposto, inferido e futuro.
5. **Atualize as páginas de entidades e conceitos afetadas**: procure páginas existentes que essa fonte toca (uma pessoa mencionada, um conceito discutido, um evento relacionado) e revise-as. Crie páginas novas para entidades e conceitos importantes que ainda não têm uma. Em conceitos, explique qual problema a nova fonte observa, qual mecanismo/evidência acrescenta e como confirma, complementa ou diverge das demais. Não apenas acrescente um link. Sinalize explicitamente quando a fonte nova contradiz ou supera algo já registrado.
6. **Mantenha provenance**: afirmações substantivas em páginas de síntese devem apontar para página de fonte, fonte bruta em `raw/`, ou ambas, conforme o esquema local.
7. **Atualize `index.md`**: adicione ou ajuste as entradas para as páginas criadas ou modificadas.
8. **Acrescente uma entrada em `log.md`**, no formato combinado no esquema (por exemplo `## [AAAA-MM-DD] ingest | Título da Fonte`), com uma ou duas linhas sobre o que mudou.
9. **Passe o portão de profundidade**: revise páginas tocadas contra `depth.md`; rode `scripts/lint_depth.py <raiz>` quando disponível. Aprofunde falhas ou rebaixe o status para `stub`/`needs-review`.

Padrão de trabalho recomendado: uma fonte de cada vez, salvo pedido explícito do usuário para processar em lote. Nas primeiras vezes, mostre o que você propõe escrever antes de tocar muitas páginas — isso calibra a relação de confiança e revela o estilo que o usuário prefere, o que torna as próximas rodadas mais fluidas e menos supervisionadas.

## Query

Roteiro sugerido para responder a uma pergunta contra a wiki:

1. **Leia `index.md` primeiro.** Em escalas moderadas, isso já indica quais páginas vale a pena abrir, sem precisar de infraestrutura de busca por embeddings.
2. **Abra as páginas relevantes** e, quando necessário, siga os links cruzados delas para reunir o contexto completo — uma boa wiki tende a ter o caminho de resposta já desenhado nas suas próprias conexões.
3. **Sintetize uma resposta com citações**: aponte para as páginas da wiki (e, quando relevante, para as fontes brutas em `raw/`) que sustentam cada afirmação.
   - Explique mecanismos e relações causais, não apenas conclusões.
   - Compare posições das fontes em dimensões explícitas.
   - Distinga evidência, interpretação da fonte e inferência nova da wiki.
4. **Escolha o formato pela pergunta, não por hábito**: uma pergunta de comparação pede uma tabela; uma pergunta exploratória pode pedir uma página de síntese; um pedido de apresentação pede um deck Marp; dados numéricos podem pedir um gráfico.
5. **Ofereça arquivar a resposta de volta na wiki** quando ela tiver valor de permanência — uma comparação, uma análise, uma conexão nova descoberta na conversa. Se o usuário topar, crie a página, ligue-a às páginas relacionadas e registre em `index.md` e `log.md` (por exemplo como uma entrada do tipo `query` ou `síntese`). É assim que as explorações do usuário também se acumulam, e não só as fontes ingeridas.

Arquive uma resposta sem insistir quando ela for claramente reutilizável: comparação entre fontes, estado atual de uma tese, mapa de conceitos, cronologia, taxonomia, ou decisão de pesquisa. Não arquive respostas triviais, temporárias ou puramente conversacionais.

## Research

Para pesquisa web e enriquecimento de contexto, leia `research.md`. Use este modo para encontrar fontes candidatas, atualizar contexto externo, verificar lacunas e preparar material para ingest.

Resumo:

1. Leia esquema local, `index.md` e `log.md`.
2. Defina a pergunta de pesquisa e o escopo.
3. Busque fontes confiáveis, priorizando fontes primárias.
4. Apresente achados com links, datas e avaliação de confiabilidade.
5. Decida o que vira ingest ou atualização de páginas.
6. Preserve fontes aceitas em `raw/` quando viável, atualize a wiki e registre `log.md`.

## Lint

Roteiro sugerido para uma checagem de saúde:

1. **Percorra a wiki sistematicamente**: leia `index.md` e, dependendo do tamanho da coleção, amostre páginas representativas ou percorra tudo.
2. **Procure por:**
   - Contradições entre páginas (duas páginas afirmando coisas incompatíveis sobre o mesmo fato)
   - Afirmações desatualizadas (uma fonte mais recente já superou o que uma página mais antiga registra)
   - Páginas órfãs (nada na wiki linka para elas)
   - Conceitos mencionados com frequência, mas sem página própria
   - Referências cruzadas óbvias que faltam (a página A menciona um termo que tem página própria, mas não linka para ela)
   - Lacunas de dados que uma busca na web resolveria
   - Páginas marcadas completas que falham o contrato de profundidade: abstract reescrito, definição curta + links, ausência de mecanismo/evidência/limitações, comparação sem implicações
3. **Relate de forma acionável**: organize os achados por tipo e, para cada um, proponha uma ação concreta — criar a página X, ligar A a B, atualizar a afirmação Y na página Z.
4. **Aplique o que for de baixo risco com aprovação simples** (criar um link, criar um stub de página) e **deixe para discussão** o que envolve julgamento de síntese — qual versão de um fato contraditório está correta, o que merece ou não virar página própria.
5. **Sugira próximos passos**: novas perguntas a investigar, novas fontes a procurar, áreas que estão crescendo rápido e podem precisar de reorganização.
6. **Registre o lint em `log.md`** (por exemplo `## [AAAA-MM-DD] lint | resumo dos achados`).
7. **Rode o lint determinístico** quando a skill fornecer `scripts/lint_depth.py`. Ele é triagem: investigue falsos positivos, mas não ignore páginas superficiais.

## Export

Para geração de HTML, TeX ou PDF, leia `export.md`. Use este modo para transformar a wiki em artefatos de leitura, sem mudar a fonte de verdade em markdown.

Resumo:

1. Leia esquema local, `index.md` e `log.md`.
2. Determine formato, escopo e ordem.
3. Gere HTML em `exports/html/` quando o usuário quiser navegação no navegador.
4. Gere TeX/PDF em `exports/tex/` quando o usuário quiser um documento compilável ou PDF navegável por referências internas.
5. Valide links internos, registre problemas e atualize `log.md`.

## Critérios de decisão

- **Página nova**: crie quando o tópico aparece em múltiplas fontes, concentra links futuros, ou é uma unidade natural de pergunta.
- **Stub**: crie quando o tópico é importante, mas a evidência ainda é pequena. Marque como `stub` ou `needs-review` conforme o esquema local.
- **Menção simples**: use quando o tópico é periférico, aparece uma vez, ou não precisa de manutenção própria.
- **Contradição**: registre as versões em conflito e suas fontes. Não apague a versão antiga sem deixar claro que ela foi superada.
- **Baixo risco**: corrigir link, adicionar backlink óbvio, atualizar índice, registrar log e criar stub pequeno podem ser feitos com aprovação simples ou diretamente quando o usuário já pediu a operação.
- **Alto julgamento**: reorganizar categorias, renomear muitas páginas, fundir páginas, descartar conteúdo ou escolher entre fontes contraditórias deve ser discutido com o usuário.
