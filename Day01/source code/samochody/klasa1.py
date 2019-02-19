# importujemy klasę
from samochod import Samochod

# inicjalizujemy obiekt
# tworzymy instancje klasy Samochod

# tworze instancje klasy Samochod, inaczej -
# powołuję do życia obiekt typu Samochod
# nadaję mu konkretne cechy
auto1 = Samochod('Volvo', 'czarny')

# tworze kolejną instancję klasy Somochod
# ta instancja - obiekt ma inne dane niż auto1
# auto1 i auto2 są dwoma oddzielnymi obiektami stworzonymi
# na podstawie klasy Samochod
auto2 = Samochod('Tesla', 'niebieski')

# oba obiekty mają cechy/atrybuty/zmienne określone w klasie
print(auto1.producent, auto1.kolor)
print(auto2.producent, auto2.kolor)

# trąbimy Volvo
print("Teraz trąbi {}: {}".format(auto1.producent, auto1.zatrab(5)))

# a teraz tesla trąbi
print('Teraz trąbi {}: {}'.format(auto2.producent, auto2.zatrab(11)))

# Ruszamy Volvo do przodu
auto1.jedz()

# sprawdzamy stan - czy jedzie
print('Czy samochod {} jedzie? - {}'.format(auto1.producent, auto1.czy_jedzie))
