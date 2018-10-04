import requests
r=requests.get('http://www.apilayer.net/api/live?access_key=9be442e4e401c675067e4876ab9d68d9')
base=r.json()['source']
