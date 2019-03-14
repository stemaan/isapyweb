import csv

with open('people_1-10.csv', 'r', newline='') as csv_data:
    # zwróć uwagę na ustawienie delimitera
    reader = csv.DictReader(csv_data, delimiter=';')

    # atrybut przechowujący nazwy kolumn
    headers = reader.fieldnames
    print(headers)

    for row in reader:
        print(row['name'], row['birth_year'])
