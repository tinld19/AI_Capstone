from sentence_transformers import SentenceTransformer
from singleton_decorator import singleton

@singleton
class EmbeddingService:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def encode(self, sentences):
        return self.model.encode(sentences)