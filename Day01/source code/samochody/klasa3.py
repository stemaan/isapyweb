# importujemy bezpośrednio klasę
from samochod import Samochod

# tworzymy instancję klasy Samochod
# w konstruktorze podajemy argumenty

# argument self - podany w definicji metody __init__
# będzie automatycznie uzupełniony przez Python'a
volvo = Samochod('volvo', 'black')

# drukujemy jeden z atrybutów = pole = zmienna instancji
print(volvo.czy_jedzie)
