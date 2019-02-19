class Osoba(object):
    '''Osoba'''

    def __init__(self, imie, nazwisko, pesel):
        '''Tworzy instancję klasy Osoba'''
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.wiek = None

    def __str__(self):
        '''Wlasna reprezentacja obiektu przy print() '''
        return "{} {} ma pesel: {}".format(self.imie, self.nazwisko, self.pesel)

    def __add__(self, other):
        '''Własna implementacja zachowania dla operatora "+"
        Dzięki temu możemy "dodawać" osoby
        '''
        return self.wiek + other.wiek


czlowiek1 = Osoba('jan', 'kowalski', 9898978778)
czlowiek1.wiek = 30

czlowiek2 = Osoba('Mateusz', 'Nowak', 98987878778)
czlowiek2.wiek = 34
# print(czlowiek1.imie)
# print(czlowiek1.nazwisko)
# print(czlowiek1.pesel)

print(czlowiek1)

# dodajemy osoby
print(czlowiek1 + czlowiek2)
