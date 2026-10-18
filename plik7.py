tekst = input("Podaj tekst: ")
t = tekst.lower().replace(" ", "")

print(f"Twój tekst: {tekst}")

if t == t[::-1]:
    print("Twój tekst jest palindromem.")
else:
    print("Twój tekst NIE jest palindromem.")
