# -*- encoding: utf-8 -*-
from json_api import countries

def conv(in_curr,out_curr,in_amount):
    base_amount=in_amount/in_curr
    out_amount=base_amount*out_curr
    return out_amount



def code2symb(b):
    for k in countries.json()['results']:
        if countries.json()['results'][k]['currencyId']==b:
            symbol=countries.json()['results'][k]['currencySymbol']
            return symbol
            break

def symb2code(d):
    for l in countries.json()['results']:
        if str(countries.json()['results'][l]['currencySymbol'].encode("utf-8"))==d:
            code3=countries.json()['results'][l]['currencyId']
            return str(code3)
            break


def symb2print(c):
    if code2symb(c) is not None:
        toprint= code2symb(c)
    else:
        toprint=''
    return toprint

