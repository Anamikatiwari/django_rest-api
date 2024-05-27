import requests

credentials= {
    'username':'admin',
    'password':'admin'
}

response=requests.request("POST",'http://localhost:8000/api-token-auth/',json=credentials)
data=response.json()
print(data)
token='c6ce2d37329337919f6c8614ffb6f459e225a5f5'

headers={
    'Authorization':'Token '+token
}

response=requests.request("GET",'http://localhost:8000/recipe/list_recipes/',headers=headers)
data=response.json()
print(data)
