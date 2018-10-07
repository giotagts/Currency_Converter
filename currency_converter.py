import argparse
from converter import conv
from converter import code2symb
from converter import symb2code
from converter import symb2print
from json_api import geturl
from json_api import base
import json


parser = argparse.ArgumentParser(description='Use this to convert currencies')
parser.add_argument('--amount',type=float, help='a valid amount for the accumulator', required=True)
parser.add_argument('--input_currency', help='a valid 3 letter code', required=True)
parser.add_argument('--output_currency', help='a valid 3 letter code',required=False)

args = parser.parse_args()

if len(args.input_currency)!=3:
    args.input_currency=symb2code(args.input_currency).decode("utf-8")


if(str(args.input_currency) != base):
    in_cr=geturl.json()['quotes'][base+''+str(args.input_currency)]
else:
    in_cr=args.amount


print '{\n\t"input": {\n\t\t"amount":'+str(args.amount)+',\n\t\t"currency": "'+ str(args.input_currency)+'"\n\t},\n\t"output": {'

if args.output_currency is not None:
    out_cr=geturl.json()['quotes'][base+''+str(args.output_currency)]
    out_am=conv(float(in_cr),float(out_cr),args.amount)
    print '\t\t"'+str(args.output_currency)+'": '+str(out_am)

else:
    for i in geturl.json()['quotes']:
        out_am=conv(float(in_cr),float(geturl.json()['quotes'][i]),args.amount)
        code=i[3:]
        print '\t\t"'+str(code)+'": '+str(out_am)





