import sys
import os
import time
import json
from pathlib import Path

root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from bot.aiBot import AIBot
from evaluation.dataset import dataset_sessions


def run_generation():
    bot = AIBot()

    print(f"Dataset carregado: {len(dataset_sessions)} sessões multi-turn.")

    checkpoint_file = "evaluation/checkpoint_generation.json"
    checkpoint_data = []

    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, "r", encoding="utf-8") as f:
            checkpoint_data = json.load(f)
        print(f"-> Checkpoint carregado com {len(checkpoint_data)} turnos já gerados.")

    answered_questions = {item['question']: item for item in checkpoint_data}

    print("Gerando respostas do bot para as sessões...")

    for session in dataset_sessions:
        print(f"\n--- Sessão {session['session_id']} ---")
        history_messages = []
        for turn in session['turns']:
            q = turn['question']
            print(f"Q: {q}")

            if q in answered_questions:
                print(" -> Recuperado do checkpoint.")
            else:
                try:
                    resposta, docs = bot.invoke(history_messages=history_messages, question=q, return_context=True)
                    contexts = [d.page_content for d in docs]

                    checkpoint_data.append({
                        "question": q,
                        "answer": resposta,
                        "contexts": contexts,
                        "ground_truth": turn['ground_truth']
                    })
                    with open(checkpoint_file, "w", encoding="utf-8") as f:
                        json.dump(checkpoint_data, f, ensure_ascii=False, indent=4)

                    time.sleep(2)
                except Exception as e:
                    print(f"\n[!] Erro na API: {e}")
                    print("[!] Progresso salvo em checkpoint_generation.json. Rode novamente para continuar.")
                    return

            saved = answered_questions.get(q) or checkpoint_data[-1]
            history_messages.append((q, saved['answer']))

    total = len([t for s in dataset_sessions for t in s['turns']])
    print(f"\nGeração concluída: {len(checkpoint_data)}/{total} turnos salvos em {checkpoint_file}")
    print("Execute reevaluate_until_complete.py para calcular as métricas RAGAS.")


if __name__ == "__main__":
    from decouple import config
    os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
    os.environ['LLAMA_V'] = config('LLAMA_V')
    os.environ['CHROMA_PERSIST_DIR'] = str(root_dir / 'chroma_data')
    run_generation()
