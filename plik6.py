#    012345678901234567890123
s = "ala ma kota a kot ma alę"
l = len(s) # ilość znaków w stringu
print(l)

print(s[10]) # drukuj znak o indeksie 10 - letra a
print(s[10:]) # drukuj od 10 indeksy do ostatniego
print(s[:10]) # drukuj od początku do 9 indeksu
print(s[4:14]) # drukuj od 4 indeksu do 13 indeksu
print(s[4:14:2]) # drukuj od 4 indeksu do 13 indeksu do 2 znak
print(s[-3]) # drukuj trzeci od końca znak
print(s[::-1]) # drukuj w odwrotnej kolejności

# print(s[-1])
#    0123456789012345678
s = "  Uniwersytet WSB Merito  "

print(s)
print(s.upper())
print(s.lower())
print(s.title()) # BARTOSZ -> Bartosz # bartosz -> Bartosz
print(s.strip())
print(s.count('M'))
print(s.find('WSB'))

s = "Bartosz Bryniarski"

print(s.startswith('Bart'))
print(s.endswith('ski'))
