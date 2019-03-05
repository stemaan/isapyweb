from bs4 import BeautifulSoup
import requests

url = 'https://www.lotto.pl/'
response = requests.get(url)
soup = BeautifulSoup(response.text, features='html.parser')

div = soup.find('div', attrs={'class': 'resultsItem lotto'})
children = div.findChildren('span', recursive=True)
date, time, *results = children

# bez list comprehension
results_as_text = list()
for result in results:
    results_as_text.append(result.text)

print(results_as_text)

# przykład z list comprehension
results_as_text = [result.text for result in results]

print(results_as_text)
