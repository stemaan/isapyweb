from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# bardzo istotny obiekt
Base = declarative_base()


# klasa reprezentująca tabelę z informacją o klientach
# zwróć uwagę, kto jest rodzicem
class Client(Base):
    # nazwa tabeli w bazie
    __tablename__ = 'clients'  # <------- atrybut wymagany

    # klucz główny
    id = Column(Integer, primary_key=True)  # <----- tabela musi mieć klucz główny

    # pozostałe kolumny
    first_name = Column(String)
    last_name = Column(String)

    # tworzymy relację - obie klasy odpowiadające tabelom muszą wiedzieć o tej relacji
    addresses = relationship('Address', back_populates='client')

    def __repr__(self):  # nieobowiązkowa implementacja metody; tworzymy ją na potrzeby deweloperskie
        return f'<Client(first_name={self.first_name}, last_name={self.last_name})>'


# klasa reprezentująca tabelę z informacją o adresach
class Address(Base):
    # nazwa tabeli w bazie
    __tablename__ = 'adresses'

    # klucz główny
    id = Column(Integer, primary_key=True)

    # pozostałe kolumny
    name = Column(String)
    address = Column(String)

    # klucz obcy, wskazuje na pole clients.id
    client_id = Column(Integer, ForeignKey('clients.id'))

    # tworzymy relację;  - obie klasy odpowiadające tabelom muszą wiedzieć o tej relacji
    client = relationship('Client', back_populates='addresses')

    def __repr__(self):  # nieobowiązkowa implementacja metody; tworzymy ją na potrzeby deweloperskie
        return f'<Address(name={self.name}, address={self.address}, client_id={self.client_id})>'
