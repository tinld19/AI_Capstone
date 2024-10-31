# import json
# from sentence_transformers import SentenceTransformer
# from elasticsearch import Elasticsearch

# # Initialize the model and Elasticsearch client
# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# try:
#     es = Elasticsearch(hosts=["http://es-container:9200"])
#     if not es.ping():
#         raise ValueError("Connection failed")
#     else:
#         print("Connected to Elasticsearch")
# except ConnectionError as e:
#     print(f"Could not connect to Elasticsearch: {e}")

# class TextChunkProcessor:    
#     def split_text_into_chunks(self, text, max_length=128):
#         sentences = text.split('. ')
#         chunks = []
#         current_chunk = []
#         current_length = 0

#         for sentence in sentences:
#             sentence_length = len(sentence.split())
#             if current_length + sentence_length <= max_length:
#                 current_chunk.append(sentence)
#                 current_length += sentence_length
#             else:
#                 chunks.append('. '.join(current_chunk) + '.')
#                 current_chunk = [sentence]
#                 current_length = sentence_length

#         if current_chunk:
#             chunks.append('. '.join(current_chunk) + '.')

#         return chunks

#     def store_chunks_in_elasticsearch(self, domain, context):
#         chunks = self.split_text_into_chunks(context)
#         for i, chunk in enumerate(chunks):
#             embedding = model.encode(chunk).tolist()
#             document = {
#                 "domain": domain,
#                 "context": chunk,
#                 "vector": embedding
#             }
#             es.index(index="docs_container", id=f"{domain}_{i}", body=document)

#     def read_data_from_file(self, file_path):
#         with open(file_path, 'r') as file:
#             list_data = json.load(file)
#             for data in list_data:
#                 self.store_chunks_in_elasticsearch(data["domain"], data["content"]["context"])

#     def get_all_data_from_elasticsearch(self):
#         query = {
#             "query": {
#                 "match_all": {}
#             }
#         }
#         response = es.search(index="docs_container", body=query, size=10000)
#         return response['hits']['hits']
    
# read_data_from_file("/Users/mac/Documents/AI_Capstone/Data/knowledge.json")

# data = get_all_data_from_elasticsearch()

# for item in data:
#    print(item['_source']['domain'], item['_source']['context'])
#    print("--------------------")
