from pojazd import Pojazd


class Samochod(Pojazd):
    '''Samochod jest podklasa pojazdu'''
    def __init__(self, marka):
        '''Tworzy instancę Samochodu'''
        Pojazd.__init__(self, marka)
        self.kola = 4
        self.moc = None

    def tuning(self):
        '''Tuning silnika'''
        self.moc += 30

    def __gt__(self, other):
        '''Przeciążony operator ">"
        dzięki temu możemy porównać dwa Samochody
        '''
        return self.moc > other.moc

    def __str__(self):
        '''Własna implementacja specjalnej metody
        Samochod bedzie inaczej wypisany print() niz pojazd
        '''
        return 'Samochod marki {}'.format(self.nazwa)

