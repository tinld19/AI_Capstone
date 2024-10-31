from .utils.semantic_route import load_route_layer, load_route
from .models.large_language_model import OpenAIClient
# from .database.handle_data import TextChunkProcessor
from .database.faiss_storage import SentenceTransformerEmbeddings
import os

embedding_function = SentenceTransformerEmbeddings()
embedding_function.add_documents_from_file("Data/knowledge.json")

class ChatBot:
   def gen_answer(self, question):
      routes = load_route()
      rl = load_route_layer(question, routes)
      openai_client = OpenAIClient()
      if (rl == "chitchat") or (rl == None):
         return "Câu hỏi không phù hợp với domain"
      else:
         result = embedding_function.search(query=question, domain=rl, k=5)
         answer = openai_client.call_openai(rl, result, question)
         # print("Answer: ", answer)
         return answer, rl
      
   # def load_data(self):
   #    processor = TextChunkProcessor()
   #    # base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../../"))
   #    # file_path = os.path.join(base_dir, "Data", "knowledge.json")
   #    file_path = "Data/knowledge.json"
   #    processor.read_data_from_file(file_path)
