import requests

endpoint = "http://localhost:8000/api/products/"
# one way to login, --> admin --> session --> post data
# ^ good for solo projects, but not great for 3rd party api access

data = {
    "title": "This field is done",
    "price": 32.90
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())