import json
import requests
from pprint import pprint
from bs4 import BeautifulSoup

headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:66.0) Gecko/20100101 Firefox/66.0"}
CLOTHES_URL = "https://dressmyrun.com"

def get_clothes(temperature, wind_speed):
  temp_url = 'temp=' + str(temperature)+'C'
  wind_url = '&wind='+ str(wind_speed)+'mph'
  web_request = CLOTHES_URL + '/conditions?' + temp_url + wind_url
  response = requests.get(web_request)
  products = get_products(response)
  return products

def get_content_tag(products_container, tag):
  content_tag = [element.text for element in products_container.find_all(tag)]
  content_tag = [item.strip() for item in content_tag]
  return content_tag

def get_products(response):
  soup = BeautifulSoup(response.text, "html.parser")
  products_container = soup.find("div", {'class': 'section-content'})
 
  names_h4 = get_content_tag(products_container,'h4')
  names_p = get_content_tag(products_container,'p')
  names_p = [item.replace("\r\n\t\t\t\t", " ") for item in names_p]
  return names_p
  #return names_h4, names_p

      