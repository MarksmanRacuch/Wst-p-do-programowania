studenci = int(input("Jaka jest liczba studentów w grupie laboratoryjnej?: "))

zliczanie = 0

i = 0

while i < studenci:
    punkty = float(input("Ile punktów otrzymał student?: "))
    zliczanie = zliczanie + punkty
    i = i + 1

srednia = zliczanie / studenci
print("Średnia z punktów które zdobyli studenci wynosi: ", srednia)
    

