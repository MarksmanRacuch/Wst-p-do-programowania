import random
def prostokat():
    a = float(input("Podaj szerokosc prostokata: "))
    b = float(input("Podaj dlugosc prostokata: "))
    pole = a * b
    obwod = a + a + b + b
    print(f"Obwod prostokata wynosi: {obwod}")
    print(f"Pole prostokata wynosi: {pole}")

prostokat()
print()

def jazda():
    droga = float(input("Podaj pokonaną droge w kilometrach: "))
    spalanie = float(input("Podaj spalanie (w litrach na 100km): "))
    zuzycie = droga / 100 * spalanie
    koszt = zuzycie * 6.5
    print("Przewidywalne zuzycie paliwa wyniesie: ", zuzycie)
    print("Przewidywalne koszt wyniesie: ", koszt, "zł")

jazda()
print()

def jazda1():
    droga = random.randint(1,1000)
    print("Droga wynosi: ", droga, "km")
    spalanie = float(input("Podaj spalanie (w litrach na 100km): "))
    zuzycie = droga / 100 * spalanie
    koszt = zuzycie * 6.5
    print("Przewidywalne zuzycie paliwa wyniesie: ", zuzycie)
    print("Przewidywalne koszt wyniesie: ", koszt, "zł")

jazda1()
print()

def bilety():
    print("Dla osob ponizej 4 roku zycia wstep jest bezplatny")
    print("Dla osob w wieku od 4 do 18 lat bilet kosztuje: 10zł")
    print("Dla osob powyzej 18 roku zycia bilet kosztuje: 20zł")
    print()
    wiek = int(input("Wprowadz wiek klienta: "))
    if wiek < 4:
        print("Cena biletu: 0zł")
    elif wiek > 17:
        print("Cena biletu: 20zł")
    else:
        print("Cena biletu: 10zł")
    
bilety()
print()

def sprawdzanie():
    litera = str(input("Wprowadź jedną literę: "))
    if (litera.isupper()):
        print("Wprowadzona litera jest: DUZA")
    elif (litera.islower()):
        print("Wprowadzona litera jest: mala")
    else:
        print("Nie wprowadzono litery")

sprawdzanie()
print()

def menu():
    print("Jaka operacje chcesz wykonać?")
    print()
    print("1) dodawanie")
    print("2) odejmowanie")
    print("3) mnożenie")
    print("4) dzielenie")
    print("5) potęgowanie")
    print()
    operacja = int(input("Wpisz numer operacji: "))
    if operacja == 1:
        dodawanie()
        menu()
    elif operacja == 2:
        odejmowanie()
        menu()
    elif operacja == 3:
        mnożenie()
        menu()
    elif operacja == 4:
        dzielenie()
        menu()
    elif operacja == 5:
        potegowanie()
        menu()
    else:
        print("Wprowadzono zły numer")
        menu()
    


def dodawanie():
    arg1 = float(input("Podaj argument 1: "))
    arg2 = float(input("Podaj argument 2: "))
    wynik = arg1 + arg2
    print("Wynik: ", wynik)
    print()

def odejmowanie():
    arg1 = int(input("Podaj argument 1: "))
    arg2 = int(input("Podaj argument 2: "))
    wynik = arg1 - arg2
    print("Wynik: ", wynik)
    print()

def mnożenie():
    arg1 = int(input("Podaj argument 1: "))
    arg2 = int(input("Podaj argument 2: "))
    wynik = arg1 * arg2
    print("Wynik: ", wynik)
    print()


def dzielenie():
    arg1 = int(input("Podaj argument 1: "))
    arg2 = int(input("Podaj argument 2: "))
    wynik = arg1 / arg2
    print("Wynik: ", wynik)
    print()


def potegowanie():
    arg1 = float(input("Podaj argument 1: "))
    arg2 = float(input("Podaj argument 2: "))
    wynik = arg1 ** arg2
    print("Wynik: ", wynik)
    print()

menu()





