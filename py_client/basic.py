import requests
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint,json={"title": "wire"})

print(get_response.json())