# przykład korzystania z prawdziwego API które wymaga podania klucza uwierzytelniającego

from urllib.parse import urljoin
from helpers import handle_response
import requests

api_url = 'https://developers.zomato.com/api/v2.1/'
resource = 'cities'
url = urljoin(api_url, resource)

request_parameters = {'q': 'Krakow'}
response = requests.get(url, params=request_parameters)
response_data = handle_response(response)

# otrzymaliśmy staus_code 403, potrzebujemy przekazać klucz do uwierzytelnienia w nagłówku zapytania
# klucz otrzymasz po rejestracji na https://developers.zomato.com/api
print(response_data)


print('-'*20)
resource = 'cities'
url = urljoin(api_url, resource)
request_headers = {'user-key': '61237b96-------'} # to fragment mojego klucza, z wiadomych powodów wstaw tu swój klucz
response = requests.get(url, params=request_parameters, headers = request_headers)
response_data = handle_response(response)
print(response_data)
