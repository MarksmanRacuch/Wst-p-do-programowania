import math

# Zadanie 1:

x = float(input("Podaj wartosc x: "))   
if x < 0:
    print(-3*x)
elif x == 0:
    print(0)
else:
    print(2*x)

print()

y = float(input("Podaj wartosc x: "))
if y >= 1:
    print(y**2)
else:
    print(y)

print()

z = float(input("Podaj wartosc x: "))
if z > 2:
    print(2+x)
elif z == 2:
    print(8)
else:
    print(z-4)

print()

# Zadanie 2

def rownanieliniowe():
    a = int(input("Podaj wartosc a rownania liniowego: "))
    b = int(input("Podaj wartosc b rownania liniowego: "))
    print(a,"x", "+", b, "= 0")
    if a == 0:
        if b == 0:
            print("test")
        else:
            print("Równanie jest sprzeczne")
    else:
        x = -b/a
        print("x =", x)

rownanieliniowe()
print()

# Zadanie 3

def rownaniekwadratowe():
    a = int(input("Podaj wartosc a rownania kwadratowego: "))
    b = int(input("Podaj wartosc b rownania kwadratowego: "))
    c = int(input("Podaj wartosc c rownania kwadratowego: "))
    print()
    print(a,"x^2", "+", b,"x", "+", c, "= 0")
    print()
    delta = (b*b) - (4*a*c)
    print(delta)
    print()
    if delta > 0:
        x1 = -b - math.sqrt(delta)/(2*a)
        x2 = -b + math.sqrt(delta)/(2*a)
        print("x1 = ", x1)
        print("x2 = ", x2)
    elif delta == 0:
        x=-b/(2*a)
        print ("x = ", x)
    else:
        print("Brak rozwiazania, nie ma miejsc zerowych")
        
rownaniekwadratowe()
print()

# Zadanie 4

one = float(input("Podaj wartosc pierwszej liczby: "))
two = float(input("Podaj wartosc drugiej liczby: "))
three = float(input("Podaj wartosc trzeciej liczby: "))

if one > two and one > three and two > three:
    print(three,two,one)
elif one > two and one > three and two < three:
    print(two,three,one)
elif two > one and one > three and two > three:
    print(three,two,one)
elif two > one and one < three and two > three:
    print(one,three,two)
elif two > one and one < three and two < three:
    print(one,two,three)
elif two < one and one < three and two < three:
    print(two,one,three)
elif one > two and two == three:
    print(three,two,one)
elif two > one and one == three:
    print(three,one,two)
elif three > two and two == one:
    print(one,two,three)
elif three == one and two < one:
    print(two,one,three)
elif three == two and two > one:
    print(one,two,three)
elif one == two and two > three:
    print(three,two,one)
else:
    print("Wszystkie liczby są równe!")    

print()

# Zadanie 5

deszcz=input("Czy pada deszcz?: ")
if deszcz == "Tak":
    deszcz = True
else:
    deszcz = not True

autobus = input("Czy stoi autobus na przystanku?: ")
if autobus == "Tak":
    autobus = True
else:
    autobus = not True

if deszcz == True and autobus == True:
    print("Weź parasol")
elif deszcz == True and not autobus:
    print("Nie dostaniesz sie na uczelnie")
elif not deszcz and autobus == True:
    print("Dostaniesz się na uczelnie")
else:
    print("Tekst uzupełniający")

print()

# Zadanie 7

zamiana = input("Zamiana małej litery na dużą, bądź odwrotnie. Wprowadź literę: ")
litera = ""
for i in range (len(zamiana)):
    if zamiana[i].isupper():
        litera += zamiana[i].lower() # litera = litera + zamiana
    elif zamiana[i].islower():
        litera += zamiana[i].upper()
    else:
        litera += zamiana[i]
print(litera)
print()

# Zadanie 6

def menu():
    print("Jaka operacje chcesz wykonać?")
    print()
    print("1) dodawanie")
    print("2) odejmowanie")
    print("3) mnożenie")
    print("4) dzielenie")
    print("5) reszta z dzielenia")
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
        reszta()
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


def reszta():
    arg1 = float(input("Podaj argument 1: "))
    arg2 = float(input("Podaj argument 2: "))
    wynik = arg1 % arg2
    print("Wynik: ", wynik)
    print()

menu()







