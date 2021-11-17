import requests

BASE = "http://localhost:8000/"

response = requests.get(BASE + "helloworld")
print(response.json())
