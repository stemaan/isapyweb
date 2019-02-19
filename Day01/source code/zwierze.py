class Zwierze:
    '''Klasa podstawowa'''

    def __init__(self, imie, wiek):
        '''Konstruktor dla klasy Zwierze'''
        self.imie = imie
        self.wiek = wiek

    def powiedz(self):
        '''Zwierze wydaje odglos'''
        print('Zwierze wydaje glosy')

    def __str__(self):
        '''Własna reprezentacja obietu za pomocą funkcji print()'''
        return '{} ma {} lat'.format(self.imie, self.wiek)


class Kot(Zwierze):
    '''Kot jest podklasą Zwierze'''

    def powiedz(self):
        '''Własna implementacja mowy kota'''
        print('Mrrrrrrrr')


class Ryba(Zwierze):
    def __init__(self, imie, wiek, waga):
        super().__init__(imie, wiek)
        self.waga = waga


class Pies(Zwierze):
    '''Pies jest podklasa klasy Zwierze'''

    def powiedz(self):
        '''Własna implementacja mowy psa'''
        print('Hau hau')

    def merdaj(self):
        '''Pies merda ogonem
        Jest to metoda specyficzna dla psa, dlatego określiliśmy ją tutaj
        a nie w klasie Zwierze
        '''
        print('Ogon lata')


class Czlowiek(Zwierze):
    '''Człowiek jest podklasą klasy zwierze'''

    def __init__(self, imie, nazwisko, wiek):
        '''Tworzymy instancję Człowieka.'''
        # nazwisko jest unikalnym atrybutem dla człowieka
        self.nazwisko = nazwisko
        # korzystamy z konstruktora bazowego, aby zainicjalizować pozistałe
        # atrybuty
        # Zwierze.__init__(self, imie, wiek)
        super().__init__(imie, wiek)

    def powiedz(self):
        '''Własna implementacja moey człowieka'''
        print('Cześć!')

    def drukuj_nazwisko(self):
        '''A tu mamy metodę, która drukuje nazwisko'''
        print(self.nazwisko)


class Student(Czlowiek):
    '''Podobno Student też Człowiek ;)
    W naszym przypadku tak jest faktycznie.
    '''

    def powiedz(self):
        '''Własna implementacja dla mowy Studenta'''
        print('Poproszę tróje...')

    # pozostałe metody Student dziedziczy z klasy Człowiek a potem z Zwierze


def main():
    '''Ta metoda będzie wywołana przy uruchomieniu tego modułu (pliku)'''
    # zwierz1 = Zwierze('Mucha', 1)
    # print(zwierz1)
    # kot1 = Kot('Filemon', 2)
    # print(kot1)
    # kot1.powiedz()
    # pies1 = Pies('Szarik', 6)
    # print(pies1)
    # print(type(pies1))
    # print(issubclass(Pies, Kot))
    # pies1.powiedz()
    # pies1.merdaj()
    #
    # student1 = Student('Janek', 'kowalski', 19)
    # print(student1)
    # student1.powiedz()

    czlowiek1 = Czlowiek('Jan', 'Kowalski', 34)
    czlowiek1.drukuj_nazwisko()
    print(czlowiek1.imie)
    print(czlowiek1.wiek)
    print(czlowiek1)
    #
    # student2 = Student('Jan', 'Iksinski', 21)
    # print(student2)


# jeśli moduł będzie uruchomiony bezpośrednio to kod wew. funkcji
# main() zostanie uruchomiony
# jeśli moduł będzie importowany do innego miejsca, to kod wew. main()
# nie zostanie wywołany
if __name__ == '__main__':
    main()
