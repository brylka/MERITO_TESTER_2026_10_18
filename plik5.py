wiek = int(input("Podaj swój wiek: "))

if wiek < 0:
    print("Jeszcze się nie urodziłeś.")
elif wiek == 18:
    print("GRATULACJE! W tym roku osiągnąłeś pełnoletność!")
elif wiek > 120:
    print("Prawdopodobnie jesteś duchem!")
elif wiek > 18:
    print("Jesteś pełnoletni.")
else:
    print("Nie jesteś pełnoletni.")

# == porównywanie
# != jest różne
# > większe
# < mniejsze
# >= większe lub równe
# <= mniejsze lub równe