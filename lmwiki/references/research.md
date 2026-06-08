# Research: pesquisa web e enriquecimento de contexto

Use este modo quando o usuário pedir para pesquisar na web, enriquecer contexto, encontrar fontes novas, verificar atualização externa, preencher lacunas ou descobrir material relevante ao assunto da wiki.

## Princípios

- Pesquisa web é descoberta e triagem. Ingest é integração.
- A wiki continua baseada em fontes rastreáveis. Não integre afirmações web sem URL, autoria/organização quando disponível, data de acesso e avaliação mínima de confiabilidade.
- Priorize fontes primárias: papers, documentação oficial, relatórios originais, dados publicados, páginas institucionais, entrevistas primárias, repositórios oficiais.
- Use fontes secundárias para mapear o tema, mas procure a fonte primária antes de atualizar páginas da wiki.
- Em assuntos temporais, registre datas concretas: data de publicação, data do evento e data de acesso.
- Se a pesquisa envolver tema médico, jurídico, financeiro, segurança ou decisões de alto impacto, trate como alta precisão: use fontes primárias/autoridades e deixe limitações explícitas.

## Preflight de research

1. Leia o esquema local, `index.md` e entradas recentes de `log.md`.
2. Identifique a lacuna: atualização factual, busca de fontes, contexto histórico, definição, comparação, estado da arte, controvérsia, ou verificação de contradição.
3. Defina escopo e critérios: período, idioma, região, tipo de fonte, fontes proibidas, profundidade desejada.
4. Se o usuário não definiu escopo e a decisão muda muito o resultado, pergunte. Caso contrário, faça uma suposição conservadora e registre-a.

## Fluxo

1. **Buscar**: pesquise com consultas específicas e varie termos quando necessário.
2. **Triar**: classifique resultados em fonte primária, fonte secundária confiável, contexto útil, ou descartar.
3. **Verificar**: compare datas, autoria, domínio, método e possíveis conflitos.
4. **Sintetizar achados preliminares**: apresente ao usuário o que foi encontrado, com links e motivo de relevância.
5. **Decidir integração**: indique quais fontes devem virar ingest, quais só informam contexto e quais foram descartadas.
6. **Preservar fontes aceitas**: quando viável, salve snapshot, markdown, bibliografia ou nota de fonte em `raw/`.
7. **Atualizar wiki**: se o usuário aprovar ou se o esquema permitir, atualize páginas afetadas, crie páginas de fonte, ajuste `index.md` e registre `log.md`.

## Formato de achados

Use uma forma curta e auditável:

```markdown
## Achados preliminares

- [Título](URL) — tipo: fonte primária/secundária/contexto. Publicado em AAAA-MM-DD, acessado em AAAA-MM-DD. Relevância: ...
- [Título](URL) — tipo: descartar. Motivo: fonte sem autoria, duplicada, antiga, ou menos confiável que fonte primária.

## Recomendação de integração

- Ingerir: [fontes que devem entrar em `raw/` e gerar página de fonte]
- Atualizar: [páginas da wiki afetadas]
- Não integrar: [contexto útil mas fraco, redundante ou temporário]
```

## Critérios de confiabilidade

- **Alta**: fonte primária, instituição reconhecida, paper revisado, documentação oficial, dataset original, relatório metodologicamente claro.
- **Média**: veículo confiável citando fontes primárias, revisão técnica assinada, livro ou artigo com referências claras.
- **Baixa**: post sem autoria, conteúdo sem data, agregador, texto promocional, fonte que não cita evidência, conteúdo gerado por IA ou fórum sem verificação.

## Integração na wiki

Quando uma fonte pesquisada for aceita:

- Crie ou atualize uma página de fonte com metadados: URL, título, autoria/organização, publicação, acesso, tipo de fonte e confiabilidade.
- Atualize páginas de conceitos/entidades/sínteses afetadas com links para a fonte.
- Se a fonte contradiz a wiki, registre a contradição em vez de sobrescrever silenciosamente.
- Atualize `index.md`.
- Acrescente uma entrada em `log.md`, por exemplo:

```markdown
## [AAAA-MM-DD] research | lacuna pesquisada
Encontradas 8 fontes, 3 aceitas para ingest, 2 usadas como contexto, 3 descartadas. Páginas afetadas: [[X]], [[Y]].
```

## Quando não integrar

Não integre quando a fonte é fraca, redundante, temporária, fora de escopo, ou quando a informação é incerta demais. Nesse caso, registre a recomendação ao usuário e deixe como candidato futuro, não como fato da wiki.
