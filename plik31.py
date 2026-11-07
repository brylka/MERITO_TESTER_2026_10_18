def suma(a, b):
    return (a*1000 + b*1000)/1000

def roznica(a, b):
    return a - b

def iloczyn(a, b):
    return a * b

def iloraz(a, b):
    if b == 0:
        raise ZeroDivisionError("Nie dzieli się przez zero")
    return a / b

if __name__ == '__main__':
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))

    print(f"{a} + {b} = {suma(a, b)}")
    print(f"{a} - {b} = {roznica(a, b)}")
    print(f"{a} * {b} = {iloczyn(a, b)}")
    try:
        print(f"{a} : {b} = {iloraz(a, b)}")
    except ZeroDivisionError as e:
        print(f"{a} : {b} = błąd: {e}")
