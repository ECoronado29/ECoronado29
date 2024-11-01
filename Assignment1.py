import sys
import string
import requests
from collections import Counter
import json

#Fetch CityBikes API
url = "http://api.citybik.es/v2/networks"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  #Load the JSON data
    
    #Get city names
    city_list = []
    city_set = set()  #Set to store unique cities
    for network in data["networks"]:
        city = network["location"]["city"]
        if city:  
            city_list.append(city.lower()) 
            city_set.add(city.lower())  #Add city to set for uniqueness
    
    #Count occurrences of each city
    city_counter = Counter(city_list)
    
    #Sort the cities by the number of networks (descending), then alphabetically by city name
    sorted_cities = sorted(city_counter.items(), key=lambda x: (-x[1], x[0]))
    
    #Output the total number of unique cities
    print("Total number of unique cities with bike-sharing networks:", len(city_set))
    
    #Output the top ten cities
    print("\nTop ten cities with the most bike-sharing systems:")
    for city, count in sorted_cities[:10]:  #Display top 10
        print(city.capitalize(), count)
else:
    print(f"Failed to retrieve data: {response.status_code}")
