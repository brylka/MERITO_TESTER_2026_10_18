lista = ["A", "B", "C"]

print(lista)
lista.append("D")
print(lista)
lista.insert(0,"E")
print(lista)
lista.remove("B")
print(lista)
lista.append("A")
print(lista)
lista.remove("A")
print(lista)
del lista[0]
print(lista)
ostatni = lista.pop()
print(lista)
print(ostatni)

print("C" in lista)
lista.append("A")
lista.append("A")
lista.append("A")
print(lista)
print(lista.count("A"))
print(lista.index("A"))


imiona = ["Adam", 'Bartosz', 'Cyprian', 'Daniel']

nr = 1
for imie in imiona:
    print(f"{nr} {imie}")
    nr += 1

print(40*"=")
for i in range(40):
    print("*", end="")
print()

for nr, imie in enumerate(imiona, start=1):
    print(f"{nr} {imie}")
