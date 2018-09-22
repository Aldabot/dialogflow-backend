import json
import re
import pandas as pd
import locale

from flask import Flask, jsonify, make_response
from flask import request

from lenders.lenders import best_lenders

app = Flask(__name__)

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

@app.route('/test', methods=['POST', 'GET'])
def get_test():
    print("Request received")
    print(request.json)
    return jsonify('{"Status" : "OK"}'), 200


# endpoint for the web hook
@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    print('the action is ' + action)
    if action == 'action.alda.loan.application':
        print('Executing action.alda.loan.application')
        return best_lenders(req)
    if action == 'action.dni.validation':
        return validateDni(req)
    if action == 'action.phone.validation':
        return validateTlf(req)
    if action == 'action.email.validation':
        return validateEmail(req)
    return req


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)
