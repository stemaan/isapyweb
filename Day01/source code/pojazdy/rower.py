from pojazd import Pojazd

class Rower(Pojazd):
    '''Rower jest Pojazdem
    Będzie dziedziczyć atrybuty z klasy Pojazd
    '''

    def __init__(self, nazwa):
        '''Własny konstruktor dla klasy Rower'''

        # inicjalizujemy informacje bazowe określone w klasie Pojazd
        Pojazd.__init__(self, nazwa)
        # możemy też zainicjalizować bezpośrednio
        # self.nazwa = nazwa
        self.kola = 2

    def zadzwon(self):
        '''Ta metoda jest specyficzna dla roweru.

        Klasa Pojazd jej nie ma i nie może używać
        '''
        return 'dryn dryn'

    # chociaż nie mamy definicji dla metod jedz() i stop()
    # to rower może z nich korzystać, bo dziedziczy je z klasy Pojazd

