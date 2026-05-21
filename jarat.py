from abc import ABC

class Jarat(ABC):

    def __init__(self, jaratszam, celallomas, jegyar):
        self.__jaratszam = jaratszam
        self.__celallomas = celallomas
        self.__jegyar = jegyar

    def get_jaratszam(self):
        return self.__jaratszam

    def get_celallomas(self):
        return self.__celallomas

    def get_jegyar(self):
        return self.__jegyar

    def __str__(self):
        return f"{self.__jaratszam} - {self.__celallomas} - {self.__jegyar} Ft"