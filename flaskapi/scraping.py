import requests

resp =  requests.get('http://api.openweathermap.org/data/2.5/weather?zip=24106,de&appid=58c4e41bd6b01af1061714aad969ee0d')
# print(dir(resp))
#json = resp.json()
# print(json)
print(resp.json())