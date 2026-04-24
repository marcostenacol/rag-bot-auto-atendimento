import sys
import os
from pathlib import Path

root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from decouple import config

from bot.aiBot import AIBot
from evaluation.dataset import dataset

def run_benchmark():
    bot = AIBot()
    
    print(f"Dataset padrão (dataset.py) carregado com {len(dataset)} perguntas.")
    
    llm = ChatGroq(model=os.environ['LLAMA_V'])
    
    results = []
    
    print(f"Executando Benchmark para {len(dataset)} perguntas...")
    for item in dataset:
        q = item['question']
        print(f"Testando: {q}")
        
        ans_rag = bot.invoke(history_messages=[], question=q)
        
        ans_llm_obj = llm.invoke([HumanMessage(content=q)])
        ans_llm = ans_llm_obj.content if hasattr(ans_llm_obj, 'content') else str(ans_llm_obj)
        
        results.append({
            "Pergunta": q,
            "Resposta Esperada": item['ground_truth'],
            "RAG (Com Contexto)": ans_rag,
            "LLM Puro (Sem Contexto)": ans_llm
        })
        
    df = pd.DataFrame(results)
    
    csv_path = "evaluation/benchmark_results.csv"
    df.to_csv(csv_path, index=False)
    print(f"Resultados salvos em {csv_path}")

if __name__ == "__main__":
    os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
    os.environ['LLAMA_V'] = config('LLAMA_V')
    os.environ['CHROMA_PERSIST_DIR'] = str(root_dir / 'chroma_data')
    run_benchmark()
