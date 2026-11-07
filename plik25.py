#           0         1          2          3
imiona = ["Adam", 'Bartosz', 'Cyprian', 'Daniel']

print(len(imiona))
print(imiona[1])

#        0 1 2 3  4  5
oceny = [2,5,2,5.5,4,3]

print(f"Ilość ocen: {len(oceny)}")
print(f"Najlepsza ocena: {max(oceny)}")

suma = 0
for i in range(0,len(oceny)):
    # print(oceny[i])
    suma += oceny[i]
    # zamiast drukować - dodać do sumy ocen
print(f"Średnia ocen: {suma/len(oceny):.2f}")
# wydrukować suma ocen/ilość ocen

oceny.append(6)
print(oceny)

suma_nowa = 0
for ocena in oceny:
    suma_nowa += ocena
print(f"Nowa średnia ocen: {suma_nowa/len(oceny):.2f}")
