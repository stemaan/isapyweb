import requests
from parsel import Selector

url = 'http://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'
text = requests.get(url).text
selector = Selector(text=text)

# wydobycie wszystkich linków na stronie,
# ktorych atrybut href zawierat tekst 'image'
links = selector.xpath('//a[contains(@href, "image")]')
print(links.getall())

for index, link in enumerate(links):
    args = (index, link.xpath('@href').get(), link.xpath('img/@src').get())
    print('Link number %d points to url %r and image %r' % args)
