import requests

url="http://192.168.55.48:8000/api/user/login"
data={"userName":"student","password":"123456","remember":False}

r=requests.post(url,json=data)
print(r.text)