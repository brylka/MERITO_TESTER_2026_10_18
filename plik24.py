# Gra „Zgadnij liczbę”: program losuje liczbę 1–100 (random.randint(1, 100)), użytkownik zgaduje,
# program podpowiada „za mało” / „za dużo”. Na końcu wypisz liczbę prób.

import random

wylosowana = random.randint(1, 100)
proby = 0

while True:
    strzal = int(input("Podaj liczbę: "))
    proby += 1

    if strzal < wylosowana:
        print("za mało")
    elif strzal > wylosowana:
        print("za dużo")
    elif strzal == wylosowana:
        print(f"Brawo! Liczba prób: {proby}")
        break
