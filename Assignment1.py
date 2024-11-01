import sys
import string
import requests
from collections import Counter
import json

#Fetch CityBikes API
url = "http://api.citybik.es/v2/networks"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Load the JSON data
    
    #Get city names
    city_list = []
    for network in data["networks"]:
        city = network["location"]["city"]
        if city:  
            city_list.append(city.lower()) 
    
    #Count 
    city_counter = Counter(city_list)
    
    #Sort the cities by the number of networks
    sorted_cities = sorted(city_counter.items(), key=lambda x: x[1], reverse=True)
    
    #Output top ten cities
    print("Top ten cities with the most bike-sharing systems:")
    for city, count in sorted_cities[:10]:  #top 10
        print(city.capitalize(), count)
else:
    print(f"Failed to retrieve data: {response.status_code}")
