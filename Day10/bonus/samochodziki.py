from model import Oferty, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///samochodziki.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# oferta #1
oferta1 = Oferty(id_sprzedajacego=20, lokalizacja='Szczecin', tytul='Nowy Ford Escort', cena=10000, marka='Ford', model='Escort')
session.add(oferta1)

# oferta #2
oferta2 = Oferty()
oferta2.id_sprzedajacego = 30
oferta2.lokalizacja = 'Świnoujście'
oferta2.tytul = 'Nowy Mercedes jak Igła'
oferta2.cena = 20000
oferta2.marka = 'Mercedes'
oferta2.model = 'W124'
session.add(oferta2)

# oferta #3
oferta3 = Oferty()
oferta_tmp = {'id_sprzedajacego': 30, 'lokalizacja': 'Warszawa', 'tytul': 'Stary Golf', 'cena': 1000}
oferta_tmp['marka'] = 'VW'
oferta_tmp['model'] = 'Golf'
for element in oferta_tmp.keys():
    setattr(oferta3, element, oferta_tmp[element])
session.add(oferta3)

session.commit()
