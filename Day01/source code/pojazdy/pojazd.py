class Pojazd(object):
    '''Klasa bazowa dla pojazdu'''
    def __init__(self, model):
        '''Tworzy nową instancję klasy.

            (model) - str, nazwa pojazdu
        '''
        # zmienne instancji - używamy z self
        self.nazwa = model
        # ta zmienna jest None, bo wiemy, że pojazdy mają koła, ale
        # mogą mieć różną ilość
        self.kola = None

    def jedz(self):
        '''Rusza pojazd'''
        return 'Jedzie'

    def stop(self):
        '''Zatrzymuje pojazd'''
        return 'Zatrzymany'

    def dodaj_kolo(self):
        self.kola += 1

    def __str__(self):
        '''Przeciążamy metodę specjalną Pythona,
            tym sposobem określamy własne zachowanie dla
            polecenia print()
        '''
        return 'Pojazd {}'.format(self.nazwa)





