class Samochod(object):
    '''Definiuje atrybuty i metody samochodu'''

    def __init__(self, marka, kolor):
        '''Konstruktor, tworzy nowe instancje'''
        self.producent = marka
        self.kolor = kolor
        self.czy_jedzie = None
        self.silnik = None

    def zatrab(self, intensywnosc):
        '''
        Trąbi w zależności od intensywności
        :param intensywnosc: int, długość trąbienia w sekundach
        :return: str, reprezentacja dźwięku klaksonu
        '''
        if intensywnosc > 10:
            return 'PIIIIIIIIIIIIII'
        else:
            return ('p' + 'i' * intensywnosc)

    def jedz(self):
        '''Rzozpedza samochod'''
        self.czy_jedzie = True

    def zatrzymaj(self):
        '''Zatrzymuje samochod'''
        self.czy_jedzie = False
