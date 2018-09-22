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
                                                                      "text": "'Para saber tu saldo conecta tu banco 🔗",
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
