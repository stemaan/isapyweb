import requests
from parsel import Selector

url = 'http://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'
text = requests.get(url).text
selector = Selector(text=text)
# selector xpath object wskazujący na tytuł strony
print(selector.xpath('//title/text()'))
# by wydobyć tekst z HTML trzeba skorzystać z konstrukcji poniżej
print(selector.xpath('//title/text()').getall())  # lista
print(selector.xpath('//title/text()').get())  # pojedynczy, pierwszy rezultat
