from urllib.parse import urljoin

import requests

API_URL = 'https://jsonplaceholder.typicode.com/'
posts_endpoint = 'posts/'
posts_url = urljoin(API_URL, posts_endpoint)
resource_id = 1
url = urljoin(posts_url, str(resource_id))
response = requests.delete(url)
print(response)
print(response.status_code)
print(response.content)
