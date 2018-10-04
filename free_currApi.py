

import requests
countries=requests.get('https://free.currencyconverterapi.com/api/v6/countries')

def symb(b):
    for k in countries.json()['results']:
        if countries.json()['results'][k]['currencyId']==b:
            symbol=countries.json()['results'][k]['currencySymbol']
            return symbol
            break
    
