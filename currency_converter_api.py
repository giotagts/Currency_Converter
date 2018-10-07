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
        input_currency = str(request.args['input_currency'])
    else:
        return "Error: No input currency field provided. Please specify an input currency."

    if 'output_currency' in request.args:
        output_currency = str(request.args['ouput_currency'])
    else:
        output_currency=None
    # Create an empty list for our results
    results = []

    if len(input_currency)!=3:
        input_currency=symb2code(input_currency).decode("utf-8")


    if(input_currency != base):
        in_cr=geturl.json()['quotes'][base+''+str(input_currency)]
    else:
        in_cr=amount

    results=[
    {
        "input" : {
            "amount": amount,
            "currency": input_currency
        }
    }]
        
    if output_currency is not None:
        out_cr=geturl.json()['quotes'][base+''+str(output_currency)]
        out_am=conv(float(in_cr),float(out_cr),amount)

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


