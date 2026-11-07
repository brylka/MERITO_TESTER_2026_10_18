slownik = {"imie": "Bartosz",
        "nazwisko": "Bryniarski",
        "wiek": 18,
        "miasto": "Jelenia Góra"}

print(slownik["imie"])
slownik["imie"] = "Paweł"
print(slownik["imie"])
#print(slownik["wzrost"])
print(slownik.get("wzrost", "niepodany"))
slownik["waga"] = 90
print(slownik)

s = {0:"A", 1:"B", 2:"C", "imie":"Bartosz"}
l = ["A","B","C","Bartosz"]
print(s[1], l[1])
print(s["imie"])
print(l[3])
