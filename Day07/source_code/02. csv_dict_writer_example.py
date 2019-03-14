import csv
from helpers import get_person

# ściąganie rekordów o id od 1 do 10
def get_people_from_range(a=1, b=10):
    # list comprehension 
    return [get_person(id) for id in range(a, b)]

# utworzenie i wypełnienie pliku csv
def save_to_csv(filename, headers, data, **kwargs):
    with open(filename, 'w', newline='') as data_file:
    # dzięki DictWriter możemy przekazać listę rekordów - słowników
        writer = csv.DictWriter(data_file, headers, **kwargs)
        writer.writeheader()
        writer.writerows(data)


people = get_people_from_range()
headers = people[0].keys()
save_to_csv('people_1-10.csv', headers, people, delimiter=';')
