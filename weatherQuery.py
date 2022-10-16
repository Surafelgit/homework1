#url = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=9a7ad1c9a2fe641ded4ee571f56df333" 

import requests
import json
import math
 

KEY = "9a7ad1c9a2fe641ded4ee571f56df333" #Api key from openweathermap.org
 
url = "http://api.openweathermap.org/data/2.5/weather?" #url 
 

city = input("Enter City: ") #user inputs the name of city 
 

fullurl = url + "appid=" + KEY + "&q=" + city #concatenate url with api key and city
 
response = requests.get(fullurl) #get a resposne from openweathermap.org
 
formatpy = response.json() #formats the response

#print(response.status_code)
 

if formatpy["cod"] == "404":
   print("Error Retreiving the data")
 
 
else:
   
    main = formatpy["main"] #main holds array of info about weather
 
    
    temperature = main["temp"]
    temperature = 1.8*(temperature - 273.15) + 32 # convert K to Fh
    temperature = math.ceil(temperature)
    
    weather = formatpy["weather"]
    weathertype = weather[0]["main"]

  
    
    print('Displaying current weather data...')
 
 
    t ="Temperature(F): "
    ty ="Type of weather: "
    print(f'{t}{temperature}')
    print(f'{ty}{weathertype}')
 
 

