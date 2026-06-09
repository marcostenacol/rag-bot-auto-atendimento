"""Reavalia os 100 turnos do checkpoint com RAGAS ate todos terem as 4 metricas validas.

Reaproveita evaluation/checkpoint_generation.json (geracao ja concluida) e refaz apenas
a fase de avaliacao, em micro-lotes com backoff. Persiste o CSV a cada lote e RETOMA de um
CSV anterior (so reavalia os turnos com metrica NaN), o que permite completar ao longo de
varios dias respeitando os limites de cota (RPD/TPD) sem retrabalho.

Avaliador: Qwen3-32B (independente do gerador Llama-4 -> evita vies de auto-avaliacao;
robusto em JSON, validado; TPD 500k). RPD do free tier (~1000) pode exigir 2 execucoes.

Uso: .venv/bin/python evaluation/reevaluate_until_complete.py
"""

import sys
import os
import time
import json
import math
import csv as _csv
from pathlib import Path

root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from decouple import config

os.environ["GROQ_API_KEY"] = config("GROQ_API_KEY")
os.environ["LLAMA_V"] = config("LLAMA_V")
os.environ["CHROMA_PERSIST_DIR"] = str(root_dir / "chroma_data")

import pandas as pd
from datasets import Dataset
from ragas import evaluate, RunConfig
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

CHECKPOINT = root_dir / "evaluation" / "checkpoint_generation.json"
OUT_CSV = root_dir / "evaluation" / "ragas_results_sessions.csv"
METRIC_COLS = ["faithfulness", "answer_relevancy", "context_precision", "context_recall"]

EVAL_MODEL = "llama-3.1-8b-instant"   # avaliador instruct, distinto do gerador Llama-4; cota folgada (500k TPD)
N_LIMIT = 100  # avaliar todos os 100 turnos; os 50 ja completos serao carregados do CSV
BATCH = 3          # turnos por lote
MAX_ROUNDS = 60    # rodadas de reavaliacao das linhas ainda NaN
SLEEP_BATCH = 8    # pausa entre lotes (segundos)
SLEEP_ROUND = 30   # pausa entre rodadas (segundos)


def is_valid(v):
    try:
        return v is not None and str(v).strip() != "" and not math.isnan(float(v))
    except (TypeError, ValueError):
        return False


def build_wrappers():
    # Avaliador independente do gerador (Qwen3-32B != Llama): evita vies de auto-avaliacao;
    # robusto em JSON (validado) e com TPD suficiente (500k). temp=0 -> determinismo.
    llm_raw = ChatGroq(model=EVAL_MODEL, temperature=0)
    emb_raw = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
    try:
        from ragas.llms import LangchainLLMWrapper
        from ragas.embeddings import LangchainEmbeddingsWrapper
        return LangchainLLMWrapper(llm_raw), LangchainEmbeddingsWrapper(emb_raw)
    except Exception:
        return llm_raw, emb_raw


def main():
    with open(CHECKPOINT, encoding="utf-8") as f:
        turns = json.load(f)
    turns = turns[:N_LIMIT]
    n = len(turns)
    print(f"Turnos a avaliar (amostra): {n}", flush=True)

    results = []
    for t in turns:
        results.append({
            "user_input": t["question"],
            "retrieved_contexts": t["contexts"],
            "response": t["answer"],
            "reference": t["ground_truth"],
            "faithfulness": float("nan"),
            "answer_relevancy": float("nan"),
            "context_precision": float("nan"),
            "context_recall": float("nan"),
        })

    # RETOMADA: carrega scores validos de um CSV anterior (mesmo avaliador), por indice.
    if OUT_CSV.exists():
        with open(OUT_CSV, encoding="utf-8") as f:
            prev = list(_csv.DictReader(f))
        carried = 0
        for i, r in enumerate(prev):
            if i < n:
                for m in METRIC_COLS:
                    if is_valid(r.get(m, "")):
                        results[i][m] = float(r[m]); carried += 1
        print(f"-> Retomada: {carried} metricas validas carregadas do CSV anterior.", flush=True)

    llm, emb = build_wrappers()
    metrics = [faithfulness, answer_relevancy, context_precision, context_recall]
    run_config = RunConfig(max_workers=1, timeout=180, max_retries=10, max_wait=70)

    def valid_count():
        return sum(1 for r in results if all(is_valid(r[m]) for m in METRIC_COLS))

    for rnd in range(1, MAX_ROUNDS + 1):
        pending = [i for i, r in enumerate(results)
                   if not all(is_valid(r[m]) for m in METRIC_COLS)]
        print(f"[Rodada {rnd}] pendentes={len(pending)} validos={valid_count()}/{n}", flush=True)
        if not pending:
            print("COMPLETO: 100/100 validos", flush=True)
            break

        for start in range(0, len(pending), BATCH):
            idxs = pending[start:start + BATCH]
            data = {
                "question": [turns[i]["question"] for i in idxs],
                "answer": [turns[i]["answer"] for i in idxs],
                "contexts": [turns[i]["contexts"] for i in idxs],
                "ground_truth": [turns[i]["ground_truth"] for i in idxs],
            }
            try:
                res = evaluate(dataset=Dataset.from_dict(data), metrics=metrics,
                               llm=llm, embeddings=emb, run_config=run_config)
                df = res.to_pandas()
                for j, i in enumerate(idxs):
                    for m in METRIC_COLS:
                        if m in df.columns:
                            val = df.iloc[j][m]
                            if is_valid(val):
                                results[i][m] = float(val)
                print(f"  lote {idxs} -> ok (validos agora: {valid_count()}/{n})", flush=True)
            except Exception as e:
                print(f"  lote {idxs} -> ERRO: {repr(e)[:160]}", flush=True)
            pd.DataFrame(results).to_csv(OUT_CSV, index=False)
            time.sleep(SLEEP_BATCH)

        if valid_count() < n:
            time.sleep(SLEEP_ROUND)

    pd.DataFrame(results).to_csv(OUT_CSV, index=False)
    print("\n=== RESUMO FINAL ===", flush=True)
    for m in METRIC_COLS:
        vals = [r[m] for r in results if is_valid(r[m])]
        avg = sum(vals) / len(vals) if vals else float("nan")
        print(f"{m}: {len(vals)}/{n} validos | media={avg:.3f}", flush=True)


if __name__ == "__main__":
    main()
