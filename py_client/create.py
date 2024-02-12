import requests
endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(endpoint, json={"title":"SSD", "content":"Blazing Fast", "price": 12345})

print(get_response.json())