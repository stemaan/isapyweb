from rower import Rower


class Dzieciecy(Rower):
    '''Podklasa klasy Rower'''
    def __init__(self):
        '''Konstruktor nie przyjmuje argumentu'''
        Rower.__init__(self, 'dzieciecy')
        self.kola = 4

    def jedz(self):
        return 'Jedzie wolno'

