class Pracownik(object):
    '''Klasa Pracownik'''
    def __init__(self, imie, nazwisko, stanowisko):
        '''Konstruktor'''

        # dane trzymamy w pseudo-prywatnych zmiennych instancji
        # używamy 2 podkreślniki z przodu nazwy
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__stanowisko = stanowisko

    def wypisz_imie(self):
        # wewnątrz naszej klasy mamy swobodny dostęp do naszych
        # pseudoprywatnych zmiennych
        print(self.__imie)

    # to jest getter - property
    # getter ma taki dekorator
    @property
    def stanowisko(self):
        '''Property definiujemy jak metodę.
        W getterze mamy kontrolą nad tym w jaki sposób oddajemy informacje
        '''
        if self.__stanowisko != None:
            return str(self.__stanowisko).capitalize()

    # to jest property - setter
    # ma taki dekorator - musimy podać nazwę gettera, kropka setter
    @stanowisko.setter
    def stanowisko(self, nazwa):
        '''Setter służy do kontrolowania informacji, ktore
        beda zapisywane do zmiennych
        '''
        if str(nazwa).isalpha():
            self.__stanowisko = nazwa

    # to jest property - deleter
    # określa zachowanie przy usuwaniu property
    @stanowisko.deleter
    def stanowisko(self):
        print('Usuwam stanowisko')
        self.__stanowisko = None


pr1 = Pracownik('jan', 'kowalski', 'aktor')
pr1.wypisz_imie()

print('\nUzywając pr1.__dict__ możemy podejrzeć wszyskie atrybuty. Zobaczymy też nasze pseudoprywatne')
print('pole, ktore jest ukryte pod zmienioną nazwą')
print(pr1.__dict__)

# nic nie stoi na przeszkodzie abym użył bezpośrednio pseudoprywatne pole')
pr1._Pracownik__imie = 'Ola'
pr1.wypisz_imie()

# używam propertisa - chociaz definiowalem go jak metode, to uzywam jak zmienną - bez nawiasów
print(pr1.stanowisko)
pr1.stanowisko = 'gwiazda 100'
print(pr1.stanowisko)
del pr1.stanowisko

print(pr1.__dict__)


