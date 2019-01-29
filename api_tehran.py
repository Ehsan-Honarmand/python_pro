# Ip Info your place
import requests

response = requests.get('https://ipinfo.io')
catg = ['ip','city','region','country','loc','org']
catgr = ['Ip Address: ','city: ','Region: ','country: ','location(lat & long): ','internet service: ']

for i in range(len(catg)):
    print(catgr[i],response.json()[catg[i]], end = '\n')