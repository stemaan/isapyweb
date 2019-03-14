import json
from pprint import pprint
import requests

url = 'http://swapi.co/api/planets/1/'
response = requests.get(url)

# otrzymaliśmy stringa (notacja JSON) i zamieniamy go na obiekt typu słownik
data = json.loads(response.text)

print(data)
print('-' * 40)
# sposób na ładną wizualizację JSONa
pprint(data)

# inny sposób na uzyskanie słownika z odpowiedzi od API
same_data = response.json()
print(data == same_data)

with open('json_data.json', 'w') as data_file:
    # zrzut słownika do pliku, w postaci JSON, z wcięciami zdef. na 4 spacje
    json.dump(same_data, data_file, indent=4)
