from urllib.parse import urljoin

import requests

API_URL = 'https://swapi.co/api/'

response = requests.get(API_URL)
# # __str__ of `requests.Response` is its status code
print(response)
print(response.status_code)
# # response content is bytes, but looks familiar to JSON?
print(response.content)
print(type(response.content))
#
people_endpoint = urljoin(API_URL, 'people/')
print(people_endpoint)
people_response = requests.get(people_endpoint)

# print(people_response.content)
#
luke_skywalker_endpoint = urljoin(people_endpoint, '1')
print(luke_skywalker_endpoint)
luke_skywalker_response = requests.get(luke_skywalker_endpoint)
print(luke_skywalker_response.json())
obiekt = luke_skywalker_response.json()
print(obiekt['name'])
print(obiekt['hair_color'])