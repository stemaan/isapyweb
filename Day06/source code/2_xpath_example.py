import requests
from parsel import Selector

url = 'http://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'
text = requests.get(url).text
selector = Selector(text=text)

# wartość atrybutu href tagu o nazwie base
print(selector.xpath('//base/@href').get())
# wydobycie linków zawartych na stronie
print(selector.xpath('//a[contains(@href, "image")]/@href').getall())
# wydobycie linków do obrazów zawartych na stronie
print(selector.xpath('//a[contains(@href, "image")]/img/@src').getall())
