# -*- encoding: utf-8 -*-
import requests
geturl=requests.get('http://www.apilayer.net/api/live?access_key=9be442e4e401c675067e4876ab9d68d9')
countries=requests.get('https://free.currencyconverterapi.com/api/v6/countries')
base=geturl.json()['source']

