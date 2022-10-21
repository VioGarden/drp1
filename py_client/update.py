import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "zembu zumbu",
    "price": 159.33
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())