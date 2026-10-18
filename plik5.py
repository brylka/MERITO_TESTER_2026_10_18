wiek = int(input("Podaj swój wiek: "))

if wiek < 0:
    print("Jeszcze się nie urodziłeś.")
else:
    if wiek >= 18:
        print("Jesteś pełnoletni.")
    else:
        print("Nie jesteś pełnoletni.")
