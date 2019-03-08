import requests
from parsel import Selector

url = 'http://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'
text = requests.get(url).text
selector = Selector(text=text)

# tu definiujemy wzorzec wyszukiwania, zwróć uwagę na (.*) - ten element nas interesuje
pattern = r'Name:\s*(.*)'

# zwracana jest kolekcja - analogia do get_all()
print(selector.xpath('//a[contains(@href, "image")]/text()').re(pattern))

# odpowiednik metody get() dla wyrażeń regularnych
print(selector.xpath('//a[contains(@href, "image")]/text()').re_first(pattern))
