start = 2
ilosc = 28
print("PN\tWT\tŚR\tCZ\tPT\tSO\tND")
for dzien in range(1-start+1, ilosc+1):
    if dzien > 0:
        print(dzien, end="\t")
    else:
        print("", end="\t")
    if (dzien + start - 1) % 7 == 0:
        print()
