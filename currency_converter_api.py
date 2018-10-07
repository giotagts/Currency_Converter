# -*- encoding: utf-8 -*-
import argparse
from converter import conv
from converter import code2symb
from converter import symb2code
from converter import symb2print
from json_api import geturl
from json_api import base
import json


import flask
from flask import request, jsonify

app = flask.Flask(__name__)


@app.route('/currency_converter', methods=['GET'])
def api_input():
    # Check if an amount and input currency were provided as part of the URL.
    # If yes, assign them to a variable.
    # If no, display an error in the browser.
    if 'amount' in request.args:
        amount = float(request.args['amount'])
    else:
       return "Error: No amount field provided. Please specify an amount."

    if 'input_currency' in request.args:
        input_currency = request.args['input_currency']
        if len(input_currency)!=3:
            input_currency=symb2code(str(input_currency))
        
    else:
        return "Error: No input currency field provided. Please specify an input currency."


    # Create an empty list for our results
    results = []

    


    if(input_currency != base):
        in_cr=geturl.json()['quotes'][base+''+input_currency]
    else:
        in_cr=amount

    results=[
    {
        "input" : {
            "amount": amount,
            "currency": input_currency
        },
    
    }]
        
    if 'output_currency' in request.args:
        output_currency = request.args['output_currency']
        if len(output_currency)!=3:
            output_currency=symb2code(str(output_currency))
        out_cr=geturl.json()['quotes'][base+''+str(output_currency)]
        out_am=conv(float(in_cr),float(out_cr),amount)
        results.append({
                "output" : {
                    output_currency : out_am
                }
        })
        

    else:
        for i in geturl.json()['quotes']:
            out_am=conv(float(in_cr),float(geturl.json()['quotes'][i]),amount)
            code=i[3:]
            results.append({
                "output" : {
                    code : out_am
                }
        })
        



    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)





app.run()


