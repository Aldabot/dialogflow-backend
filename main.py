import json
import re

from flask import Flask, jsonify, make_response
from flask import request

app = Flask(__name__)


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


def best_lenders(req):
    try:
        amount = req.get('queryResult').get('parameters').get('amount').get('number')
    except AttributeError:
        return 'amount not recognized'

    if amount < 50:
        print('Amount under 50 euros')
        return make_response(jsonify({'fulfillmentText': 'Ninguna entidad ofrece menos de 50€...',
                                      'fulfillmentMessages': [
                                          {
                                              "quickReplies": {
                                                  "title": 'Ninguna empresa ofrece menos de 50€...',
                                                  'quickReplies': [
                                                      'Quiero 50€',
                                                      'Quiero más de 50€',
                                                      'Ayúdame'
                                                  ]
                                              }
                                          }
                                      ]}))
    if amount <= 300:
        print('Amount between 50 and 300')
        return make_response(jsonify({'fulfillmentText': '',
                                      'fulfillmentMessages': [
                                          {
                                              'text': {
                                                  'text': [
                                                      'A continuación te muestro los mejores préstamos que te ofrecen ' + str(
                                                          round(amount, 0)) + '€'
                                                  ]
                                              }
                                          },
                                          {
                                              'card': {
                                                  'title': 'Vivus',
                                                  'subtitle': 'Hasta 300€ 30 días \n 30 días gratis \n Sin comisiones',
                                                  'imageUri': 'https://s3-eu-west-1.amazonaws.com/aldachatbot/vivus.png',
                                                  'buttons': [
                                                      {
                                                          'text': 'Seleccionar',
                                                          'postback': 'https://www.vivus.es/'
                                                      },
                                                      {
                                                          'text': 'Más información',
                                                          'postback': 'https://www.vivus.es/'
                                                      }
                                                  ]

                                              }
                                          },
                                          {
                                              'card': {
                                                  'title': 'Wonga',
                                                  'subtitle': 'Hasta 300€ 60 días \n 15 días gratis \n Sin comisiones',
                                                  'imageUri': 'https://s3-eu-west-1.amazonaws.com/aldachatbot/wonga.png',
                                                  'buttons': [
                                                      {
                                                          'text': 'Seleccionar',
                                                          'postback': 'https://www.wonga.es/'
                                                      },
                                                      {
                                                          'text': 'Más información',
                                                          'postback': 'https://www.wonga.es/'
                                                      }
                                                  ]

                                              }
                                          },
                                          {
                                              'card': {
                                                  'title': 'Qué Bueno!',
                                                  'subtitle': 'Hasta 300€ 34 días \n Sin comisiones',
                                                  'imageUri': 'https://s3-eu-west-1.amazonaws.com/aldachatbot/quebueno.png',
                                                  'buttons': [
                                                      {
                                                          'text': 'Seleccionar',
                                                          'postback': 'https://www.quebueno.es/'
                                                      },
                                                      {
                                                          'text': 'Más información',
                                                          'postback': 'https://www.quebueno.es/'
                                                      }
                                                  ]

                                              }
                                          },
                                          {
                                              "quickReplies": {
                                                  "title": 'Ten en cuenta que estos préstamos empeoran tu historial crediticio. En ocasiones, el mejor préstamo es el que no se pide.',
                                                  'quickReplies': [
                                                      'Gracias!',
                                                      'Estoy en ASNEF',
                                                      'Historial?',
                                                      'Más ayuda'
                                                  ]
                                              }
                                          }
                                      ]}))

    if amount <= 50000:
        print('Amount between 300 and 50.000€')
        response = []
        response.append({'text': {
                              'text': [
                                  'A continuación te muestro los mejores préstamos que te ofrecen ' + str(
                                      round(amount,0)) + '€'
                              ]}})

        if 6000 <= amount <= 50000:
            print ('Cetelem added')
            response.append({
              'card': {
                  'title': 'Cetelem',
                  'subtitle': 'Hasta 50.000€ 8 años \n TAE desde 6,12% \n Online y sin comisiones',
                  'imageUri': 'https://s3-eu-west-1.amazonaws.com/aldachatbot/cetelem.png',
                  'buttons': [
                      {
                          'text': 'Seleccionar',
                          'postback': 'https://www.cetelem.es/'
                      },
                      {
                          'text': 'Más información',
                          'postback': 'https://www.cetelem.es/'
                      }]}})

        if 4000 <= amount <= 15000:
            print('Cofidis added')
            response.append({
              'card': {
                  'title': 'Cofidis',
                  'subtitle': 'Hasta 15.000€ 8 años \n TAE desde 6,12% \n Online y sin comisiones',
                  'imageUri': 'https://s3-eu-west-1.amazonaws.com/aldachatbot/cofidis.png',
                  'buttons': [
                      {
                          'text': 'Seleccionar',
                          'postback': 'https://www.cofidis.es/'
                      },
                      {
                          'text': 'Más información',
                          'postback': 'https://www.cofidis.es/'
                      }]}})

        if 500 <= amount <= 5000:
            print('Creditea added')
            response.append({
              'card': {
                  'title': 'Creditea',
                  'subtitle': 'Hasta 5.000€ 3 años \n TAE desde 24,90% \n Online y sin comisiones',
                  'imageUri': 'https://s3-eu-west-1.amazonaws.com/aldachatbot/creditea.png',
                  'buttons': [
                      {
                          'text': 'Seleccionar',
                          'postback': 'https://www.creditea.es/'
                      },
                      {
                          'text': 'Más información',
                          'postback': 'https://www.creditea.es/'
                      }]}})

        response.append({
            'quickReplies': {
                'title': 'Además de estas opciones, es posible que tu banco te ofrezca un préstamo preconcedido: este tipo de préstamo es el más rápido pero también es el más caro!',
                'quickReplies': [
                    'Gracias!',
                    'TAE?'
                ]
            }
        })

        return make_response(jsonify({'fulfillmentMessages': response}))

    if amount > 60000:
        print('Amount above 60.000€')
        return make_response(
            jsonify({'fulfillmentText': 'Ninguna entidad ofrece más de 60.000€ sin un aval hipotecario',
                     'fulfillmentMessages': [
                         {
                             'quickReplies': {
                                 'title': 'Ninguna entidad ofrece más de 60.000€ sin un aval hipotecario',
                                 'quickReplies': [
                                     'Quiero 50.000€',
                                     'Quiero menos de 50.000€',
                                     'Ayúdame'
                                 ]
                             }
                         }
                     ]}))


