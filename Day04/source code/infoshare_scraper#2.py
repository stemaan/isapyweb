# rozbudowana wersja crawlera

import requests
import logging
import sys


def get_page(city):
    url = 'https://infoshareacademy.com/?s&city={}'.format(city)
    logging.info('ściągamy stronę z której wyciągniemy dane:{}'.format(url))
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.text


def get_data(content):
    logging.info('szukamy elementu z przypisaną klasą "course-title"')
    course_pattern = '"course-title">'
    opening_tag = '<span>'
    closing_tag = '</span>'

    # pozycja w zmiennej, wskazująca na rozpoczęcie nazwy szkolenia; uzględnia rozmiar tagów
    course_title_pos = content.find(course_pattern) + sum([len(course_pattern), len(opening_tag)])

    # pozycja w pliku, wskazująca na zamknięcie tagu. Zwróć uwagę na użycie 'course_title_pos'
    closing_tag_pos = content.find(closing_tag, course_title_pos)

    # wyciągamy zawartość
    title = content[course_title_pos:closing_tag_pos]

    logging.info('szukamy elementu z datą')
    date_pattern = 'course-info__paragraph course-info__paragraph--date">'
    closing_tag = '</p>'
    date_pos = content.find(date_pattern, closing_tag_pos) + len(date_pattern)
    closing_tag_pos = content.find(closing_tag, date_pos)

    date = content[date_pos:closing_tag_pos]

    return title, date


logging.basicConfig(filename='{}.log'.format(sys.argv[0]), level=logging.DEBUG)
miasta = 'Gdańsk', 'Kraków', 'Lublin', 'Poznań', 'Warszawa', 'Wrocław'

for miasto in miasta:
    dane_html = get_page(miasto)
    kurs_raw, data_raw = get_data(dane_html)
    print('Miasto: {}, Kurs: {}, Data: {}'.format(miasto, kurs_raw, data_raw))
