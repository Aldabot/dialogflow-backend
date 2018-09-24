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
                                              'platform': 'FACEBOOK',
                                              'payload': {
                                                          "facebook": {
                                                              "attachment": {
                                                                  "type": "template",
                                                                  "payload": {
                                                                      "template_type": "button",
                                                                      "text": "Para consultar tus movimientos conecta tu banco 🔗",
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

def fake_transactions(req):
    return make_response(jsonify({'fulfillmentText': '',
                                  'fulfillmentMessages': [
                                      {
                                          'platform': 'FACEBOOK',
                                          'payload': {
                                              "facebook": {
"text": "Lo tengo.\n\n\🚀 143€ Transportes\n🍽️ 189€ Restaurantes\n🛍️ 46€ Supermercado\n🥜 60€ Otros",
                                                      "quick_replies": [
                                                          {
                                                              "content_type": "text",
                                                              "title": "Enviar dinero💸",
                                                              "payload": "where_is_my_money_going"
                                                          },
                                                          {
                                                              "content_type": "text",
                                                              "title": "Quiero ahorrar📈 ",
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
