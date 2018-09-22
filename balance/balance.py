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
                                              'card': {
                                                'title': 'Para consultar tu saldo conecta tu banco 🔗',
                                                  'buttons': [
                                                      {
                                                          'text': 'Conectar',
                                                          'postback': 'https://www.alda.bot/'
                                                      }
                                                  ]
                                              }
                                          }
                                      ]
                                      }
                                     )
                             )
