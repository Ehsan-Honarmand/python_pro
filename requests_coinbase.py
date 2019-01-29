import requests

# url api ---> api/geocoding/sunset-sunrise.org/api

respose = requests.get('https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400') 
r = respose.json()   
print(r['results'])

sunrise_dict = r['results']['sunrise']
print(sunrise_dict)