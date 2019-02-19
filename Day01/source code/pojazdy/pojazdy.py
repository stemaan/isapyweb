from pojazd import Pojazd
from rower import Rower
from rower_dziec import Dzieciecy
from samochod import Samochod

poj1 = Pojazd('ogolny')
print(poj1)

# rower1 = Rower('Romet')
# print(rower1)
# print(rower1.zadzwon())
# print(rower1.kola)
# print(rower1.jedz())
# print('--------------')
# dzieciecy1 = Dzieciecy()
# print(dzieciecy1.nazwa)
# print(dzieciecy1.kola)
# dzieciecy2 = Dzieciecy()
# print(dzieciecy2.nazwa)
# print(dzieciecy2.kola)
#
# print(rower1.jedz())
# print(dzieciecy2.jedz())

auto1 = Samochod('Volvo')
print(auto1)
auto1.moc = 163
auto1.tuning()
print(auto1.moc)

auto2 = Samochod('BMW')
auto2.moc = 180
print(auto1 > auto2)
rower1 = Rower("Romet")
print(rower1)
print('-----------')
kids1 = Dzieciecy()
print(kids1.kola)
kids1.dodaj_kolo()
print(kids1.kola)



