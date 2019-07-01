import json
from constants import WEATHER_API_KEY
from Clothes_Scrapping import get_clothes
import requests


api_url = "http://api.apixu.com/v1/"

WEATHER_API_KEY = WEATHER_API_KEY


api_key = '?key='+WEATHER_API_KEY 

def add_api_action_and_city(api_action, city):
  city_request = '&q='+city
  api_action_link = api_url + api_action + api_key + city_request
  return api_action_link 

def get_city_weather(city):
  api_action = 'current.json'
  api_request = add_api_action_and_city(api_action, city)
  response = requests.get(api_request)
  dirty_info = response.json()
  city_info = {}
  city_info['name'] = dirty_info['location']['name']
  city_info['weather'] = dirty_info['current']['condition']['text']
  city_info['icon'] = dirty_info['current']['condition']['icon']
  city_info['temperature'] = dirty_info['current']['temp_c']
  return city_info

def get_city_weather_forecast(city, days):
  city_request = '&q='+city
  api_action = 'forecast.json'
  days_request = '&days='+str(days)
  api_request = api_url + api_action + api_key + city_request + days_request
  response = requests.get(api_request)
  dirty_info = response.json()
  forecast = response.json()['forecast']['forecastday']
  forecast_days = []
 
  for days in forecast:
    day = {}
    try:
      forecast_day = forecast[0]
      day['date'] = forecast_day['date']
      day['maxtemp_c'] = forecast_day['day']['maxtemp_c']
      day['mintemp_c'] = forecast_day['day']['mintemp_c']
      day['wind_mph'] = forecast_day['day']['maxwind_mph']
      day['condition'] = forecast_day['day']['condition']['text']
      day['clothes'] = get_clothes(day['maxtemp_c'], day['wind_mph'])
      forecast_days.append(day)
    except:
      pass
  return forecast_days    
  


