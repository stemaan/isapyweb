import csv
from helpers import get_person


# ściągamy dane Luke'a
def get_luke_skywalker():
    return get_person(1)

# ściągamy dane R2D2
def get_r2_d2():
    return get_person(3)


def save_to_csv(filename, headers, data):
    with open(filename, 'w', newline='') as data_file:
        # tworzymy obiekt odpowiadający za obsługę formatu csv
        writer = csv.writer(data_file)

        # zapis pojedynczego wiersza - nagłówek czyli definicja kolumn
        writer.writerow(headers)

        # zapis kolekcji
        writer.writerows(data)


luke = get_luke_skywalker()
r2d2 = get_r2_d2()
headers = luke.keys()
data = [luke.values(), r2d2.values()]
save_to_csv('luke_r2d2.csv', headers, data)

