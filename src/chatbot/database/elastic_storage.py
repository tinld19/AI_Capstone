from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
from scipy import spatial

# "http://localhost:9200"
class ElasticSearchHandler:
   def __init__(self, index_name, es_host="http://localhost:9200"):
      self.index_name = index_name
      self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
      self.es = Elasticsearch(hosts=[es_host])

   def split_text_into_chunks(self, text, max_length=128):
      sentences = text.split('. ')
      chunks = []
      current_chunk = []
      current_length = 0

      for sentence in sentences:
         sentence_length = len(sentence.split())
         if current_length + sentence_length <= max_length:
               current_chunk.append(sentence)
               current_length += sentence_length
         else:
               chunks.append('. '.join(current_chunk) + '.')
               current_chunk = [sentence]
               current_length = sentence_length

      if current_chunk:
         chunks.append('. '.join(current_chunk) + '.')

      return chunks

   def store_chunks(self, domain, context):
      chunks = self.split_text_into_chunks(context)
      for i, chunk in enumerate(chunks):
         embedding = self.model.encode(chunk).tolist()
         document = {
               "domain": domain,
               "context": chunk,
               "vector": embedding
         }
         self.es.index(index=self.index_name, id=f"{domain}_{i}", body=document)
         
   def cosine_similarity(self, vector1, vector2):
      return 1 - spatial.distance.cosine(vector1, vector2)

   def get_documents_by_domain(self, domain):
      query = {
         "query": {
               "match": {
                  "domain": domain
               }
         }
      }
      results = self.es.search(index=self.index_name, body=query)
      documents = [hit["_source"] for hit in results["hits"]["hits"]]
      return documents
   
   def get_top_similar_documents(self, domain, question, top_k=5):
      question_embedding = self.model.encode(question)
      documents = self.get_documents_by_domain(domain)
      for doc in documents:
         doc["similarity"] = self.cosine_similarity(question_embedding, doc["vector"])
      documents = sorted(documents, key=lambda x: x["similarity"], reverse=True)
      return documents[:top_k]