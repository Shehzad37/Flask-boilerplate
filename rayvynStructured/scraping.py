#!/usr/bin/env python3
from rvn.dbhandler.CveHandler import add_all_to_db
from rvn.Model.Model import products_schema, Cve
import simplejson as json
from rvn.utils.Util import c_dt

#get_cisco_data()

print(c_dt)
print('Collecting Data...')

print('----------------------')
#send_alert("",1)
#get_palo_data()
#print(get_forti_data())
#get_orc_data()

f = []
add_all_to_db()
data = Cve.query.all()
result = products_schema.dump(data)
for all in result:
    desc = str(all['description']).replace('[','').replace(']','')
    all['description'] = desc
    f.append(list(all.values()))
    # print(f)
print(json.dumps(f))
# data = '[["Tiger Nixon", "System Architect", "Edinburgh", "5421", "2011/04/25", "$4555"],["Garrett Winters", "Accountant", "Tokyo", "8422", "2011/07/25", "$170,750"],["Ashton Cox", "Junior Technical Author", "San Francisco", "1562", "2009/01/12", "$86,000"],["Cedric Kelly", "Senior Javascript Developer", "Edinburgh", "6224", "2012/03/29", "$433,060"]]'

# t = list(result.values())
# print(t)
# print(json.dumps([t]))
# print(str([t]))
# d= '[["Tiger Nixon", "System Architect", "Edinburgh", "5421", "2011/04/25", "$4555"],["Garrett Winters", "Accountant", "Tokyo", "8422", "2011/07/25", "$170,750"],["Ashton Cox", "Junior Technical Author", "San Francisco", "1562", "2009/01/12", "$86,000"],["Cedric Kelly", "Senior Javascript Developer", "Edinburgh", "6224", "2012/03/29", "$433,060"]]'
# print(d)
# //data = Cve.query.all()
# print(data)
# print(p.encode(encoding='md5'))
#print(get_redhat_data())
#get_nist_cve()
#print(get_crit_desc(get_cisco_data()))
