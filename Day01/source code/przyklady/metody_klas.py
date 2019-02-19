# metody klasy
class Pracownik(object):

    # pola naszej klasy
    liczba_pracownikow = 0
    roczna_podwyzka = 5

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        Pracownik.liczba_pracownikow += 1

    def ustaw_wynagrodzenie(self, amount):
        self.pay = amount

    def daj_roczna_podwyzke(self):
        self.pay += self.pay * (1/self.roczna_podwyzka)

    # metoda klasy oznaczana jest takim dekoratorem
    @classmethod
    def okresl_rocz_podw(cls, wartosc):
        '''Metoda klasy jako pierwszy argument zawsze przyjmuje klasę jako słowo
        kluczowe cls
        '''
        if wartosc > 8:
            cls.roczna_podwyzka = 8
        else:
            cls.roczna_podwyzka = wartosc

    def __str__(self):
        return ('{} stanowisko: {}'.format(self.imie, self.stanowisko))

# używamy metody klasy do zmiany wartości pola klasy
print('Pracownik.roczna_podwyzka =',Pracownik.roczna_podwyzka)
Pracownik.okresl_rocz_podw(12)
print('Po zmianie pole Pracownik.roczna_podwyzka =',Pracownik.roczna_podwyzka)

pr1 = Pracownik('jan kowalski', 'kowal')
pr2 = Pracownik('janina kowalska', 'dyrektor')

print('\nWywolujemy metodę klasy poprzez instancję.')
pr1.okresl_rocz_podw(16)

print('\nPomimo tego, pole roczna_podwyżka jest takie same dla wszystkich')
print(Pracownik.roczna_podwyzka)
print(pr1.roczna_podwyzka)
print(pr2.roczna_podwyzka)
print('\nDobra praktyka - pola i metody klasy używać odwołując się do klasy a nie instancji')
