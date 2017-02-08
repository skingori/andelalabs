import requests
import json
import time


def convert_kel_cel(kel_value):
    return int(kel_value - 273.15)
print("Enter City Below")
city = input("")
print("Enter your API KEY below")
key = input('')
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + key

response = requests.get(url)

content = response.content

data = json.loads(content)

temp = data['main']['temp']
sky=data['weather'][0]['main']
pr=data['main']['pressure']

'''Get the main data'''
print ("The weather in " + city + " is: " + str(convert_kel_cel(temp)) + '°' + " ,Sky:" + sky + " ,Pressure:" +str(convert_kel_cel(pr)))
