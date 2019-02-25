from urllib.parse import urljoin

import requests

API_URL = 'https://jsonplaceholder.typicode.com/'
posts_endpoint = 'posts/'
url = urljoin(API_URL, posts_endpoint)

# schema of post resource
# {
#   "userId": int,
#   "id": int,
#   "title": str,
#   "completed": boolean
# }

example_data = {
    'userId': 123,
    'id': 321,
    'title': 'infoshare test 123',
    'completed': True
}

# wysyłanie danych jako pary  klucz=wartość
response = requests.post(url, data=example_data)
print(response)
print(response.status_code)
print(response.content)

# wysyłanie danych jako JSON poprzez ustawienie headera; ważne (!)
headers = {
    'Content-type': 'application/json; charset=UTF-8'
}
response = requests.post(url, json=example_data, headers=headers)
print(response)
print(response.status_code)
print(response.content)
print(response.headers)
