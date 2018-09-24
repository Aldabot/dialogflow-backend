from flask import Flask, jsonify, make_response
from flask import request


def balance(req):

    user_exists = False

    if user_exists == True:
        salida = make_response(jsonify(
            {'fulfillmentText': 'Tu saldo actual es: XXX'}))
        return salida

    if user_exists == False:
        return make_response(jsonify({'fulfillmentText': '',
                                      'fulfillmentMessages': [
                                          {
                                              'platform': 'FACEBOOK',
                                              'payload': {
                                                          "facebook": {
                                                              "attachment": {
                                                                  "type": "template",
                                                                  "payload": {
                                                                      "template_type": "button",
                                                                      "text": "Para saber tu saldo conecta tu banco 🔗",
                                                                      "buttons": [
                                                                          {
                                                                              "type": "web_url",
                                                                              "url": "https://www.alda.bot/faq",
                                                                              "title": "Conectar",
                                                                              "webview_height_ratio": "full",
                                                                              "messenger_extensions": "false"
                                                                          }
                                                                      ]
                                                                  }
                                                              }
                                                          }
                                              }
                                          }
                                      ]
                                      }
                                     )
                             )


def fake_balance(req):
    return make_response(jsonify({'fulfillmentText': '',
                                  'fulfillmentMessages': [
                                      {
                                          'platform': 'FACEBOOK',
                                          'payload': {
                                              "facebook": {
"text": "Buenas Gabriel!👋\n\n\
Visa Electron (7394): -524€\nVisa Classic (3780): 0€\nCuenta (9373): 1.612€\nCuenta (2376): 1.500€\nCuenta Imagin: 100€\n\n\
Total: 2.688€ 📈 ",

                                                      "quick_replies": [
                                                          {
                                                              "content_type": "text",
                                                              "title": "Donde va mi dinero🔎",
                                                              "payload": "where_is_my_money_going"
                                                          },
                                                          {
                                                              "content_type": "text",
                                                              "title": "Enviar dinero💸",
                                                              "payload": "Send_money"
                                                          }
                                                      ]
                                                  }
                                          }
                                      }
                                  ]
                                  }
                                 )
                         )
