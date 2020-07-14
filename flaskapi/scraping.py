import requests

resp =  requests.get('http://api.openweathermap.org/data/2.5/weather?zip=24106,de&appid=58c4e41bd6b01af1061714aad969ee0d')
# resp =  requests.get('https://raw.githubusercontent.com/CVEProject/cvelist/master/1999/0xxx/CVE-1999-0001.json')
# resp =  requests.get('https://source.android.com/security/bulletin/2020-03-01')

# print(dir(resp))
r = resp.json()
print(r)
#json = resp.json()
# print(json)
# obj = resp.json()
# print(obj['CVE_data_meta'])