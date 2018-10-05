import argparse
from converter import conv
from free_currApi import symb
from json_api import r
from json_api import base
import json


parser = argparse.ArgumentParser(description='Use this to convert currencies')
parser.add_argument('--amount',type=float, help='a valid amount for the accumulator', required=True)
parser.add_argument('--input_currency', help='a valid 3 letter code', required=True)
parser.add_argument('--output_currency', help='a valid 3 letter code',required=False)


args = parser.parse_args()
#print args

if(str(args.input_currency) != base):
    in_cr=r.json()['quotes'][base+''+str(args.input_currency)]
else:
    in_cr=args.amount


if args.output_currency:
    out_cr=r.json()['quotes'][base+''+str(args.output_currency)]
    #print ''+str(args.amount)+' '+str(args.input_currency)+' = '+str(args.output_currency)
    out_am=conv(float(in_cr),float(out_cr),args.amount)
    print '' + str(symb(str(args.input_currency)))+''+ str(args.amount) +' ('+str(args.input_currency)+') = '+ str(symb(str(args.output_currency)))+''+str(out_am) +' (' + str(args.output_currency)+')'
else:
    for i in r.json()['quotes']:
        out_am=conv(float(in_cr),float(r.json()['quotes'][i]),args.amount)
        code=i[3:]
        print '' + str(symb(str(args.input_currency)))+''+ str(args.amount) +' ('+str(args.input_currency)+') = '+ str(out_am) +' (' + str(code)+ ')'
