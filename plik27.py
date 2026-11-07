a = [1,2,3]
b = a

b.append(4)
print(b)
print(a)

c = a.copy()
c.append(5)
print(c)
print(a)
print(b)


linia = "2026.11.07;12:10:38;Logowanie;PASS;Bartosz"
pola = linia.split(";")
# godzina = pola[1].split(":")
# print(godzina[1])
print(pola)
print("#".join(pola))