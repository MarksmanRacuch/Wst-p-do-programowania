studenci = int(input("Jaka jest liczba studentów w grupie laboratoryjnej?: "))

zliczanie = 0

i = 0

while i >= 0:
    punkty = float(input("Ile punktów otrzymał student?: "))
    if punkty > 0 and punkty < 101:
        continue
    else:
        break
zliczanie = zliczanie + punkty
i = i + 1

srednia = zliczanie / studenci
print("Średnia z punktów które zdobyli studenci wynosi: ", srednia)