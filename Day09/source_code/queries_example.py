from sqlalchemy import and_, or_
from client_models import Client, Address
from sqlalchemy_create_engine import Session

if __name__ == '__main__':
    session = Session()
    # Query object jest leniwy i wynik zwraca w momencie ewaluacji!

    # filtrowanie wg wartości
    session.query(Client).filter(Client.first_name == 'Jan')

    # filtrowanie wg dopasowania
    session.query(Address).filter(Address.address.ilike('%Python%'))

    # czy wartość zawiera się z zbiorze
    session.query(Client).filter(Client.first_name.in_(['Adam', 'Pawel', 'Jan']))

    # czy wartość NIE zawiera się z zbiorze
    session.query(Client).filter(~Client.first_name.in_(['Anna', 'Malgorzata']))

    # czy kolumna jest pusta
    session.query(Address).filter(Address.client_id == None)

    # iloczyn logiczny
    session.query(Address).filter(and_(Address.client_id == None, Address.name == 'Dom'))

    # suma logiczna
    session.query(Address).filter(or_(Address.client_id == None, Address.name == 'Praca'))
