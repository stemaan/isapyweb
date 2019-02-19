# metoda klasy jako alternatywny konstruktor
class Pracownik(object):
    '''Klasa Pracownik'''

    # pola klasy
    liczba_pracownikow = 0
    roczna_podwyzka = 5

    def __init__(self, imie, stanowisko):
        '''Podstawowy konstruktor'''
        self.imie = imie
        self.stanowisko = stanowisko
        Pracownik.liczba_pracownikow += 1

    def ustaw_wynagrodzenie(self, amount):
        self.wynagrodzenie = amount

    def daj_roczna_podwyzke(self):
        self.wynagrodzenie += self.wynagrodzenie * (1 / self.roczna_podwyzka)

    # metoda klasy ma taki dekorator
    @classmethod
    def okresl_rocz_podw(cls, wartosc):
        '''Zmienia wartość domyślnej podwyżki.
        Metoda klasy - zmienia pole klasy
        '''
        if wartosc > 8:
            cls.roczna_podwyzka = 8
        else:
            cls.roczna_podwyzka = wartosc

    @classmethod
    def z_pensja(cls, imie, stan, pensja):
        '''Alternatywny konstruktor, określiliśmy inne argumenty'''

        # musimy pamiętać o tym w jaki sposób tworzymy obiekt i jak zmieniamy jego dane
        prac = cls(imie, stan)
        # przed zwróceniem instancji, musimy zaktualizować jej pola
        prac.wynagrodzenie = pensja
        # zwracamy gotową instancję
        return prac


# tworzymy obiekt używając alternatywnego konstruktora
os1 = Pracownik.z_pensja('Jan Kowalski', 'aktor', 5000)

print(os1.wynagrodzenie)
print(os1.imie)

os2 = Pracownik.z_pensja('Janina', 'aktorka', 3000)
print(os2.wynagrodzenie)
print(os2.imie)

print(os1.wynagrodzenie)
