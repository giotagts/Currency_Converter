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


quotes=[
{   
    "input": {
        "amount": 0.9,
        "currency": "CNY"
    },
    "output": {
        "AUD": 0.20, 
    }
}
]
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

    if len(args.input_currency)!=3:
        args.input_currency=symb2code(args.input_currency).decode("utf-8")


    if(str(args.input_currency) != base):
        in_cr=geturl.json()['quotes'][base+''+str(args.input_currency)]
    else:
        in_cr=args.amount


    text= '{\n\t"input": {\n\t\t"amount":'+str(args.amount)+',\n\t\t"currency": "'+ str(args.input_currency)+'"\n\t},\n\t"output": {'

    if args.output_currency is not None:
        out_cr=geturl.json()['quotes'][base+''+str(args.output_currency)]
        out_am=conv(float(in_cr),float(out_cr),args.amount)
        text=text+ '\t\t"'+str(args.output_currency)+'": '+str(out_am)

    else:
        for i in geturl.json()['quotes']:
            out_am=conv(float(in_cr),float(geturl.json()['quotes'][i]),args.amount)
            code=i[3:]
            text=text +'\t\t"'+str(code)+'": '+str(out_am)
    results.append(text)



    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)





app.run()


