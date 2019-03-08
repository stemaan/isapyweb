import os
from parsel import Selector


def load_offer(_offer):
    file_name = os.path.join('data', _offer)
    with open(file_name, encoding='utf-8') as _file_in:
        _data = _file_in.read()

    return _data


def get_details(_data):
    selector = Selector(text=_data)

    # selector xpath object wskazujący na tytuł strony
    print(selector.xpath('//title/text()'))

    # by wydobyć tekst z HTML trzeba skorzystać z konstrukcji poniżej
    print(selector.xpath('//title/text()').get())  # pojedynczy, pierwszy rezultat

    # TODO: dodaj kolejne etykietki
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[2]/span/text()').get(), ' ', end="")
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[2]/div/a/@title').get())

    # TODO: dodaj wyszukiwanie waluty
    # TODO: dodaj wyszukiwanie lokalizacji


offers = (
    'ford-focus-salon-polska-klima-sprawy-zadbany-polecam-ID6BxpMS.html',
    'ford-focus-1-6-tdci-salon-polska-serwis-aso-klima-ID6BwGlg.html'
)
for offer in offers:
    data = load_offer(offer)
    get_details(data)
    print('-' * 40)
