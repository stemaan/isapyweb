from sqlalchemy_create_engine import Session

if __name__ == '__main__':
    from client_models import Client, Address

    session = Session()

    # utworzenie pierwszego obiektu
    jan = Client(first_name='Jan', last_name='Kowalski')
    session.add(jan)

    # bardzo ważny fragment kodu
    session.commit()

    # utworzenie obiektu; zwróć uwagę na to, że wcześniej musiał istnieć jan.id
    address1 = Address(name='Dom', address='ul. Pythona 15 12-345 Pythonowo', client_id=jan.id)
    session.add(address1)
    session.commit()

    # sprawdzenie stanu bazy danych
    print(session.query(Client).all())
    print(session.query(Address).all())


    adam = Client(first_name='Adam', last_name='Nowak')
    session.add(adam)

    # bardzo ważny fragment kodu
    # session.commit()

    # utworzenie obiektu
    address2 = Address(name='Dom', address='ul. Pythona 23 12-345 Pythonowo', client_id=adam.id)
    session.add(address2)
    session.commit()

    # jaka jest wartosc jan.id ?
    print(session.query(Client).all())
    print(session.query(Address).all())


