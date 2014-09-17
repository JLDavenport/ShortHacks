#!/usr/bin/python
import requests

apikey = "0def10027afaebb7"

r = requests.get('http://api.wunderground.com/api/'+apikey+'/forecast/q/CA/Burbank.json')
data = r.json()

for day in data['forecast']['simpleforecast']['forecastday']:
    print day['date']['weekday'] + ":"
    print "Conditions: ", day['conditions']
    print "High: ", day['high']['fahrenheit'] + "F", "Low: ", day['low']['fahrenheit'] + "F", '\n'
