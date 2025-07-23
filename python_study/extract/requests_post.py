import requests

url = "https://reqres.in/api/login"
headers = {
    "x-api-key": "reqres-free-v1"
}
payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

try :
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
    print(response.json())
except Exception as e :
    print(e)