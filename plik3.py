# print(0.1)
# print(0.2)
# print(0.1 + 0.2)
# print(0.1, 0.2, 0.1 + 0.2, sep="\n")
# print(1, 2, sep="\n")
# print(1 + 2)

a = 0.1  # 0.1 * 100 = 10
b = 0.2  # 0.2 * 100 = 20
         # 10 + 20 = 30
         # 30 / 100 = 0.3

print(a + b)
print((int(a*100) + int(b*100))/100)

assert 1 + 2 == 3, "Kalkulator: 1 + 2 powinno dać 3"
assert 0.1 + 0.2 == 0.3, "Kalkulator: 0.1 + 0.2 powinno dać 0.3"