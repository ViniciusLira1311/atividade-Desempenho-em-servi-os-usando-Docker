import requests

for i in range(10):
    response = requests.get('http://localhost:80')
    print(f"Requisição {i+1}: {response.text}")