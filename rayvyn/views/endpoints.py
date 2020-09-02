from flask import render_template, jsonify
from Model import Cve, products_schema, app, product_schema
import simplejson as json
import re


@app.route('/index')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def rayvyn():

    return render_template('rayvyn.html')


@app.route('/getData', methods=['GET'])
def getData():
    f = []
    data = Cve.query.filter((Cve.impact >= 7.5) | ((Cve.vector == 'NETWORK') & (Cve.impact >= 7.5))).all()
    result = products_schema.dump(data)
    for cve in result:
        desc = str(cve['description'])
        desc = re.sub('[^-.0-9a-zA-Z]+', ' ', desc)
        cve['description'] = desc
        cve['list_vendors'] = str(cve['list_vendors']).capitalize()
        p = list(cve.values())
        p.insert(0,"")
        f.append(p)
    cve = json.dumps(f)
    # print(cve)
    return str(cve)
