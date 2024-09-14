import os
import json
import sys

from semantic_router import Route
from semantic_router.layer import RouteLayer
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder()

def load_route():
   relative_path = os.path.join('..', 'AI_CAPSTONE', 'Data', 'route.json')
   file_path = os.path.abspath(relative_path)
   routes = []
   
   with open(file_path, 'r') as file:
      data = json.load(file)
   
   for item in data:
      for key, value in item.items():
         routes.append(Route(
            name=key,
            utterances = value
         ))
   return routes

def load_route_layer(question, routes):
   rl = RouteLayer(encoder=encoder, routes=routes)
   domain = rl(question).name
   return domain

# routes = load_route()