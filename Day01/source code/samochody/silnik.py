class Silnik(object):
    '''Ta klasa opisuje cechy i zachowanie silnika'''

    def __init__(self, moc, pojemnosc):
        '''
        Konstruktor, tworzy instancję silnika
        :param moc: int, określa moc w koniach mechanicznych
        :param pojemnosc: int, określa pojemność silnika w cm3
        '''
        self.horse_power = moc
        self.volume = pojemnosc
        self.pracuje = False

    def uruchom(self):
        '''Uruchamia silnik'''
        self.pracuje = True

    def zatrzymaj(self):
        '''Zatrzymuje silnik'''
        self.pracuje = False

    def praca_silnika(self, stan):
        '''Steruje pracą silnika

        :param stan: bool, True jeśli mamy włączyć, False jeśli chcemy zatrzymać
        '''
        self.pracuje = stan
