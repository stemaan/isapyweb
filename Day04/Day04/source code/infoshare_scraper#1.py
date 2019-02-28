# podstawowa wersja crawlera

import requests

# ściągamy stronę z której wyciągniemy dane
url = 'https://infoshareacademy.com/?s&city=Krakow'
response = requests.get(url)
content = response.text

# szukamy elementu z przypisaną klasą "course-title"
course_pattern = '"course-title">'
opening_tag = '<span>'
closing_tag = '</span>'

# pozycja w zmiennej, wskazująca na rozpoczęcie nazwy szkolenia; uzględnia rozmiar tagów
course_title_pos = content.find(course_pattern) + sum([len(course_pattern), len(opening_tag)])

# pozycja w pliku, wskazująca na zamknięcie tagu. Zwróć uwagę na użycie 'course_title_pos'
closing_tag_pos = content.find(closing_tag, course_title_pos)

# wyciągamy zawartość
print(content[course_title_pos:closing_tag_pos])

# sięgamy po kolejne informacje
date_pattern = 'course-info__paragraph course-info__paragraph--date">'
closing_tag = '</p>'
date_pos = content.find(date_pattern, closing_tag_pos) + len(date_pattern)
closing_tag_pos = content.find(closing_tag, date_pos)

print(content[date_pos:closing_tag_pos])

