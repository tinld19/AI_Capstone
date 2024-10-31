# import json
# import faiss
# from uuid import uuid4
# from langchain_community.docstore.in_memory import InMemoryDocstore
# from langchain_community.vectorstores import FAISS
# from sentence_transformers import SentenceTransformer
# from langchain.embeddings.base import Embeddings
# from langchain.schema import Document

# class SentenceTransformerEmbeddings(Embeddings):
#    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
#       self.model = SentenceTransformer(model_name)
#       sample_embedding = self.embed_query("Hello world")
#       embedding_dim = len(sample_embedding)
#       self.index = faiss.IndexFlatL2(embedding_dim)
#       self.vector_store = FAISS(
#          embedding_function=self,
#          index=self.index,
#          docstore=InMemoryDocstore(),
#          index_to_docstore_id={},
#       )
   
#    def embed_query(self, text):
#       return self.model.encode(text)

#    def embed_documents(self, texts):
#       return [self.model.encode(text) for text in texts]

#    def add_documents_from_file(self, file_path):
#       with open(file_path, 'r', encoding='utf-8') as f:
#          data = json.load(f)
      
#       documents = []
#       for item in data:
#          doc = Document(
#                page_content=item["content"]["context"],
#                metadata={"source": item["domain"]}
#          )
#          documents.append(doc)

#       uuids = [str(uuid4()) for _ in range(len(documents))]
      
#       self.vector_store.add_documents(documents=documents, ids=uuids)

#    def search(self, query, domain, k=2):
#       results = self.vector_store.similarity_search(
#          query,
#          k=k,
#          filter={"source": domain},
#       )
      
#       output = "\n".join([f"{res.page_content} [{res.metadata}]" for res in results])
#       return output

# if __name__ == "__main__":
#    embedding_function = SentenceTransformerEmbeddings()

#    embedding_function.add_documents_from_file("/Users/mac/Documents/AI_Capstone/AI_Capstone/Data/knowledge.json")

#    query = "Khai báo hải quan là gì?"
#    domain = "Khai báo hải quan"
#    output = embedding_function.search(query, domain)

#    print(output)
