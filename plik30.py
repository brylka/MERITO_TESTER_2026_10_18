def przywitaj(imie, wiek, kraj = "Polska"):
    print(f"Cześć, {imie}.\nMasz {wiek} lat.")
    print(f"Mieszkasz w: {kraj}")

# przywitaj("Bartosz", 18)

def suma(a, b):
    return a+b

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

print(f"{a} + {b} = {suma(a,b)}")