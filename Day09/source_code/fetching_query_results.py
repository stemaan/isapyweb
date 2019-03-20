if __name__ == '__main__':
    from client_models import Client
    from sqlalchemy_create_engine import Session

    # utworzenie sesji
    session = Session()

    # pierwszym sposobem na otrzymanie rezultatu jest iteracja
    # w momencie iteracji obiekt Query jest ewaluowany
    collection = session.query(Client).filter(Client.first_name == 'Jan')
    for result in collection:
        print(result)

    # ten sam efekt co wyżej
    results = session.query(Client).filter(Client.first_name == 'Jan').all()
    print(results)

    # tylko pierwszy rezultat zapytania
    only_first = session.query(Client).filter(Client.first_name == 'Jan').first()
    print(only_first)

    # gdy oczekiwany jest tylko jeden obiekt
    one = session.query(Client).filter(Client.first_name == 'Jan').one()
    print(one)

    # jeżeli zapytanie zwraca więcej niż jedne obiekt wtedy metoda one zwróci wyjątek
    # MultipleResultsFound: Multiple rows were found for one()
    # lub jeżeli zbiór będzie pusty
    # NoResultFound: No row was found for one()

    # podobnie jak metoda one, lecz gdy zbiór jest pusty nie zwracany jest wyjątek lecz None
    one_or_none = session.query(Client).filter(Client.first_name == 'Jan').one_or_none()
