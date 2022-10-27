print("Program do wypisywania liczb z przedziału od liczby 1 do liczby 2")

liczba1 = int(input("Podaj liczbę 1: "))
liczba2 = int(input("Podaj liczbę 2: "))

while liczba1 in range(liczba1,liczba2+1):
    if liczba1 % 2 == 0: print(liczba1, end="  ")
    liczba1 = liczba1 + 1
    
    
print()
print()