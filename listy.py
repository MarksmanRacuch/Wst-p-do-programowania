import random


lista_zakupow = ["kaczka","indyk","kurczak","kluski"]
print(lista_zakupow[0],lista_zakupow[1])
lista_zakupow.insert(2,"mleko")
print(lista_zakupow[2],lista_zakupow[3])

print()

zasieg = int(input("Jak długa ma byc lista?: "))
zestaw_1 = []
for i in range(0,zasieg):
    n = random.randint(1,10)
    zestaw_1.append(n)
print(zestaw_1)

zasieg2 = int(input("Jak długa ma byc lista?: "))
zestaw_2 = []
for i in range(0,zasieg2):
    n = random.randint(5,15)
    zestaw_2.append(n)
print(zestaw_2)

print()

zgadywanka = int(input("Podaj liczbe ktora chcesz sprawdzic: "))
h = zgadywanka

if h in zestaw_1 and h in zestaw_2:
    print("Liczba znajduje sie w obu listach")
elif h in zestaw_2:
    print("Liczba znajduje sie w liscie 2")
elif h in zestaw_1:
    print("Liczba znajduje sie w liscie 1")
else:
    print("Liczby nie ma w zadnej z list")

print()

zestaw1_2 = zestaw_1 + zestaw_2
zestaw1_2.sort()
print("Posortowana lista:")
print(zestaw1_2)

print()

zwierzeta = []

zwierzeta.extend(["Aksolotl","Samogłów","Suhak stepowy","Macracantha arcuata","Palczak madagaskarski"])
zwierzeta.sort()
print(zwierzeta[0]," ",zwierzeta[2]," ",zwierzeta[3]," ",zwierzeta[4])
print("Zwierzat na liscie jest:", len(zwierzeta))

print()

imiona = ["Kasia","Tomek","Jan","Ola","Jerzy","Marek","Piotr","Zuzia","Bartek","Jacek"]
print(imiona)
print()
dowolne_imie = str(input("Zamień imię 'Ola' na inne. Wybierz imię: "))
imiona[3] = dowolne_imie
dowolne_imie2 = str(input("Wybierz imię do dodania do listy: "))
imiona.insert(4,dowolne_imie2)
del imiona[6]
print()
print(imiona)
print()
imiona.insert(0,"Kunegunda")
imiona.insert(1,"Hermelegilda")
imiona.insert(2,"Andrzej")
del imiona[7]
dowolne_imie3 = str(input("Zamień ostatnie imię na liściena inne. Wybierz imię: "))
imiona[11] = dowolne_imie3
print()
print(imiona[0],imiona[1],imiona[2],imiona[9],imiona[10],imiona[11],)
print()
dowolne_imie4 = str(input("Podaj imię: "))
if dowolne_imie4 in imiona:
    print("Imię znajduje się na liście")
else:
    print("Podanego imienia nie ma na liście")
print()
print(sorted(imiona))
print(sorted(imiona, reverse=True))
del imiona[11]
del imiona[10]
del imiona[9]
del imiona[8]
del imiona[7]
del imiona[6]
print()
print("Liczba elementów listy wynosi:", len(imiona))
print()

punkty = []
su = 0
for i in range(0,15):
    n = random.randint(0,50)
    punkty.append(n)
    su = su + n
sr = su / 15

more = 0
less = 0
for i in list(punkty):
    if i >= sr:
        more = more + 1
    else:
        less = less + 1

print(punkty)
print()
print("Największa liczba punktów w liście to:", max(punkty))
print("Najmniejsza liczba punktów w liście to:", min(punkty))
print()
a = float(input("Podaj wybraną liczbę z listy: "))
if a in punkty:
    print(punkty.index(a))
else:
    print("Liczba nie występuje na liście")
print("Średnia z tych punktów wynosi:",sr)
print("Więcej pktów od średniej zdobyło:",more,"osób")
print("Mniej pktów od średniej zdobyło:",less,"osób")

lista_x = []

print()
print("Lista 10 elementowa:")
for i in range (0,10):
    n = input("Podaj dowolna nazwe: ")
    lista_x.append(n)
print()
print(lista_x)
print(lista_x[9:6:-1] + lista_x[:7])

lista_y = lista_x

lista_y[5] = "LOL"

print(lista_x)
print(lista_y)
