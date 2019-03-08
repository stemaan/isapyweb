import re

from bs4 import BeautifulSoup
import requests

url = 'https://www.lotto.pl/'
response = requests.get(url)
soup = BeautifulSoup(response.text, features='html.parser')

result_lotto_div = soup.find('div', attrs={'class': 'resultsItem lotto'})
result_number_div = result_lotto_div.find('div', class_='resultnumber')
results = result_number_div.find_all(string=re.compile('\d{1,2}'))
print(results)
