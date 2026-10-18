wiek = int(input("Podaj wiek: "))
if wiek < 18:
    tekst = "niepełnoletni"
else:
    tekst = "pełnoletni"
print(f"Jesteś {tekst}")

print(f"Jesteś {"nie" if int(input("Podaj wiek: ")) < 18 else ""}pełnoletni")

