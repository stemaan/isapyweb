from sqlalchemy import Column, Integer, String, Float, Text, Date, DateTime, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Oferty(Base):
    __tablename__ = 'oferty'
    id_oferty = Column(Integer, primary_key=True)
    id_sprzedajacego = Column(Integer)
    lokalizacja = Column(String(300))
    tytul = Column(String(300))
    cena = Column(Integer)
    marka = Column(String(300))
    model = Column(String(300))