def validate_amount_term(req):
    amount = req.get('queryResult').get('parameters').get('Amount').get('number')
    term = req.get("queryResult").get('parameters').get('Term-days').get('number')
    validAmount = True
    validTerm = True
    if amount > 300 or amount < 50:
        validAmount = False
    if term > 60:
        validTerm = False

    if validAmount & validTerm:
        salida = make_response(jsonify(req.get('queryResult').get('fulfillmentMessages')))
    else:
        textoError = ''
        if validAmount == False:
            textoError = textoError + 'Solo podemos ofrecerte entre 50 y 300 Euros, indica otra cantidad por favor. '
        if validTerm == False:
            textoError = textoError + 'Lamentablemente no podemos ofrecerte más de 60 días. '
        salida = make_response(jsonify({'fulfillmentText': textoError}))
    return salida


def validateDni(req):
    identificador = req.get('queryResult').get('parameters').get('DNI')
    nifRegex = '^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$'
    nieRegex = '^[XYZ][0-9]{7}[TRWAGMYFPDXBNJZSQVHLCKE]$'
    validNif = False
    validNie = False
    if re.search(nifRegex, identificador):
        validNif = True

    if re.search(nieRegex, identificador):
        validNie = True

    if validNif == False and validNie == False:
        salida = make_response(jsonify(
            {'fulfillmentText': 'El formato del identifidador Nif o Nie no es correcto, vuelva a introducirlo.'}))
        return salida

    return make_response(jsonify(req.get('queryResult').get('fulfillmentMessages')))


def validateTlf(req):
    tlf = req.get('queryResult').get('parameters').get('phone-number')
    tlfRegex = '^[0-9]{9}$'
    validTlf = False
    if re.search(tlfRegex, tlf):
        validTlf = True

    if validTlf == False:
        salida = make_response(jsonify({
            'fulfillmentText': 'El formato del telefono introducido no es correcto, ha de ser 999999999 , vuelva a introducirlo.'}))
        return salida

    return make_response(jsonify(req.get('queryResult').get('fulfillmentMessages')))


def validateEmail(req):
    email = req.get('queryResult').get('parameters').get('email')
    emailRegex = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
    validEmail = False
    if re.search(emailRegex, email):
        validEmail = True

    if validEmail == False:
        salida = make_response(
            jsonify({'fulfillmentText': 'El formato del email introducido no es correcto, vuelva a introducirlo.'}))
        return salida

    return make_response(jsonify(req.get('queryResult').get('fulfillmentMessages')))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)
