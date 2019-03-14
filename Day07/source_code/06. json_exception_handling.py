from json import JSONDecodeError

import requests

url = 'http://swapi.co/api/pxlanets/999/'
bad_response = requests.get(url)

try:
    data = bad_response.json()
except JSONDecodeError as err:
    print(err)
    data = bad_response.text

print('-'*40)
print('Real response:')
print(data)
