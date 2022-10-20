import requests # API Library

# endpoints are like urls, there will be many in your application
# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/" # "http://127.0.0.1:8000/"

# get_response = requests.post(endpoint, params={"abc":123}, json={"query":"Hello World"}) # HTTP Request
get_response = requests.post(endpoint, json={"title":"abc123", "content":"Hello World", "price":"abc1234"}) # HTTP Request

# whenever urls http://localhost:8000/api/?this_arg="thisvalue" <-- query parameters

# Rest API --> Web API (uses HTTP Request)
# print(get_response.text) # Print raw text response
# print(get_response.status_code)

# HTTP Request --> HTML
# REST API HTTP Request --> JSON (xml)
# JavaScript Object Notation ~almost~ Python Dictionary

print(get_response.json()) # Python Dictionary
# print(get_response.json()['message']) # Python Dictionary
# print(get_response.status_code) # Status Code of API

# b'{"query": "Hello World"}'
