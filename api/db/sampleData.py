import requests

url = "http://127.0.0.1:5000/api/milestone"
obj = {
    "name":"testMeilenstein",
    "idImage":"5",
    "amount":"1200.0",
    "description":"Testbeschreibung"
}
x = requests.post(url,headers = obj)
print(x.text)