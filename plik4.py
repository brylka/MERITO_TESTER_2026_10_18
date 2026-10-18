a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

# c = a + b
# print(str(a) + " + " + str(b) + " = " + str(c))
# print(a, "+", b, "=", c)
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
if b == 0:
    print("Nie dzieli się przez zero!")
else:
    print(f'{a} : {b} = {a / b}')
    print(f'Część całkowita {a} : {b} = {a // b}')
    print(f'Reszta z dzielenia {a} : {b} = {a % b}')
print(f"{a} do potęgi {b} = {a ** b}")

