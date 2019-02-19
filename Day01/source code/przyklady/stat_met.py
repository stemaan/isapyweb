# metody statyczne

class Matematyka(object):

    # metoda statyczna ma taki dekorator
    @staticmethod
    def pole_prostokata(bok_a, bok_b):
        return bok_a * bok_b

# metodę statyczną używamy bez tworzenia instancji klasy.
# ta metoda nie korzysta z żadnych informacji z klasy
pole = Matematyka.pole_prostokata(30, 40)

print('Pole wynosi:', pole)