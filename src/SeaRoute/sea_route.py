from geopy.geocoders import Nominatim
import searoute as sr
from geopy.geocoders import ArcGIS


class SeaRoute:
   @staticmethod
   def compute_distance(list_location_from, list_location_to):
      loc = Nominatim(user_agent="GetLoc")
      # geolocator = ArcGIS(scheme="https")
      getLoc = loc.geocode(list_location_from)
      getDes = loc.geocode(list_location_to)
      origin = [getLoc.longitude, getLoc.latitude]
      destination = [getDes.longitude, getDes.latitude]
      # print("origin", origin)
      # print("destination", destination)
      route = sr.searoute(origin, destination)
      # print("infor route:", route)
      distance = route["properties"]["length"]
      time = route["properties"]["duration_hours"]
      # print("distance", distance)
      return distance, time
   
   @staticmethod
   def get_location(address):
      loc = Nominatim(user_agent="GetLoc")
      location = loc.geocode(address)
      return location.longitude, location.latitude