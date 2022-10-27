n = int(input("Podaj liczbę studentów: "))

i = 1
suma = 0

while i < n+1:
    punkty = float(input(f"Podaj liczbę punktów studenta {i}: "))
    suma = suma + punkty
    i = i + 1

srednia = suma / n
print("Srednia wynosi: ", srednia)
    

