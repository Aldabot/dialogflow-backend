from flask import Flask, jsonify, make_response
from flask import request


def transactions(req):

    user_exists = False

    if user_exists == True:
        salida = make_response(jsonify(
            {'fulfillmentText': 'Tus movimientos: XXX'}))
        return salida

    if user_exists == False:
        return make_response(jsonify({'fulfillmentText': '',
                                      'fulfillmentMessages': [
                                          {
                                              'card': {
                                                  'title': 'Para consultar tus movimientos conecta tu banco 🔗',
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
