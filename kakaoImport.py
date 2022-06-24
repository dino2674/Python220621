import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
client_id = 'b49beab28af53268eb463029b256ea6d'
redirect_uri = 'https://example.com/oauth'
code = 'y9Bu0vbemCPEFlhGtL2HNuYwqF0MbdgfM8iIuHj6mJC92moS1F3dA-t0THnBNwqfnV1W7gorDR8AAAGBj1vAVw'

data = {
    'grant_type':'authorization_code',
    'client_id':client_id,
    'redirect_uri':redirect_uri,
    'code': code,
    }

response = requests.post(url, data=data)
tokens = response.json()

#발행된 토큰 저장
with open("token.json","w") as kakao:
    json.dump(tokens, kakao)