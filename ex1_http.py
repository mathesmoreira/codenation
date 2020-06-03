#Codenation - Aula de HTTP
import requests

#Token
token_url = 'https://httpbin.org/bearer'
token = 'Bearer MySuperToken'

response = requests.get(token_url, headers = {'Authorization': token})

print(f'Token Status Code: {response.status_code}')
print(f'Token Response: {response.json()}')