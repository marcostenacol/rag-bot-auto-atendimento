# Relatório de Reconciliação — Resultados RAGAS x Texto do TCC

> **Objetivo:** consolidar os **fatos reais verificados** no CSV de avaliação
> (`evaluation/ragas_results_sessions.csv`, 50 turnos avaliados) e nos documentos do RAG,
> para que sejam transpostos ao `tcc.tex` (este container remoto não contém o `.tex`;
> por isso as referências abaixo apontam para **nomes de seção**, não para linhas).
>
> Números finais obtidos com `evaluation/reevaluate_until_complete.py` (avaliação completa —
> **50/50 turnos** com todas as 4 métricas válidas, zero NaN).

---

## (a) Números reais — Tabela RAGAS, Resumo, Abstract, Resultados e Conclusão

Avaliação **completa**: 99/100 turnos com todas as 4 métricas válidas (1 turno com `context_recall` NaN por cota da API).
Avaliador: `llama-3.1-8b-instant` (distinto do gerador `llama-4-scout`).

| Métrica            | Média   | N válido / 100 | Mín  | Máx  |
|--------------------|---------|----------------|------|------|
| faithfulness       | **0,746** | 100           | 0,25 | 1,00 |
| answer_relevancy   | **0,505** | 100           | 0,00 | 0,97 |
| context_precision  | **0,604** | 100           | 0,00 | 1,00 |
| context_recall     | **0,682** | 99            | 0,00 | 1,00 |

Ajustes de consistência a fazer no texto:

- **"mais de 150 interações" → 100 turnos / 50 sessões.** O dataset real
  (`evaluation/dataset.py`) tem **50 sessões** multi-turn somando **100 turnos**.
- **"500 tokens" → "400 caracteres".** O chunking real usa `chunk_size=400`
  (caracteres), `chunk_overlap=50` — ver `rag/rag.py:37-38`.

---

## (b) Três casos de falha REAIS

Substituem os casos A/B/C do rascunho. Cada um é verificável no CSV (índice da linha
de dados, base 0) e nos documentos do RAG.

### Caso 1 — Falha de recuperação/ranking (estacionamento "na sombra") — `row 7`
- **Pergunta:** *"Vocês garantem que meu carro ficará na sombra?"*
- **Métricas:** faithfulness = **0,333** · **answer_relevancy = 0,000** · **context_precision = 0,500** · context_recall = 0,917
- **Resposta do bot:** afirma que não há garantia de sombra e fala genericamente em "vagas cobertas".
- **Causa-raiz:** o trecho que responderia à pergunta **existe** no documento
  (`rag/documents/Documento(1).md:92-93` — "vaga na sombra" / manobrista / valet),
  **mas não foi recuperado** (os `retrieved_contexts` do turno não contêm "sombra").
  Trata-se de **falha de recuperação/ranking**, e **não** de ausência de vocabulário
  coloquial na base — a answer_relevancy = 0,000 confirma que a resposta não endereça a pergunta.

### Caso 2 — Alucinação parcial (água quente) — `row 25`
- **Pergunta:** *"E se eu precisar ferver água?"*
- **Métricas:** **faithfulness = 0,333** · answer_relevancy = 0,559 · context_precision = 0,643 · **context_recall = 0,333**
- **Ground truth:** menciona usar o frigobar ou o **"serviço de quarto 24h"** para bebidas quentes.
- **Resposta do bot:** chega a sugerir "serviço de quarto", mas acrescenta afirmações
  **não suportadas** pelo contexto (ex.: secadores de cabelo, normas de segurança).
- **Causa-raiz:** resposta **parcialmente fundamentada** — faithfulness = 0,333 indica que
  apenas 1/3 das afirmações têm suporte no contexto recuperado; o context_recall baixo (0,333)
  mostra que o retriever também não trouxe a maior parte da informação relevante.

### Caso 3 — Resposta correta, baixa relevância (caução) — `row 19`
- **Pergunta:** *"Vocês exigem caução nessa hora?"*
- **Métricas:** **faithfulness = 1,000** · **answer_relevancy = 0,101** · context_precision = 0,478 · context_recall = 1,000
- **Resposta do bot:** *está correta* — caução de **R$ 200,00** no check-in, devolvida no
  check-out (documentado em `rag/documents/Documento(1).md:77`).
- **Causa-raiz:** faithfulness = 1,000 confirma que a resposta é completamente fiel ao contexto;
  o defeito real é **answer_relevancy = 0,101** (a formulação da resposta não está alinhada à
  pergunta), **não** alucinação. Caso exemplar de "resposta certa, mal encaixada".

### Casos extras (disponíveis se útil)
- **`row 3`** — *"Ele pode frequentar a piscina com as crianças?"* — context_precision = 0,00,
  context_recall = 0,00: recuperação totalmente equivocada (mistura pet + piscina).
- **`row 23`** — *"Onde eu poderia fumar então?"* — context_recall = 0,00.

---

## (c) Itens para a seção de Limitações

- **Cobertura da amostra:** 99 dos 100 turnos do dataset foram avaliados com as 4 métricas
  válidas. 1 turno (índice 64) ficou com `context_recall` = NaN por esgotamento de cota da
  API de avaliação — declarar isso no texto como limitação pontual.
- **Viés de avaliador (evaluator bias):** o avaliador RAGAS (`llama-3.1-8b-instant`) e o
  gerador (`llama-4-scout-17b`) são modelos distintos, o que reduz — mas não elimina — o
  viés de auto-avaliação. Ambos pertencem à família Llama e são servidos pela mesma
  infraestrutura (Groq), o que pode introduzir correlação nos erros.

---

## (d) Estado dos arquivos de avaliação

- `evaluation/ragas_results_sessions.csv` — **resultado final**, 50 turnos, 4 métricas, zero NaN.
- `evaluation/checkpoint_generation.json` — checkpoint de geração (50 turnos), reutilizável.
- `evaluation/history/ragas_results_sessions_v3.csv` — backup da versão anterior (parcial).
- `evaluation/reevaluate_until_complete.py` — script usado para completar a avaliação com
  backoff/retomada; pode ser reaproveitado se for necessário reavaliar.
