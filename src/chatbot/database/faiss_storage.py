import json
import faiss
from uuid import uuid4
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings
from langchain.schema import Document

class SentenceTransformerEmbeddings(Embeddings):
   def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
      self.model = SentenceTransformer(model_name)
      sample_embedding = self.embed_query("Hello world")
      embedding_dim = len(sample_embedding)
      self.index = faiss.IndexFlatL2(embedding_dim)
      self.vector_store = FAISS(
         embedding_function=self,
         index=self.index,
         docstore=InMemoryDocstore(),
         index_to_docstore_id={},
      )

   def embed_query(self, text):
      return self.model.encode(text)

   def embed_documents(self, texts):
      return [self.model.encode(text) for text in texts]

   def split_text(self, text, chunk_size=300, overlap=50):
      """Chia văn bản thành các đoạn nhỏ (chunk) với độ dài cụ thể."""
      words = text.split()
      chunks = []
      for i in range(0, len(words), chunk_size - overlap):
         chunk = " ".join(words[i:i + chunk_size])
         chunks.append(chunk)
      return chunks

   def add_documents_from_file(self, file_path, chunk_size=300, overlap=50):
      with open(file_path, 'r', encoding='utf-8') as f:
         data = json.load(f)
      
      documents = []
      for item in data:
         chunks = self.split_text(item["content"]["context"], chunk_size, overlap)
         for chunk in chunks:
               doc = Document(
                  page_content=chunk,
                  metadata={"source": item["domain"]}
               )
               documents.append(doc)

      uuids = [str(uuid4()) for _ in range(len(documents))]
      self.vector_store.add_documents(documents=documents, ids=uuids)

   def search(self, query, domain, k=5):
      results = self.vector_store.similarity_search(
         query,
         k=k,
         filter={"source": domain},
      )
      output = "\n".join([f"{res.page_content} [{res.metadata}]" for res in results])
      return output