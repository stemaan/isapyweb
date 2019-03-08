import os
from parsel import Selector


def load_offer(_offer):
    file_name = os.path.join('data', _offer)
    with open(file_name, encoding='utf-8') as _file_in:
        _data = _file_in.read()

    return _data


def get_details(_data):
    selector = Selector(text=_data)

    # selector css object wskazujący na tytuł strony
    # zapisy alternatywne
    print(selector.css('title::text'))
    print(selector.css('head > title::text'))

    # by wydobyć tekst z HTML trzeba skorzystać z konstrukcji poniżej
    # zapisy alternatywne
    print(selector.css('title::text').get())
    print(selector.css('head > title::text').get())

    # TODO: dodaj kolejne etykietki
    # Uwaga! - Te selektory zostały wygenerowane przez Chrome. FF może zapisać inaczej

    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(2) > span::text').get(), ' ', end="")
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(2) > div > a::attr(title)').get())

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
