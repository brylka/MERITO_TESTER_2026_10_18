for a in range(1,101):
    if a % 2 == 0:
        continue
    print(a, end=" ")
print()

for a in range(1,101):
    if a == 40:
        break
    print(a, end=" ")
print()

for a in range(-100,-201,-10):
    print(a, end=" ")
