import requests
from api import db
from api.models.ModelOne import Product, Example


# resp =  requests.get('http://api.openweathermap.org/data/2.5/weather?zip=24106,de&appid=58c4e41bd6b01af1061714aad969ee0d')
resp =  requests.get('https://raw.githubusercontent.com/CVEProject/cvelist/master/1999/0xxx/CVE-1999-0001.json')
# resp =  requests.get('https://source.android.com/security/bulletin/2020-03-01')

# print(dir(resp))
r = resp.json()
name = r['CVE_data_meta']['ID']
desc = r['description']['description_data'][0]['value']
price = 0
qty = 0

new_product = Product(name, desc, price, qty)

db.session.add(new_product)
db.session.commit()
print(new_product.id)
db.session.add(Example('Shehzad'))
db.session.add(new_product)
db.session.commit()
print('added')