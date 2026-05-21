class JegyFoglalas:

    def __init__(self, utas_nev, jarat):
        self.__utas_nev = utas_nev
        self.__jarat = jarat

    def get_utas_nev(self):
        return self.__utas_nev

    def get_jarat(self):
        return self.__jarat

    def __str__(self):
        return f"{self.__utas_nev} - {self.__jarat}"