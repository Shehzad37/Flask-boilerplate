from flask import render_template
from rvn.Model.Model import Cve,products_schema,app
import simplejson as json


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/rayvyn', methods=['GET'])
def rayvyn():
    cves = []

    # jsonify(result))
    # print (list(list(data)))
    # data = [["Tiger Nixon", "System Architect", "Edinburgh", "5421", "2011/04/25"],
    #         ["Garrett Winters", "Accountant", "Tokyo", "8422", "2011/07/25", "$170,750"],
    #         ["Ashton Cox", "Junior Technical Author", "San Francisco", "1562", "2009/01/12", "$86,000"],
    #         ["Cedric Kelly", "Senior Javascript Developer", "Edinburgh", "6224", "2012/03/29", "$433,060"]
    #
    #  ]
    return render_template('rayvyn.html')

@app.route('/getData', methods=['GET'])
def getData():
    f = []
    data = Cve.query.filter(Cve.impact >= 7.5, Cve.active == 1).all()
    result = products_schema.dump(data)
    for cve in result:
        desc = str(cve['description']).replace('[', '').replace(']', '')
        cve['description'] = desc
        f.append(list(cve.values()))

        # print(f)
    cve = json.dumps(f)
    # f.append(list(result.values()))

    # print(f)
    # #data = Cve.query.all()
    # data = '[["Tiger Nixon", "System Architect", "Edinburgh", "5421", "2011/04/25", "$4555"],["Garrett Winters", "Accountant", "Tokyo", "8422", "2011/07/25", "$170,750"],["Ashton Cox", "Junior Technical Author", "San Francisco", "1562", "2009/01/12", "$86,000"],["Cedric Kelly", "Senior Javascript Developer", "Edinburgh", "6224", "2012/03/29", "$433,060"]]'
    # cve = [['CVE-2016-11085', '["php/qmn_options_questions_tab.php in the quiz-master-next plugin before 4.7.9 for WordPress allows CSRF, with resultant stored XSS, via the question_name parameter because js/admin_question.js mishandles parsing inside of a SCRIPT element."]', '2020-08-21T15:21Z', 'NETWORK', 'nist', 6.5]]

    # print(data)
    # data = '[{"Name":"tif", "Age":"7"},{"Name":"Bulbul", "Age":"17"}]'
    # print((list(result)))
    return str(cve.capitalize())
