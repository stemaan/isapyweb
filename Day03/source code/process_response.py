import logging

import requests
from helpers import get_people_list, get_person, get_root, handle_response


# wyświetlenie dostępnych zasobów
def display_api_info():
    endpoints = get_root()
    print('Dostepne zasoby API')
    for resource_name, url in endpoints.items():
        print(resource_name, url)

# wyświetlenie liczności zasobu
def display_resource_count(resource_name):
# pobieramy listę zasobów
    endpoints = get_root()

    try:
        url = endpoints[resource_name]
    except KeyError as keyerr:
        logging.error(
            f'Wyjatek podczas proby uzyskania zasobu {keyerr}: {endpoints}'
        )
        return

# pobieramy konkretny zasób
    response = requests.get(url)
    response_data = handle_response(response)

# zwróc uwagę na konstrukcję get z domyślną wartością
    count = response_data.get('count', None)

    print(f'Ilość zasobów o nazwie "{resource_name}" wynosi: {count}')


if __name__ == '__main__':
    display_api_info()
    print('-'*40)

    # literówka jest zamierzona
    display_resource_count(resource_name='peopxle')
    print('-'*40)

    # bez literówki w nazwie zasobu
    display_resource_count(resource_name='people')
    print('-'*40)

    # pobieramy listę bohaterów
    print(get_people_list())
    print('-'*40)

    # pobieramy pełen zasób (szczegóły dotyczące bohatera #1)
    person = get_person(1)
    print(person['name'])
    print('-'*40)


