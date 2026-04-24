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
from evaluation.dataset import dataset

def run_evaluation():
    bot = AIBot()
    
    print(f"Dataset padrão (dataset.py) carregado com {len(dataset)} perguntas.")

    questions = []
    answers = []
    contexts_list = []
    ground_truths = []
    
    print(f"Gerando respostas do bot para {len(dataset)} perguntas...")
    for item in dataset:
        q = item['question']
        print(f"Q: {q}")
        
        docs = bot._AIBot__retriever.invoke(q)
        contexts = [d.page_content for d in docs]
        
        resposta = bot.invoke(history_messages=[], question=q)
        
        questions.append(q)
        answers.append(resposta)
        contexts_list.append(contexts)
        ground_truths.append(item['ground_truth'])
        
        time.sleep(2)
        
    data = {
        "question": questions,
        "answer": answers,
        "contexts": contexts_list,
        "ground_truth": ground_truths
    }
    
    hf_dataset = Dataset.from_dict(data)
    
    llm = ChatGroq(model=os.environ['LLAMA_V'])
    embeddings = bot.embeddings
    
    print("Iniciando avaliação RAGAS...")
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

    print("Resultados da Avaliação RAGAS:")
    print(evaluate_result)
    
    df = evaluate_result.to_pandas()
    df.to_csv("evaluation/ragas_results.csv", index=False)
    print("Resultados salvos em evaluation/ragas_results.csv")

if __name__ == "__main__":
    from decouple import config
    os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
    os.environ['LLAMA_V'] = config('LLAMA_V')
    os.environ['CHROMA_PERSIST_DIR'] = str(root_dir / 'chroma_data')
    run_evaluation()
