def przywitaj(imie, wiek, kraj = "Polska"):
    print(f"Cześć, {imie}.\nMasz {wiek} lat.")
    print(f"Mieszkasz w: {kraj}")

# przywitaj("Bartosz", 18)

def suma(a:float, b:float) -> float:
    return a+b

# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
#
# print(f"{a} + {b} = {suma(a,b)}")

def czy_parzysta(n):
    return n % 2 == 0

# print(czy_parzysta(3))

def statystyki(liczby):
    """
    Przyjmuje jako parametr listę liczb,
    zwraca czter wartości: wartość minimalna,
    wartość maksymalna, sumę liczb i średnią arytmetyczną.

    Args:
        liczby: lista floatów
    Returns:
        Maksimum
        Minimum
        Suma
        Średnia
    """
    return (min(liczby), max(liczby),
            sum(liczby), round(sum(liczby) / len(liczby),2))

e1, e2, e3, e4 = statystyki([3,5,4,6,2,3,4])
stat = statystyki([3,5,4,6,2,3,4])

# print(e4)
# print(stat[3])
# help(statystyki)

print(suma("4","5"))