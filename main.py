from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from legitarsasag import LegiTarsasag
from jegy_foglalas import JegyFoglalas


def menu():
    print("\n--- REPÜLŐJEGY FOGLALÁSI RENDSZER ---")
    print("1 - Jegy foglalása")
    print("2 - Foglalás lemondása")
    print("3 - Foglalások listázása")
    print("4 - Kilépés")


# légitársaság létrehozása
legi = LegiTarsasag("Air Hungary")

# járatok
j1 = BelfoldiJarat("B101", "Debrecen", 15000)
j2 = BelfoldiJarat("B102", "Szeged", 12000)
j3 = NemzetkoziJarat("N201", "London", 85000)

legi.jarat_hozzaadas(j1)
legi.jarat_hozzaadas(j2)
legi.jarat_hozzaadas(j3)

# 6 előre feltöltött foglalás
legi.foglalas_hozzaadas(JegyFoglalas("Anna", j1))
legi.foglalas_hozzaadas(JegyFoglalas("Béla", j2))
legi.foglalas_hozzaadas(JegyFoglalas("Csilla", j3))
legi.foglalas_hozzaadas(JegyFoglalas("Dani", j1))
legi.foglalas_hozzaadas(JegyFoglalas("Eszter", j2))
legi.foglalas_hozzaadas(JegyFoglalas("Ferenc", j3))


while True:

    menu()
    valasztas = input("Válassz: ")

    # foglalás
    if valasztas == "1":

        print("\nElérhető járatok:")

        for i, jarat in enumerate(legi.get_jaratok()):
            print(f"{i + 1}. {jarat}")

        try:
            jarat_index = int(input("Járat száma: ")) - 1

            if jarat_index < 0 or jarat_index >= len(legi.get_jaratok()):
                print("Hibás járat!")
                continue

            nev = input("Utas neve: ")

            foglalas = JegyFoglalas(
                nev,
                legi.get_jaratok()[jarat_index]
            )

            legi.foglalas_hozzaadas(foglalas)

            print("Sikeres foglalás!")
            print(
                f"Ár: {legi.get_jaratok()[jarat_index].get_jegyar()} Ft"
            )

        except ValueError:
            print("Hibás adat!")

    # lemondás
    elif valasztas == "2":

        foglalasok = legi.get_foglalasok()

        if not foglalasok:
            print("Nincs foglalás!")
            continue

        for i, foglalas in enumerate(foglalasok):
            print(f"{i + 1}. {foglalas}")

        try:
            index = int(input("Melyiket törlöd? ")) - 1

            if legi.foglalas_torles(index):
                print("Foglalás törölve!")
            else:
                print("Hibás sorszám!")

        except ValueError:
            print("Számot adj meg!")

    # listázás
    elif valasztas == "3":

        foglalasok = legi.get_foglalasok()

        if not foglalasok:
            print("Nincs foglalás!")
        else:
            for foglalas in foglalasok:
                print(foglalas)

    # kilépés
    elif valasztas == "4":
        print("Kilépés...")
        break

    else:
        print("Hibás menüpont!")