# importujemy nasze moduły i klasy
import silnik
import samochod

# tworzymy kilka instancji obiektów typu Silnik
maly_silnik = silnik.Silnik(75, 1000)
sredni_silnik = silnik.Silnik(160, 1600)
v8 = silnik.Silnik(450, 6000)

# drukujemy kilka cech naszych silników
print(v8.horse_power)
print(maly_silnik.horse_power)

# tworzymy instancje klasy Samochod
volvo = samochod.Samochod('volvo', 'balck')

# przypisujemy obiekt typu Silnik do atrybutu silnik w obiekcie
# typu Samochod
volvo.silnik = sredni_silnik

# drukujemy moc silnika w naszym samochodzie
# wgłąb obiektu, do poszczególnych atrybutów,
# dostajemy się używając kropek
print('Moc silnika w volvo:', volvo.silnik.horse_power)

# tworzymy nowy obiekt typu Samochod,
# trzymamy do w zmiennej audi
audi = samochod.Samochod('audi', 'srebrny')

# przypisujemy obiekt typu Silnik do obiektu Samochod
# wstawiamy silnik do samochodu
audi.silnik = maly_silnik

# dostajemy się do atrybutów obiektu Silnik wewnatrz naszego
# obiektu Samochod
print('audi ma silnik o mocy {}'.format(audi.silnik.horse_power))

print('Czy silnik w audi pracuje? - ', audi.silnik.pracuje)

# korzystamy z metody dostarczanej przez obiekt Silnik
# i wykorzystujemy ją do uruchomienia silnika w audi
print('Uruchamiamy silnik w audi')
audi.silnik.uruchom()

# sprawdzamy czy silnik w audi pracuje
print('Czy silnik w audi pracuje? - ', audi.silnik.pracuje)

# w Volvo silnik nie pracuje, bo silnik w volvo jest
# inną instancją klasy Silnik niż instancja w audi
print('Czy silnik w volvo pracuje? -', volvo.silnik.pracuje)

# a teraz włączamy i wyłączamy silnik w volvo
print('Uruchamiamy silnik w volvo')
volvo.silnik.praca_silnika(True)

print('Czy silnik w volvo pracuje? -', volvo.silnik.pracuje)

print('Wyłączamy silnik w volvo')
volvo.silnik.praca_silnika(False)

print('Czy silnik w volvo pracuje? -', volvo.silnik.pracuje)
