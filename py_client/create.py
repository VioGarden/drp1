import requests

headers = {'Authorization': 'Bearer 26bba57e0250856e115cb67fe2eded3cfca595b7'}

endpoint = "http://localhost:8000/api/products/"
# one way to login, --> admin --> session --> post data
# ^ good for solo projects, but not great for 3rd party api access

data = {
    "title": "This field is done",
    "price": 32.90
}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())