import sys
import os
import time
from pathlib import Path

root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

import pandas as pd
from datasets import Dataset
from ragas import evaluate, RunConfig
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

from bot.aiBot import AIBot
from evaluation.dataset import dataset_sessions

import json

def run_evaluation():
    bot = AIBot()
    
    print(f"Dataset de sessões carregado com {len(dataset_sessions)} sessões multi-turn.")

    questions = []
    answers = []
    contexts_list = []
    ground_truths = []
    
    checkpoint_file = "evaluation/checkpoint_generation.json"
    checkpoint_data = []
    
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, "r", encoding="utf-8") as f:
            checkpoint_data = json.load(f)
            print(f"-> Checkpoint carregado com {len(checkpoint_data)} turnos já gerados.")
            
    # Cria um dicionário para busca rápida
    answered_questions = {item['question']: item for item in checkpoint_data}
    
    print("Gerando respostas do bot para as sessões...")
    
    # Se quiser testar apenas uma parte para o TCC sem bater cota, altere dataset_sessions para dataset_sessions[:10]
    for session in dataset_sessions:
        print(f"\n--- Iniciando Sessão {session['session_id']} ---")
        history_messages = []
        for turn in session['turns']:
            q = turn['question']
            print(f"Q: {q}")
            
            if q in answered_questions:
                print(" -> Recuperado do checkpoint.")
                saved_item = answered_questions[q]
                resposta = saved_item['answer']
                contexts = saved_item['contexts']
            else:
                try:
                    resposta, docs = bot.invoke(history_messages=history_messages, question=q, return_context=True)
                    contexts = [d.page_content for d in docs]
                    
                    # Salva no checkpoint
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
                    print(f"\n[!] Erro na API (possível Rate Limit): {e}")
                    print("[!] O progresso foi salvo no checkpoint 'checkpoint_generation.json'.")
                    print("[!] Aguarde o limite da Groq resetar ou use outra chave de API, e rode o script novamente.")
                    return
            
            questions.append(q)
            answers.append(resposta)
            contexts_list.append(contexts)
            ground_truths.append(turn['ground_truth'])
            
            history_messages.append((q, resposta))
            
    data = {
        "question": questions,
        "answer": answers,
        "contexts": contexts_list,
        "ground_truth": ground_truths
    }
    
    hf_dataset = Dataset.from_dict(data)
    
    llm = ChatGroq(model=os.environ['LLAMA_V'])
    embeddings = bot.embeddings
    
    print("\nIniciando avaliação RAGAS nas sessões...")
    metrics = [faithfulness, answer_relevancy, context_precision, context_recall]
    
    run_config = RunConfig(max_workers=1, timeout=30)

    try:
        from ragas.llms import LangchainLLMWrapper
        from ragas.embeddings import LangchainEmbeddingsWrapper
        evaluate_result = evaluate(
            dataset=hf_dataset,
            metrics=metrics,
            llm=LangchainLLMWrapper(llm),
            embeddings=LangchainEmbeddingsWrapper(embeddings),
            run_config=run_config
        )
    except:
        evaluate_result = evaluate(
            dataset=hf_dataset,
            metrics=metrics,
            llm=llm,
            embeddings=embeddings,
            run_config=run_config
        )

    print("\nResultados da Avaliação RAGAS Multi-turn:")
    print(evaluate_result)
    
    df = evaluate_result.to_pandas()
    df.to_csv("evaluation/ragas_results_sessions.csv", index=False)
    print("Resultados salvos em evaluation/ragas_results_sessions.csv")

if __name__ == "__main__":
    from decouple import config
    os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
    os.environ['LLAMA_V'] = config('LLAMA_V')
    os.environ['CHROMA_PERSIST_DIR'] = str(root_dir / 'chroma_data')
    run_evaluation()
