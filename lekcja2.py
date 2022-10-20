def menu():
    print("Jaka operacje chcesz wykonać?")
    print()
    print("1) dodawanie")
    print("2) odejmowanie")
    print("3) mnożenie")
    print("4) dzielenie")
    print("5) potęgowanie")
    print("6) zamknij program")
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
    elif operacja == 6:
        pass
    else:
        print("Wprowadzono zły numer")
        print()
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
    if arg2 != 0:
        wynik = arg1 / arg2
    else:
        print("Dzielenie przez 0!")
        return
    print()
    print("Wynik: ", wynik)
    
def potegowanie():
    arg1 = float(input("Podaj argument 1: "))
    arg2 = float(input("Podaj argument 2: "))
    wynik = arg1 ** arg2
    print("Wynik: ", wynik)
    print()

menu()