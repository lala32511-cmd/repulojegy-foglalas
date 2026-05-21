class LegiTarsasag:

    def __init__(self, nev):
        self.__nev = nev
        self.__jaratok = []
        self.__foglalasok = []

    def jarat_hozzaadas(self, jarat):
        self.__jaratok.append(jarat)

    def foglalas_hozzaadas(self, foglalas):
        self.__foglalasok.append(foglalas)

    def foglalas_torles(self, index):
        if 0 <= index < len(self.__foglalasok):
            del self.__foglalasok[index]
            return True
        return False

    def get_jaratok(self):
        return self.__jaratok

    def get_foglalasok(self):
        return self.__foglalasok