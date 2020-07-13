import requests

resp =  requests.get('http://api.openweathermap.org/data/2.5/weather?zip=24106,de&appid=APIKEY')
# print(dir(resp))
#json = resp.json()
# print(json)
print(resp.json())
