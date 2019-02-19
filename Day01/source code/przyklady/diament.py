# Dziedziczenie Diamentowe

# nasza glowna klasa
class Zwierze:
    '''Glowna klasa'''

    def __init__(self, imie):
        '''Inicjalizuje nowa instancje
        imie - str
        '''
        self.imie = imie

    def mowi(self):
        '''Wspolna metoda dla wszystkich zwierzat'''
        print('Zwierze nie mowi')

    def __str__(self):
        '''Definiujemy metode specjalna, ktora bedzie nam prezentowac obiekt
        przy uzyciu print()
        '''
        return str(self.imie).capitalize()


class Kon(Zwierze):
    '''Klasa pochodna od Zwierze'''

    def __init__(self, imie):
        '''Inicjalizuje nowa instancje Kon'''

        # korzystamy z konstruktora klasy nadrzednej aby zainicjalizowac
        # pola okreslone w rodzicu
        Zwierze.__init__(self, imie)

    def mowi(self):
        '''Kon mowi. Implementujemy zachowanie odpowiednie dla konia.
        Obiekty typu Kon, beda korzystac z tej metody say()
        '''
        print('Hej, jestem koń')

    def skacz(self):
        '''Kon skacze.
        Ta metoda jest specyficzna dla konia, tylko obiekty typu Kon,
         oraz dzieci klasy Kon moga z niej korzystac.
        '''
        print('Koń skacze')


class Osiol(Zwierze):
    '''Klasa potomna Zwierze'''

    def __init__(self, imie):
        '''Inicjalizuje nowy obiekt Osiol.
        PyCharm podkresla nazwe, poniewaz sugeruje abysmy uzyli konstruktor z klasy bazowej'''
        Zwierze.imie = imie

    def mowi(self):
        '''Wlasna implementacja dla Osiol'''
        print('iiiiiihhaaaa jestem osiol')

    def biegnij(self):
        '''Metoda specyficzna dla klasy Osiol'''
        print('Ja nie biegam, jestem oslem')


class Mul(Kon, Osiol):
    '''Mul dziedziczy od Osiol i Kon

    Wazna jest kolejnosc z jaka okreslimy dziedziczenie. Atrybuty beda szukane od pierwszej pozycji
    '''

    def mowi(self):
        '''Wlasna implementacja mowienia dla Mul'''
        print('Jestem mułem, ale też mówię jak moj rodzic super(): ', end='*')
        # Mul skorzysta z metody mowi() rodzica, pierwszego w ktorym bedzie ta metoda
        super().mowi()


print('\nZwierzak: ------------------')
# tworzymy instancje Zwierze
animal1 = Zwierze('zwierzak')
print(animal1)
animal1.mowi()
#
print('\nKoń: ------------------')
# tworzymy instancje Kon
kon1 = Kon('Kary')
print(kon1)
# jak widzimy kon korzysta z wlasnej implementacji
kon1.mowi()
kon1.skacz()

print('\nOsioł: ------------------')
osiol1 = Osiol('donkey kong')
osiol1.mowi()
osiol1.biegnij()

print('\nMuł: ------------------')
mul1 = Mul('Mułek')
# korzystamy z wlasnej implementacji mowi()
mul1.mowi()
#
# a tu korzystamy z metod obu rodzicow
mul1.skacz()
mul1.biegnij()
