import os
import sys
import shutil
from decouple import config

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_huggingface import HuggingFaceEmbeddings

os.environ['HUGGINGFACE_API_KEY'] = config('HUGGINGFACE_API_KEY')

persist_directory = os.environ.get('CHROMA_PERSIST_DIR', 'chroma_data')

if __name__ == '__main__':

    if '--reset' in sys.argv:
        if os.path.exists(persist_directory):
            shutil.rmtree(persist_directory)
            print("Banco vetorial limpo.")

    folder_path = os.environ.get('RAG_DOCS_DIR', 'rag/documents')
    all_docs = []

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if filename.endswith('.pdf'):
            loader = PyPDFLoader(full_path)
            docs = loader.load()
            all_docs.extend(docs)
        elif filename.endswith('.md'):
            loader = TextLoader(full_path, encoding='utf-8')
            docs = loader.load()
            all_docs.extend(docs)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50,
    )
    chunks = text_splitter.split_documents(documents=all_docs)

    for chunk in chunks:
        source = chunk.metadata.get("source", "desconhecido")
        filename = os.path.basename(source).replace(".pdf", "").replace(".md", "")
        chunk.page_content = f"[Documento: {filename} - Hotel]\n\n{chunk.page_content}"

    print(f"Total de chunks gerados: {len(chunks)}")

    embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )
    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory=persist_directory,
    )
    vector_store.add_documents(documents=chunks)
    print("Documentos indexados com sucesso!")
