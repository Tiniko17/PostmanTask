from server import link_to_server
import pip._vendor.requests 
import json

response_from_server = pip._vendor.requests.get(link_to_server)
data_from_response = json.loads(response_from_server.text)
