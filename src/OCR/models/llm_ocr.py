import os
import google.generativeai as genai
from singleton_decorator import singleton
from openai import AzureOpenAI as az
from dotenv import load_dotenv
from .prompt import PROMT_OCR

load_dotenv()
genai.configure(api_key=os.getenv('API_KEY'))

@singleton
class LLM_OCR:
   def __init__(self):
      # self.azure_endpoint = os.getenv('AZURE_ENDPOINT')
      # self.api_key = os.getenv('API_KEY')
      # self.api_version = os.getenv('API_VERSION', '2024-02-15-preview')
      
      # if not self.azure_endpoint or not self.api_key:
      #    raise ValueError("AZURE_ENDPOINT and API_KEY environment variables must be set")
      
      # self.client = az(
      #    azure_endpoint=self.azure_endpoint,
      #    api_key=self.api_key,
      #    api_version=self.api_version
      # )
      self.model = genai.GenerativeModel("gemini-1.5-flash")
   
   def extract_data_ocr(self, data):
      prompt = PROMT_OCR.replace("{data}", data)
      
      # completion = self.client.chat.completions.create(
      #    model='testing-auto-gen-testcase',
      #    messages=[
      #          {
      #             "role": "user",
      #             "content": prompt,
      #          }
      #    ],
      #    max_tokens=1000,
      # )
      
      # message_openai = completion.choices[0].message.content.lstrip("\n")
      # message_clean = message_openai.replace("```", "").replace("json", "")
      message_clean = self.model.generate_content(prompt)
      return message_clean.text