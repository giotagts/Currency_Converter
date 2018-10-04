import argparse
from converter import conv
from json_api import r
from json_api import base
import json


parser = argparse.ArgumentParser(description='Use this to convert currencies')
parser.add_argument('--amount',type=float, help='a valid amount for the accumulator', required=True)
parser.add_argument('--input_currency', help='a valid 3 letter code', required=True)
parser.add_argument('--output_currency', help='a valid 3 letter code',required=False)


args = parser.parse_args()
#print args

in_cr=r.json()['quotes'][base+''+str(args.input_currency)]


if args.output_currency:
    out_cr=r.json()['quotes'][base+''+str(args.output_currency)]
    #print ''+str(args.amount)+' '+str(args.input_currency)+' = '+str(args.output_currency)
    out_am=conv(float(in_cr),float(out_cr),args.amount)
    print ''+ str(args.amount) +' '+str(args.input_currency)+' = '+ str(out_am) +' ' + str(args.output_currency)
else:
    for i in r.json()['quotes']:
        out_am=conv(float(in_cr),float(r.json()['quotes'][i]),args.amount)
        print ''+ str(args.amount) +' '+str(args.input_currency)+' = '+ str(out_am) +' ' + str(i)

