import json
import re
import pandas as pd
import locale

from flask import Flask, jsonify, make_response
from flask import request


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
                                                          int(amount)) + '€'
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
                                  'A continuación te muestro los mejores préstamos que te ofrecen ' +
                                  '{:n}'.format(amount) + '€'
                              ]}})

        lenders_df = pd.read_csv('https://s3-eu-west-1.amazonaws.com/aldachatbot/lenders.csv', delimiter=";", header=0)

        for index, row in lenders_df.iterrows():
            print("Checking " + row["Lender"])
            if row['Min_Amt'] <= amount <= row['Max_Amt']:
                print('Including ' + row['Lender'])
                response.append({
                    'card': {
                        'title': row['Lender'],
                        'subtitle': 'Hasta ' + '{:n}'.format(row['Max_Amt']) + "€ \n TAE desde "
                                    + str(row['Min_TAE']) + "% \n " + row['Subtitle'],
                        'imageUri': row['Image_url'],
                        'buttons': [
                            {
                                'text': 'Seleccionar',
                                'postback': row['Url']
                            },
                            {
                                'text': 'Más información',
                                'postback': row['Url']
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
                                     'Quiero 60.000€',
                                     'Quiero menos de 60.000€',
                                     'Ayúdame'
                                 ]
                             }
                         }
                     ]}))
