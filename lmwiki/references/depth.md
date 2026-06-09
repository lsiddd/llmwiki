# Contrato de profundidade

Use este documento ao criar, revisar ou validar páginas. O objetivo não é inflar texto: é produzir uma base explicativa, comparativa e auditável que substitua a necessidade de reler todas as fontes para compreender o tema.

## Regra central

Uma página completa precisa responder às perguntas relevantes entre:

1. **O que é?** Definição operacional e fronteiras do conceito.
2. **Por que importa?** Problema, motivação e contexto.
3. **Como funciona?** Componentes, mecanismo, fluxo, arquitetura ou processo.
4. **Quais variantes existem?** Taxonomia e diferenças.
5. **Como decidir?** Trade-offs, condições de uso e critérios de escolha.
6. **Como avaliar?** Evidências, métricas, hipóteses, baselines e resultados.
7. **Onde falha?** Limitações, riscos, contradições e casos adversos.
8. **Como se conecta?** Dependências causais e contribuição específica das fontes.
9. **O que ainda falta?** Lacunas e agenda de pesquisa.

Nem toda página exige nove seções literais. Ela exige conteúdo equivalente, adequado ao domínio.

## Anti-padrões que reprovam uma página

- definição de um parágrafo seguida por uma lista de links;
- resumo que apenas reescreve o abstract;
- seção "como aparece na coleção" sem explicar como cada fonte contribui;
- três tensões genéricas copiadas para conceitos diferentes;
- página de síntese que enumera fontes sem compará-las;
- afirmações fortes sem fonte, evidência ou qualificação;
- página marcada `stable`/`completo` sem limitações ou perguntas abertas;
- comprimento obtido por colagem extensa da fonte, sem síntese.

## Páginas de fonte

Uma página de fonte completa deve conter:

- metadados e link para a fonte bruta;
- pergunta/problema central;
- tese, abordagem ou método;
- mapa da estrutura intelectual da fonte, cobrindo as seções substantivas;
- mecanismo, arquitetura, taxonomia ou algoritmo em detalhe;
- evidências: configuração, métricas, baselines e resultados quando existirem;
- distinção explícita entre demonstrado, proposto, inferido e futuro;
- limitações, hipóteses e ameaças à validade;
- contribuição para conceitos e sínteses existentes;
- divergências ou complementaridades com outras fontes.

Leia a fonte inteira. Em papers longos, inventarie headings e leia introdução, método/arquitetura, resultados, discussão, conclusão e seções diretamente relevantes. Não baseie a página apenas no abstract.

## Páginas de conceito

Uma página de conceito completa deve conter:

- definição operacional e fronteiras: o que entra e o que não entra;
- componentes e mecanismo interno;
- taxonomia/variantes;
- decisões de projeto e trade-offs;
- métricas e formas de avaliação;
- falhas, riscos e limitações;
- relação com conceitos vizinhos;
- comparação fonte a fonte.

Na comparação fonte a fonte, explique pelo menos:

- qual problema a fonte observa;
- qual mecanismo, evidência ou perspectiva acrescenta;
- como confirma, complementa ou diverge das demais.

## Páginas de síntese

Uma síntese completa deve:

- formular uma tese ou modelo mental próprio, fundamentado;
- comparar fontes em dimensões explícitas;
- explicar convergências, divergências e dependências;
- conectar mecanismo a consequência;
- distinguir evidência das fontes de inferência da wiki;
- identificar lacunas e propor perguntas/experimentos verificáveis.

Use tabelas quando a pergunta for comparativa, mas explique as implicações da tabela em prosa.

## Entidades, eventos e páginas factuais

Mesmo páginas factuais devem explicar relevância para a wiki, relações importantes, cronologia ou contexto, fontes e incertezas. Não transforme cada menção periférica em uma página.

## Profundidade proporcional

Profundidade não significa tamanho uniforme:

- `stub`: pode ser curto, mas deve dizer claramente o que falta.
- fonte curta: cubra integralmente o que ela realmente oferece.
- survey/paper longo: preserve taxonomias, mecanismos e diferenças internas.
- conceito central com muitas fontes: deve ser mais rico que conceitos periféricos.

Contagem de palavras é apenas um sinal de triagem. O critério real é cobertura explicativa.

## Portão de conclusão

Antes de marcar uma página como completa:

1. Verifique se ela ultrapassa os anti-padrões.
2. Confirme que links para fontes vêm acompanhados da relação explicada.
3. Confirme que mecanismo/evidência/limitações aparecem quando aplicáveis.
4. Confirme que o leitor entende diferenças entre fontes sem abri-las todas.
5. Rode `scripts/lint_depth.py <raiz-da-wiki>` quando disponível.

Se a página falhar, aprofunde-a ou marque `stub`/`needs-review`. Não declare uma wiki completa enquanto suas páginas centrais forem apenas índices comentados.
