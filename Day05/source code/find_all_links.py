from bs4 import BeautifulSoup
import requests

url = 'http://www.onet.pl'
response = requests.get(url)
soup = BeautifulSoup(response.text, features='html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))