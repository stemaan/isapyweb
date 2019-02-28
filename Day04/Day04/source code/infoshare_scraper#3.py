# najbardziej rozbudowana wersja crawlera

import requests
import logging
import sys
import os


def get_page(city, title='Python%20od%20podstaw', mode='download'):
    file_name = '{}.{}.html'.format(city, title)
    full_file_name = os.path.join(folder, file_name)

    if mode == 'download':
        url = 'https://infoshareacademy.com/?s&city={}&type={}'.format(city, title)
        logging.info('ściągamy stronę z której wyciągniemy dane:{}'.format(url))
        response = requests.get(url)

        if response.status_code != 200:
            return None

        with open(full_file_name, 'w') as file_out:
            file_out.write(response.text)

        response = response.text

    else:
        logging.info('odczytujemy z dysku plik z którego wyciągniemy dane:{}'.format(full_file_name))
        with open(full_file_name, 'r') as file_in:
            response = file_in.read()

    return response


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


logging.basicConfig(filename='{}.log'.format(sys.argv[0]),
                    format='%(asctime)s,%(msecs)d %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%Y:%H:%M:%S',
                    level=logging.DEBUG)

folder = 'data'
if not os.path.isdir(folder):
    logging.info('zakładamy folder {}'.format(folder))
    os.mkdir(folder)

miasta = 'Gdańsk', 'Kraków', 'Lublin', 'Poznań', 'Warszawa', 'Wrocław'
for miasto in miasta:
    dane_html = get_page(miasto)
#    dane_html = get_page(miasto, mode='load')
    kurs_raw, data_raw = get_data(dane_html)
    print('Miasto: {}, Kurs: {}, Data: {}'.format(miasto, kurs_raw, data_raw))
