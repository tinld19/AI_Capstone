from .utils.semantic_route import load_route_layer, load_route
from .database.elastic_storage import ElasticSearchHandler
from .models.large_language_model import OpenAIClient
from .database.handle_data import TextChunkProcessor
import os

class ChatBot:
   def gen_answer(self, question):
      routes = load_route()
      rl = load_route_layer(question, routes)
      elastic_storage = ElasticSearchHandler("docs_container")
      openai_client = OpenAIClient()
      if rl == "chitchat":
         return "Câu hỏi không phù hợp với domain"
      else:
         list_knowledge_base = elastic_storage.get_top_similar_documents(rl, question)
         # print(f"Domain: {rl}")
         knowledge_base = """ """
         for kb in list_knowledge_base:
            knowledge_base += kb["context"] + "\n"
         answer = openai_client.call_openai(rl, knowledge_base, question)
         # print("Answer: ", answer)
         return answer
      
   def load_data(self):
      processor = TextChunkProcessor()
      base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../../"))
      file_path = os.path.join(base_dir, "Data", "knowledge.json")
      processor.read_data_from_file(file_path)
