from urllib.parse import urljoin

import requests

API_URL = 'https://jsonplaceholder.typicode.com/'
posts_endpoint = 'posts/'
posts_url = urljoin(API_URL, posts_endpoint)
# schema of post resource
# {
#   "userId": int,
#   "id": int,
#   "title": str,
#   "completed": boolean
# }
example_data = {
    'title': 'infoshare test 123',
}
resource_id = 1
url = urljoin(posts_url, str(resource_id))
get_response = requests.get(url)
print(get_response.content)
response = requests.put(url, data=example_data)
print(response)
print(response.status_code)
print(response.content)
