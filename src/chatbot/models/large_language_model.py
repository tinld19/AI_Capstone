import os
from singleton_decorator import singleton
from openai import AzureOpenAI as az
from dotenv import load_dotenv
from .prompt_tuning import PROMPT_CHAT

load_dotenv()

@singleton
class OpenAIClient:
   def __init__(self):
      self.azure_endpoint = os.getenv('AZURE_ENDPOINT')
      self.api_key = os.getenv('API_KEY')
      self.api_version = os.getenv('API_VERSION', '2024-02-15-preview')
      
      if not self.azure_endpoint or not self.api_key:
         raise ValueError("AZURE_ENDPOINT and API_KEY environment variables must be set")
      
      self.client = az(
         azure_endpoint=self.azure_endpoint,
         api_key=self.api_key,
         api_version=self.api_version
      )

   def call_openai(self, domain, knowledge_base, question):
      prompt = PROMPT_CHAT.replace("{domain}", domain).replace("{knowledge_base}", knowledge_base).replace("{question}", question)
      
      completion = self.client.chat.completions.create(
         model='testing-auto-gen-testcase',
         messages=[
               {
                  "role": "user",
                  "content": prompt,
               }
         ],
         max_tokens=1000,
      )
      
      message_openai = completion.choices[0].message.content.lstrip("\n")
      return message_openai