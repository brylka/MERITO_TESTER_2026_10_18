tekst = input("Podaj tekst: ")

print(f"Twój tekst: {tekst}")

if tekst.lower().replace(" ", "") == tekst[::-1].lower().replace(" ", ""):
    print("Twój tekst jest palindromem.")
else:
    print("Twój tekst NIE jest palindromem.")
