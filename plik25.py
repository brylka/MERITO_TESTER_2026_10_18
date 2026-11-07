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
    print(oceny[i])
    # zamiast drukować - dodać do sumy ocen
# wydrukować suma ocen/ilość ocen