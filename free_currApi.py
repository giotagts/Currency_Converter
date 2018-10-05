

import requests
countries=requests.get('https://free.currencyconverterapi.com/api/v6/countries')

def code2symb(b):
    for k in countries.json()['results']:
        if countries.json()['results'][k]['currencyId']==b:
            symbol=countries.json()['results'][k]['currencySymbol']
            return symbol
            break

def symb2code(d):
    for l in countries.json()['results']:
        if countries.json()['results'][l]['currencySymbol']==d:
            code3=countries.json()['results'][l]['currencyId']
            return code3
            break
