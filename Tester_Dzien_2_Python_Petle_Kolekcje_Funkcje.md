# Tester oprogramowania – Dzień 2

**Pętle, kolekcje, funkcje, wyjątki i praca z plikami**

| | |
|---|---|
| **Uczelnia** | Uniwersytet WSB Merito we Wrocławiu |
| **Kierunek** | Studia podyplomowe: Tester oprogramowania |
| **Moduł** | Tester jako developer narzędzi z pomocą Pythona |
| **Opracował** | Bartosz Bryniarski |
| **Wymiar** | 8 godzin dydaktycznych (8 × 45 min) |

---

## Plan dnia

| Nr | Temat | Zakres |
|---|---|---|
| 1 | Pętle `while` i `for` | `range()`, `break`, `continue`, `else`, ponawianie prób |
| 2 | Listy i krotki | Indeksowanie, metody, iteracja, rozpakowanie |
| 3 | Słowniki, zbiory i wyrażenia składane | `dict`, `set`, zliczanie, porównywanie danych, comprehensions |
| 4 | Funkcje | `def`, parametry, `return`, argumenty domyślne i nazwane, docstringi, typy |
| 5 | Funkcje cd. i testowanie funkcji | Zasięg, `*args`, `**kwargs`, `lambda`, przypadki testowe z `assert`, wartości brzegowe |
| 6 | Obsługa wyjątków | `try`/`except`/`else`/`finally`, `raise`, własne wyjątki |
| 7 | Operacje wejścia/wyjścia | Pliki tekstowe, `with`, `pathlib`, CSV, JSON |
| 8 | Projekt | Generator raportu z wyników testów |

---

## 1. Pętle `while` i `for`

### Cele
- powtarzać instrukcje za pomocą pętli,
- wybrać właściwy rodzaj pętli,
- sterować pętlą (`break`, `continue`, `else`).

### 1.1. Rozgrzewka – powtórka z dnia 1

Przewidź wynik bez uruchamiania:
```python
s = "Tester"
print(s[1:4])
print(s[-2:].upper())
print(len(s) % 4)
print(f"{10 / 3:.2f}")
print("ok" if "t" in s and len(s) > 5 else "nie")
```

### 1.2. Pętla `while` – powtarzaj, dopóki warunek jest prawdziwy

```python
licznik = 1
while licznik <= 5:
    print(f"Iteracja nr {licznik}")
    licznik += 1          # bez tej linii pętla byłaby nieskończona!
print("Koniec")
```

> **Pętla nieskończona** – jeśli warunek nigdy nie stanie się fałszywy. Przerwanie programu w PyCharm: czerwony kwadrat (*Stop*) lub **Ctrl + F2**; w terminalu: **Ctrl + C**.

**Walidacja danych wejściowych**
```python
wiek = int(input("Podaj wiek (0-120): "))
while wiek < 0 or wiek > 120:
    print("Niepoprawny wiek!")
    wiek = int(input("Podaj wiek (0-120): "))
print(f"Zapisano wiek: {wiek}")
```

**Pętla z „wartownikiem” – `while True` + `break`**
```python
suma = 0
while True:
    tekst = input("Podaj liczbę (pusty Enter kończy): ")
    if tekst == "":
        break
    suma += float(tekst)
print(f"Suma: {suma}")
```

### 1.3. Pętla `for` i funkcja `range()`

```python
for znak in "Python":
    print(znak)
```

| Wywołanie | Generuje |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 6)` | 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -1)` | 10, 9, …, 1 |

```python
for i in range(1, 6):
    print(f"{i} do kwadratu = {i ** 2}")
```

**Kiedy która pętla?** Znana liczba powtórzeń lub przechodzenie po elementach → `for`. Powtarzanie, aż coś się wydarzy → `while`.

### 1.4. `break`, `continue` i `else`

```python
# break – natychmiastowe wyjście z pętli
for i in range(1, 100):
    if i * i > 50:
        print(f"Pierwsza liczba, której kwadrat > 50: {i}")
        break

# continue – przejście do następnej iteracji
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")      # 1 2 4 5 7 8 10
print()
```

Blok `else` po pętli wykona się tylko wtedy, gdy pętla zakończyła się **bez `break`**.

### 1.5. Przykład z pracy testera – ponawianie prób (retry)

Testy często czekają na usługę, która nie zawsze odpowiada od razu. Typowy wzorzec: spróbuj kilka razy, a jeśli się nie uda – zgłoś błąd.

```python
import random

MAX_PROB = 5
proba = 1
while proba <= MAX_PROB:
    odpowiedz_ok = random.random() < 0.3      # symulacja niestabilnego serwera
    print(f"Próba {proba}: {'OK' if odpowiedz_ok else 'brak odpowiedzi'}")
    if odpowiedz_ok:
        print("Serwer odpowiedział – można testować dalej")
        break
    proba += 1
else:
    print("Serwer nie odpowiada – test niezaliczony")
```

### 1.6. Pętle zagnieżdżone

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:4}", end="")
    print()
```

### Ćwiczenie 1.1
Wypisz odliczanie od 10 do 0, a na końcu „Start!”. Zrób to raz pętlą `while`, raz pętlą `for`.

### Ćwiczenie 1.2
Gra „Zgadnij liczbę”: program losuje liczbę 1–100 (`random.randint(1, 100)`), użytkownik zgaduje, program podpowiada „za mało” / „za dużo”. Na końcu wypisz liczbę prób.

### Ćwiczenie 1.3
Logowanie: użytkownik ma 3 próby na podanie poprawnego hasła (`tajne123`). Po trzech błędach – „Konto zablokowane”. Użyj `for` + `break` + `else`.

### Ćwiczenie 1.4
FizzBuzz: dla liczb 1–30 wypisz „Fizz” (wielokrotności 3), „Buzz” (wielokrotności 5), „FizzBuzz” (wielokrotności 15), w pozostałych przypadkach – liczbę.

---

## 2. Listy i krotki

### Cele
- przechowywać wiele wartości w jednej zmiennej,
- modyfikować listy i przechodzić po nich,
- rozumieć, czym krotka różni się od listy.

### 2.1. Tworzenie i indeksowanie list

```python
wyniki = ["PASS", "FAIL", "PASS", "SKIP"]
czasy_ms = [120, 95, 340, 0]
pusta = []
z_range = list(range(1, 6))       # [1, 2, 3, 4, 5]

print(wyniki[0])      # PASS
print(wyniki[-1])     # SKIP
print(wyniki[1:3])    # ['FAIL', 'PASS']
print(len(wyniki))    # 4

wyniki[3] = "PASS"    # lista jest mutowalna – można ją zmieniać
```

### 2.2. Najważniejsze metody

```python
lista = [1, 2, 3]

lista.append(4)          # [1, 2, 3, 4]       – dodaj na koniec
lista.insert(0, 0)       # [0, 1, 2, 3, 4]    – wstaw na pozycję
lista.extend([5, 6])     # [0, 1, 2, 3, 4, 5, 6]
lista.remove(3)          # usuń pierwsze wystąpienie wartości 3
ostatni = lista.pop()    # usuń i zwróć ostatni element
del lista[0]             # usuń element o indeksie 0

liczby = [5, 2, 8, 2, 9, 1]
print(2 in liczby)                   # True
print(liczby.count(2))               # 2
print(liczby.index(8))               # 2
print(min(liczby), max(liczby), sum(liczby))

liczby.sort()                        # sortuje w miejscu
posortowane = sorted(liczby, reverse=True)   # zwraca NOWĄ listę
```

### 2.3. Iteracja: `enumerate` i `zip`

```python
testy = ["logowanie", "rejestracja", "koszyk"]
statusy = ["PASS", "FAIL", "PASS"]

for nr, nazwa in enumerate(testy, start=1):
    print(f"{nr}. {nazwa}")

for nazwa, status in zip(testy, statusy):
    print(f"{nazwa:<12} {status}")
```

### 2.4. Pułapka: kopiowanie list

```python
a = [1, 2, 3]
b = a            # b to TA SAMA lista!
b.append(4)
print(a)         # [1, 2, 3, 4]  (!)

c = a.copy()     # nowa, niezależna lista
c.append(5)
print(a)         # [1, 2, 3, 4]
```

### 2.5. Napisy ↔ listy

```python
linia = "TC-001;Logowanie;PASS;120"
pola = linia.split(";")              # ['TC-001', 'Logowanie', 'PASS', '120']
print(" | ".join(pola))              # TC-001 | Logowanie | PASS | 120
```

### 2.6. Krotki (tuple)

**Krotka** to niemutowalna (niezmienna) sekwencja – dobra dla danych, które nie powinny się zmieniać.

```python
rozdzielczosc = (1920, 1080)
jednoelementowa = (42,)       # przecinek jest konieczny!
# rozdzielczosc[0] = 1280     # TypeError – krotki nie można zmienić

# Rozpakowanie
szer, wys = rozdzielczosc
pierwszy, *srodek, ostatni = [1, 2, 3, 4, 5]
print(pierwszy, srodek, ostatni)   # 1 [2, 3, 4] 5

# Lista krotek – typowe dane testowe
dane_logowania = [
    ("anna@test.pl", "Haslo123!", True),
    ("anna@test.pl", "zle", False),
    ("", "Haslo123!", False),
]
for email, haslo, oczekiwany in dane_logowania:
    print(f"{email!r:<16} {haslo!r:<12} → oczekiwany wynik: {oczekiwany}")
```

> `{email!r}` wypisuje wartość „tak jak w kodzie”, z cudzysłowami – dzięki temu widać nawet pusty napis `''`.

### 2.7. Przykład z pracy testera – statystyka wykonania

```python
wyniki = ["PASS", "PASS", "FAIL", "PASS", "SKIP", "FAIL", "PASS"]

wykonane = len(wyniki) - wyniki.count("SKIP")
zaliczone = wyniki.count("PASS")
print(f"Zaliczone: {zaliczone}/{wykonane} ({zaliczone / wykonane:.0%})")
```

### Ćwiczenie 2.1
Wczytaj od użytkownika 5 czasów odpowiedzi serwera (ms) do listy. Wypisz: listę, średnią, minimum, maksimum oraz listę posortowaną malejąco.

### Ćwiczenie 2.2
Z listy `czasy = [120, 95, 340, 0, 210, 180, 890, 640]` utwórz listę czasów przekraczających 200 ms (pętla + `append`). Wypisz, ile ich jest.

### Ćwiczenie 2.3
Usuń duplikaty z listy `["TC-1", "TC-2", "TC-2", "TC-3", "TC-1"]`, zachowując kolejność pierwszych wystąpień.

### Ćwiczenie 2.4
Masz listę krotek `(nazwa_testu, czas_ms)`. Znajdź najwolniejszy test pętlą (bez `max`).

---

## 3. Słowniki, zbiory i wyrażenia składane

### Cele
- przechowywać dane w postaci par klucz–wartość,
- porównywać zbiory danych,
- zwięźle tworzyć kolekcje.

### 3.1. Słowniki (dict)

```python
przypadek = {
    "id": "TC-001",
    "tytul": "Logowanie poprawnym hasłem",
    "priorytet": "wysoki",
    "kroki": ["Otwórz stronę", "Wpisz dane", "Kliknij Zaloguj"],
    "status": "PASS",
}

print(przypadek["tytul"])
print(przypadek.get("autor"))             # None – brak klucza, ale bez błędu
print(przypadek.get("autor", "nieznany")) # wartość domyślna
# print(przypadek["autor"])               # KeyError

przypadek["autor"] = "Anna"               # dodanie
przypadek["status"] = "FAIL"              # modyfikacja
del przypadek["autor"]                    # usunięcie
print("kroki" in przypadek)               # True – sprawdza KLUCZE
```

**Iteracja**
```python
ceny = {"chleb": 4.5, "mleko": 3.99, "masło": 7.49}

for produkt in ceny:                  # po kluczach
    print(produkt)
for produkt, cena in ceny.items():    # po parach
    print(f"{produkt:<10}{cena:>6.2f} zł")
```

### 3.2. Klasyczny wzorzec – zliczanie

```python
statusy = ["PASS", "FAIL", "PASS", "SKIP", "PASS", "FAIL"]
licznik = {}
for s in statusy:
    licznik[s] = licznik.get(s, 0) + 1
print(licznik)          # {'PASS': 3, 'FAIL': 2, 'SKIP': 1}
```

> W bibliotece standardowej jest gotowe narzędzie: `collections.Counter` (dzień 3).

### 3.3. Zbiory (set) – unikalne elementy

```python
tagi = {"smoke", "regresja", "smoke", "api"}
print(tagi)                   # {'smoke', 'regresja', 'api'} – bez duplikatów
pusty = set()                 # UWAGA: {} to pusty słownik, nie zbiór!

a = {"Anna", "Jan", "Ola"}
b = {"Jan", "Kasia"}
print(a | b)    # suma
print(a & b)    # część wspólna: {'Jan'}
print(a - b)    # różnica: {'Anna', 'Ola'}
```

### 3.4. Przykład z pracy testera – czy odpowiedź API ma wszystkie pola?

```python
oczekiwane_pola = {"id", "email", "imie", "nazwisko"}
odpowiedz = {"id": 7, "email": "anna@test.pl", "imie": "Anna", "telefon": "123"}

brakujace = oczekiwane_pola - odpowiedz.keys()
nadmiarowe = odpowiedz.keys() - oczekiwane_pola

print("Brakujące pola:", brakujace)     # {'nazwisko'}
print("Nadmiarowe pola:", nadmiarowe)   # {'telefon'}
```

### 3.5. Wyrażenia składane (comprehensions)

```python
# tradycyjnie
kwadraty = []
for x in range(1, 6):
    kwadraty.append(x ** 2)

# list comprehension
kwadraty = [x ** 2 for x in range(1, 6)]

# z warunkiem
czasy = [120, 95, 340, 0, 210]
wolne = [c for c in czasy if c > 200]            # [340, 210]

# dict i set comprehension
dlugosci = {s: len(s) for s in ["kot", "pies", "chomik"]}
unikalne_litery = {z.lower() for z in "Mississippi"}
```

> Comprehensions są czytelne, gdy są **krótkie**. Jeśli nie mieści się w jednej linii – użyj zwykłej pętli.

### 3.6. Porównanie kolekcji

| Cecha | `list` | `tuple` | `set` | `dict` |
|---|---|---|---|---|
| Zapis | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"a": 1}` |
| Uporządkowana | ✅ | ✅ | ❌ | ✅ |
| Mutowalna | ✅ | ❌ | ✅ | ✅ |
| Duplikaty | ✅ | ✅ | ❌ | klucze ❌ |
| Dostęp | indeks | indeks | – | klucz |

### Ćwiczenie 3.1
Masz listę wyników: `[("TC-1", "PASS"), ("TC-2", "FAIL"), ("TC-3", "PASS"), ("TC-4", "FAIL"), ("TC-5", "SKIP")]`. Utwórz słownik `status → liczba testów` oraz listę identyfikatorów testów niezaliczonych.

### Ćwiczenie 3.2
Dwie wersje aplikacji mają listy dostępnych funkcji:
`v1 = ["login", "rejestracja", "koszyk", "płatność"]`, `v2 = ["login", "koszyk", "płatność", "czat", "wishlist"]`.
Wypisz: funkcje usunięte w v2, funkcje nowe w v2, funkcje wspólne (te trzeba przetestować regresyjnie).

### Ćwiczenie 3.3
Za pomocą comprehensions:
- a) lista liczb od 1 do 100 podzielnych przez 7,
- b) słownik `{słowo: długość}` dla zdania „tester znajduje błędy zanim zrobi to klient”,
- c) lista adresów e-mail `user1@test.pl` … `user5@test.pl`.

---

## 4. Funkcje

### Cele
- zrozumieć ideę programowania proceduralnego,
- definiować i wywoływać funkcje,
- przekazywać argumenty i zwracać wyniki.

### 4.1. Programowanie proceduralne

**Programowanie proceduralne** polega na dzieleniu programu na mniejsze, nazwane fragmenty – **funkcje** – z których każda realizuje jedno zadanie.

**Dlaczego to ważne dla testera?**
- funkcję można **przetestować osobno** – to podstawa testów jednostkowych,
- **DRY** (*Don't Repeat Yourself*) – kod narzędzia piszemy raz, używamy wielokrotnie,
- czytelność: `wygeneruj_email()` mówi więcej niż 5 linii kodu.

### 4.2. Definicja, parametry i `return`

```python
def przywitaj(imie):                 # imie – parametr
    print(f"Cześć, {imie}!")

przywitaj("Anna")                    # "Anna" – argument


def pole_prostokata(a, b):
    return a * b

wynik = pole_prostokata(3, 4)
print(wynik * 2)                     # 24 – zwrócony wynik można dalej używać
```

**`print` vs `return`** – kluczowa różnica:
```python
def suma_print(a, b):
    print(a + b)          # tylko wyświetla

def suma_return(a, b):
    return a + b          # zwraca wartość

x = suma_print(2, 3)      # wypisze 5
print(x)                  # None (!)
y = suma_return(2, 3)
print(y)                  # 5
```

> Funkcję, która **zwraca** wynik, łatwo przetestować. Funkcję, która tylko **wypisuje** – znacznie trudniej. Dlatego logika powinna zwracać wyniki, a wypisywanie zostawiamy na koniec programu.

**`return` kończy funkcję natychmiast; można zwrócić kilka wartości**
```python
def czy_parzysta(n):
    return n % 2 == 0

def statystyki(liczby):
    return min(liczby), max(liczby), sum(liczby) / len(liczby)

najmn, najw, sr = statystyki([120, 95, 340, 210])
```

### 4.3. Argumenty domyślne i nazwane

```python
def wygeneruj_email(numer, domena="test.pl", prefiks="user"):
    return f"{prefiks}{numer}@{domena}"

print(wygeneruj_email(1))                          # user1@test.pl
print(wygeneruj_email(2, "example.com"))           # user2@example.com
print(wygeneruj_email(3, prefiks="admin"))         # admin3@test.pl
print(wygeneruj_email(domena="qa.pl", numer=4))    # kolejność dowolna
```

> Parametry z wartością domyślną muszą być **po** parametrach bez niej.

**Pułapka – mutowalna wartość domyślna:**
```python
def dodaj(element, lista=[]):     # ŹLE! lista tworzona raz, współdzielona
    lista.append(element)
    return lista

print(dodaj(1))   # [1]
print(dodaj(2))   # [1, 2]  (!)

def dodaj(element, lista=None):   # DOBRZE
    if lista is None:
        lista = []
    lista.append(element)
    return lista
```

### 4.4. Docstringi i adnotacje typów

```python
def cena_brutto(netto: float, vat: float = 0.23) -> float:
    """
    Zwraca cenę brutto zaokrągloną do 2 miejsc.

    Args:
        netto: cena netto w zł.
        vat: stawka VAT, np. 0.23 dla 23%.

    Returns:
        Cena brutto.
    """
    return round(netto * (1 + vat), 2)


help(cena_brutto)
```

> Adnotacje typów **nie są wymuszane** przez interpreter – służą czytelności i podpowiedziom PyCharm.

### 4.5. Funkcja `main` i `if __name__ == "__main__":`

```python
def cena_brutto(netto, vat=0.23):
    return round(netto * (1 + vat), 2)


def main():
    netto = float(input("Kwota netto: "))
    print(f"Kwota brutto: {cena_brutto(netto)} zł")


if __name__ == "__main__":
    main()
```

Blok `if __name__ == "__main__":` wykona się tylko przy bezpośrednim uruchomieniu pliku, a nie przy jego imporcie (więcej w dniu 3). Dzięki temu plik z testami może zaimportować `cena_brutto` bez uruchamiania `main()`.

### Ćwiczenie 4.1
Napisz funkcję `ocena(punkty)` zwracającą ocenę według skali z dnia 1 (≥90 → 5.0, ≥80 → 4.5, ≥70 → 4.0, ≥60 → 3.5, ≥50 → 3.0, poniżej → 2.0).

### Ćwiczenie 4.2
Napisz funkcję `czy_przestepny(rok)` zwracającą `True`/`False`.

### Ćwiczenie 4.3
Napisz funkcję `pass_rate(wyniki)`, która dla listy statusów (`"PASS"`, `"FAIL"`, `"SKIP"`) zwraca procent zaliczonych testów spośród wykonanych (SKIP nie liczymy). Dla listy bez wykonanych testów zwróć `0.0`.

### Ćwiczenie 4.4
Napisz funkcję `formatuj_cene(kwota, waluta="zł", miejsca=2)`, np. `formatuj_cene(1234.5)` → `"1234.50 zł"`.

---

## 5. Funkcje cd. i testowanie funkcji

### Cele
- rozumieć zasięg zmiennych,
- stosować `*args`, `**kwargs` i `lambda`,
- **pisać pierwsze testy funkcji** z użyciem `assert`,
- dobierać dane testowe metodą klas równoważności i wartości brzegowych.

### 5.1. Zasięg zmiennych

```python
x = "globalna"

def funkcja():
    y = "lokalna"
    print(x)      # odczyt zmiennej globalnej – OK
    print(y)

funkcja()
# print(y)        # NameError – y istnieje tylko wewnątrz funkcji
```

> Unikaj `global`. Funkcja powinna dostawać dane przez **parametry** i oddawać wynik przez **`return`** – wtedy da się ją testować niezależnie od reszty programu.

Uwaga na listy i słowniki przekazane do funkcji – funkcja może je **zmienić** (efekt uboczny):
```python
def dodaj_wynik(wyniki, status):
    wyniki.append(status)       # modyfikuje oryginalną listę!

moje = ["PASS"]
dodaj_wynik(moje, "FAIL")
print(moje)                     # ['PASS', 'FAIL']
```

### 5.2. `*args` i `**kwargs`

```python
def srednia(*liczby):              # liczby to krotka
    if not liczby:
        return None
    return sum(liczby) / len(liczby)

print(srednia(4, 5, 3))            # 4.0
print(srednia(*[120, 95, 340]))    # rozpakowanie listy do argumentów


def utworz_uzytkownika(email, **dodatkowe):    # dodatkowe to słownik
    uzytkownik = {"email": email, "aktywny": True}
    uzytkownik.update(dodatkowe)
    return uzytkownik

print(utworz_uzytkownika("a@test.pl", rola="admin", jezyk="pl"))
```

### 5.3. `lambda` – krótka funkcja anonimowa

```python
wyniki = [("TC-1", 120), ("TC-2", 890), ("TC-3", 340)]

posortowane = sorted(wyniki, key=lambda w: w[1], reverse=True)
print(posortowane[0])                                # ('TC-2', 890) – najwolniejszy
print(max(wyniki, key=lambda w: w[1]))               # to samo krócej
```

### 5.4. Pierwsze testy funkcji

W dniu 1 poznaliśmy `assert`. Teraz użyjemy go do sprawdzania **własnych funkcji**.

```python
def cena_brutto(netto, vat=0.23):
    return round(netto * (1 + vat), 2)


def test_cena_brutto_domyslny_vat():
    assert cena_brutto(100) == 123.0


def test_cena_brutto_inny_vat():
    assert cena_brutto(100, vat=0.08) == 108.0


def test_cena_brutto_zero():
    assert cena_brutto(0) == 0


if __name__ == "__main__":
    test_cena_brutto_domyslny_vat()
    test_cena_brutto_inny_vat()
    test_cena_brutto_zero()
    print("Wszystkie testy zaliczone ✅")
```

**Konwencja:** funkcja testowa zaczyna się od `test_`, a jej nazwa mówi, **co** sprawdza. Tę konwencję wykorzysta w dniu 3 narzędzie `pytest` – automatycznie znajdzie i uruchomi takie funkcje.

Każdy test ma budowę **AAA**:
- **Arrange** – przygotuj dane,
- **Act** – wywołaj testowaną funkcję,
- **Assert** – sprawdź wynik.

```python
def test_statystyki():
    dane = [120, 95, 340]                    # Arrange
    najmn, najw, sr = statystyki(dane)       # Act
    assert najmn == 95                       # Assert
    assert najw == 340
    assert sr == 185
```

### 5.5. Jak dobrać dane testowe? Klasy równoważności i wartości brzegowe

Nie da się przetestować wszystkich możliwych wartości. Tester dzieli dane wejściowe na **klasy równoważności** (grupy, dla których program powinien zachowywać się tak samo) i sprawdza **wartości brzegowe** – miejsca, w których najczęściej czają się błędy.

**Przykład:** bilet ulgowy przysługuje osobom w wieku 0–17 lat, normalny 18–64, senioralny od 65.

| Klasa | Przedział | Wartości brzegowe do sprawdzenia |
|---|---|---|
| niepoprawny | < 0 | -1 |
| ulgowy | 0–17 | 0, 17 |
| normalny | 18–64 | 18, 64 |
| senioralny | ≥ 65 | 65 |

```python
def rodzaj_biletu(wiek):
    if wiek < 0:
        return "błąd"
    if wiek < 18:
        return "ulgowy"
    if wiek < 65:
        return "normalny"
    return "senioralny"


def test_rodzaj_biletu_wartosci_brzegowe():
    assert rodzaj_biletu(-1) == "błąd"
    assert rodzaj_biletu(0) == "ulgowy"
    assert rodzaj_biletu(17) == "ulgowy"
    assert rodzaj_biletu(18) == "normalny"
    assert rodzaj_biletu(64) == "normalny"
    assert rodzaj_biletu(65) == "senioralny"
```

> Gdyby programista napisał `wiek <= 18` zamiast `wiek < 18`, test dla wartości **18** od razu by to wykrył. Test dla „typowego” wieku 30 – nigdy.

**Wiele przypadków w pętli (testy sterowane danymi):**
```python
def test_rodzaj_biletu_tabela():
    przypadki = [
        (-1, "błąd"), (0, "ulgowy"), (17, "ulgowy"),
        (18, "normalny"), (64, "normalny"), (65, "senioralny"),
    ]
    for wiek, oczekiwany in przypadki:
        wynik = rodzaj_biletu(wiek)
        assert wynik == oczekiwany, f"wiek={wiek}: oczekiwano {oczekiwany}, jest {wynik}"
```

> Komunikat po przecinku w `assert` jest bardzo ważny – gdy test się wywali, od razu widać, **dla jakich danych**.

### Ćwiczenie 5.1
Napisz testy (funkcje `test_...`) dla `ocena(punkty)` z ćw. 4.1. Wyznacz wartości brzegowe dla każdego progu.

### Ćwiczenie 5.2
Napisz testy dla `czy_przestepny(rok)`. Uwzględnij wszystkie klasy: podzielny przez 4, przez 100, przez 400, niepodzielny przez 4.

### Ćwiczenie 5.3
Napisz testy dla `pass_rate()` z ćw. 4.3, w tym przypadki szczególne: pusta lista, same SKIP, same PASS.

### Ćwiczenie 5.4 – znajdź błąd 🐞
Poniższa funkcja powinna zwracać `True` dla haseł mających **co najmniej 8 znaków** i zawierających **co najmniej jedną cyfrę**. Napisz testy, które wykryją ukryty błąd.
```python
def czy_haslo_poprawne(haslo):
    if len(haslo) > 8:
        for znak in haslo:
            if znak.isdigit():
                return True
        return False
    return False
```

---

## 6. Obsługa wyjątków

### Cele
- czytać komunikaty o błędach (traceback),
- przechwytywać i obsługiwać wyjątki,
- zgłaszać własne wyjątki.

### 6.1. Czym jest wyjątek?

**Wyjątek** to błąd, który pojawił się w trakcie działania programu. Jeśli nikt go nie obsłuży – program się zatrzymuje i wypisuje **traceback**:

```
Traceback (most recent call last):
  File "kalkulator.py", line 3, in <module>
    wynik = 10 / dzielnik
            ~~~^~~~~~~~~~
ZeroDivisionError: division by zero
```

**Jak czytać traceback?** Od **dołu**: ostatnia linia to typ i opis błędu, nad nią – plik i numer linii, w której błąd wystąpił.

| Wyjątek | Kiedy występuje | Przykład |
|---|---|---|
| `ValueError` | zła wartość | `int("abc")` |
| `TypeError` | zły typ | `"a" + 1` |
| `ZeroDivisionError` | dzielenie przez zero | `1 / 0` |
| `IndexError` | indeks poza listą | `[1, 2][5]` |
| `KeyError` | brak klucza w słowniku | `{}["x"]` |
| `FileNotFoundError` | brak pliku | `open("brak.txt")` |
| `AssertionError` | niespełniona asercja | `assert 1 == 2` |

### 6.2. `try` / `except`

```python
try:
    liczba = int(input("Podaj liczbę: "))
    print(f"Odwrotność: {1 / liczba}")
except ValueError:
    print("To nie jest liczba!")
except ZeroDivisionError:
    print("Zero nie ma odwrotności!")
```

Dostęp do treści błędu:
```python
try:
    int("abc")
except ValueError as e:
    print(f"Błąd: {e}")     # Błąd: invalid literal for int() with base 10: 'abc'
```

> **Nie łap wszystkiego na ślepo** (`except:` lub `except Exception:` bez potrzeby). Ukrywa to błędy – a tester chce je widzieć!

### 6.3. `else` i `finally`

```python
try:
    plik = open("dane.txt", encoding="utf-8")
except FileNotFoundError:
    print("Brak pliku z danymi testowymi")
else:
    print(plik.read())          # wykona się tylko, gdy NIE było wyjątku
    plik.close()
finally:
    print("Koniec próby odczytu")   # wykona się ZAWSZE
```

`finally` służy do sprzątania (zamykanie połączeń, usuwanie plików tymczasowych) – tak jak *teardown* w testach.

### 6.4. Wzorzec: wczytywanie aż do skutku

```python
def wczytaj_liczbe(komunikat):
    while True:
        try:
            return float(input(komunikat))
        except ValueError:
            print("Niepoprawna liczba, spróbuj ponownie.")
```

### 6.5. Zgłaszanie wyjątków – `raise`

Funkcja, która dostała złe dane, powinna to **głośno zgłosić**, a nie zwracać dziwny wynik:

```python
def rodzaj_biletu(wiek):
    if not isinstance(wiek, int):
        raise TypeError("Wiek musi być liczbą całkowitą")
    if wiek < 0:
        raise ValueError(f"Wiek nie może być ujemny: {wiek}")
    if wiek < 18:
        return "ulgowy"
    if wiek < 65:
        return "normalny"
    return "senioralny"
```

### 6.6. Własne wyjątki

```python
class BladWalidacji(Exception):
    """Zgłaszany, gdy dane testowe są niepoprawne."""


def sprawdz_email(email):
    if "@" not in email:
        raise BladWalidacji(f"Brak znaku @ w adresie: {email!r}")
    return True


try:
    sprawdz_email("anna.test.pl")
except BladWalidacji as e:
    print(f"Walidacja nie przeszła: {e}")
```

> Słowo `class` poznamy dokładnie w dniu 3 – na razie wystarczy ten wzorzec.

### 6.7. Testowanie wyjątków

Test powinien sprawdzić także, czy funkcja **zgłasza błąd**, gdy powinna:

```python
def test_rodzaj_biletu_ujemny_wiek():
    try:
        rodzaj_biletu(-1)
    except ValueError:
        pass                  # dobrze – wyjątek wystąpił
    else:
        assert False, "Oczekiwano ValueError dla wieku -1"
```

> W dniu 3 zapiszemy to krócej: `with pytest.raises(ValueError):`.

### 6.8. `assert` a wyjątki – kiedy co?

- `assert` – w **testach** (sprawdzamy oczekiwany wynik),
- `raise` – w **kodzie aplikacji/narzędzia** (reagujemy na złe dane).

`assert` można wyłączyć przełącznikiem `python -O`, więc nie używamy go do walidacji danych w kodzie produkcyjnym.

### Ćwiczenie 6.1
Napisz funkcję `bezpieczne_dzielenie(a, b)`, która zwraca wynik dzielenia lub `None`, gdy `b == 0`. Napisz do niej testy.

### Ćwiczenie 6.2
Zmień `pass_rate()` z ćw. 4.3 tak, aby zgłaszała `ValueError`, gdy na liście pojawi się nieznany status (np. `"OK"`). Napisz test sprawdzający ten wyjątek.

### Ćwiczenie 6.3
Napisz program, który prosi o indeks i wypisuje element listy `["login", "koszyk", "płatność"]`. Obsłuż `ValueError` (to nie liczba) i `IndexError` (brak elementu) z odpowiednimi komunikatami.

---

## 7. Operacje wejścia/wyjścia

### Cele
- czytać i zapisywać pliki tekstowe,
- pracować z plikami CSV i JSON – najczęstszymi formatami danych testowych,
- korzystać z `pathlib`.

### 7.1. Otwieranie plików i `with`

```python
with open("notatki.txt", "w", encoding="utf-8") as plik:
    plik.write("Pierwsza linia\n")
    plik.write("Druga linia\n")
# tutaj plik jest już automatycznie zamknięty – nawet jeśli wystąpił wyjątek
```

| Tryb | Znaczenie |
|---|---|
| `"r"` | odczyt (domyślny); błąd, gdy plik nie istnieje |
| `"w"` | zapis; **nadpisuje** zawartość, tworzy plik |
| `"a"` | dopisywanie na końcu |
| `"x"` | utworzenie; błąd, gdy plik istnieje |

> Zawsze podawaj `encoding="utf-8"` – inaczej polskie znaki mogą się „rozsypać” (zwłaszcza na Windows).

### 7.2. Odczyt

```python
with open("notatki.txt", encoding="utf-8") as plik:
    cala_tresc = plik.read()            # cały plik jako jeden napis

with open("notatki.txt", encoding="utf-8") as plik:
    for linia in plik:                  # linia po linii – oszczędza pamięć
        print(linia.strip())

with open("notatki.txt", encoding="utf-8") as plik:
    linie = plik.read().splitlines()    # lista linii bez \n
```

### 7.3. Przykład z pracy testera – analiza logów

Plik `aplikacja.log`:
```
2026-10-29 10:15:01 INFO Start aplikacji
2026-10-29 10:15:02 INFO Połączono z bazą
2026-10-29 10:15:07 WARNING Wolna odpowiedź: 1200 ms
2026-10-29 10:15:09 ERROR Timeout podczas płatności
2026-10-29 10:15:12 INFO Użytkownik zalogowany
2026-10-29 10:15:15 ERROR Brak produktu o id=42
```

```python
bledy = []
with open("aplikacja.log", encoding="utf-8") as plik:
    for linia in plik:
        if " ERROR " in linia:
            bledy.append(linia.strip())

print(f"Znaleziono błędów: {len(bledy)}")
for b in bledy:
    print(" -", b)
```

### 7.4. `pathlib` – wygodna praca ze ścieżkami

```python
from pathlib import Path

katalog = Path("raporty")
katalog.mkdir(exist_ok=True)              # utwórz, jeśli nie istnieje

plik = katalog / "wynik.txt"              # łączenie ścieżek operatorem /
plik.write_text("PASS\n", encoding="utf-8")
print(plik.read_text(encoding="utf-8"))
print(plik.exists(), plik.name, plik.suffix)   # True wynik.txt .txt

for p in Path(".").glob("*.log"):          # wszystkie pliki .log w katalogu
    print(p)
```

### 7.5. Pliki CSV

Plik `uzytkownicy.csv` (dane testowe):
```
email,haslo,oczekiwany_wynik
anna@test.pl,Haslo123!,sukces
jan@test.pl,zle,blad
,Haslo123!,blad
```

```python
import csv

with open("uzytkownicy.csv", encoding="utf-8", newline="") as plik:
    for wiersz in csv.DictReader(plik):         # każdy wiersz to słownik
        print(wiersz["email"], wiersz["oczekiwany_wynik"])
```

Zapis:
```python
import csv

wyniki = [
    {"id": "TC-1", "status": "PASS", "czas_ms": 120},
    {"id": "TC-2", "status": "FAIL", "czas_ms": 340},
]
with open("wyniki.csv", "w", encoding="utf-8", newline="") as plik:
    writer = csv.DictWriter(plik, fieldnames=["id", "status", "czas_ms"])
    writer.writeheader()
    writer.writerows(wyniki)
```

> `newline=""` przy plikach CSV zapobiega pustym liniom między wierszami na Windows.
> Wartości z CSV są zawsze **napisami** – liczby trzeba skonwertować: `int(wiersz["czas_ms"])`.

### 7.6. Pliki JSON

JSON to format używany przez większość API – tester spotyka go codziennie.

```python
import json

konfiguracja = {
    "srodowisko": "test",
    "base_url": "https://test.example.com",
    "timeout_s": 5,
    "przegladarki": ["chrome", "firefox"],
    "debug": True,
}

# zapis do pliku
with open("config.json", "w", encoding="utf-8") as plik:
    json.dump(konfiguracja, plik, indent=2, ensure_ascii=False)

# odczyt z pliku
with open("config.json", encoding="utf-8") as plik:
    cfg = json.load(plik)
print(cfg["base_url"], cfg["przegladarki"][0])

# napis ↔ obiekt (np. odpowiedź z API)
tekst = '{"id": 7, "email": "anna@test.pl", "aktywny": true}'
dane = json.loads(tekst)
print(dane["aktywny"])                  # True
print(json.dumps(dane, indent=2))
```

| JSON | Python |
|---|---|
| obiekt `{}` | `dict` |
| tablica `[]` | `list` |
| `"tekst"` | `str` |
| `1`, `1.5` | `int`, `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

### Ćwiczenie 7.1
Dla pliku `aplikacja.log` policz, ile jest wpisów każdego poziomu (`INFO`, `WARNING`, `ERROR`). Wskazówka: `linia.split()[2]`.

### Ćwiczenie 7.2
Wczytaj `uzytkownicy.csv` i zapisz te same dane do `uzytkownicy.json` jako listę słowników.

### Ćwiczenie 7.3
Napisz funkcję `wczytaj_konfiguracje(sciezka)`, która zwraca słownik z pliku JSON, a gdy plik nie istnieje – zwraca konfigurację domyślną `{"srodowisko": "test", "timeout_s": 5}`.

---

## 8. Projekt: generator raportu z wyników testów

### Cel
Napisać narzędzie, które wczytuje wyniki testów z pliku CSV, liczy statystyki i zapisuje raport w JSON. Wykorzystujemy: pętle, kolekcje, funkcje, wyjątki, pliki i **testy własnego narzędzia**.

### 8.1. Dane wejściowe – `wyniki_testow.csv`

```
id,nazwa,modul,status,czas_ms
TC-001,Logowanie poprawne,logowanie,PASS,120
TC-002,Logowanie złe hasło,logowanie,PASS,95
TC-003,Rejestracja nowego konta,rejestracja,FAIL,340
TC-004,Reset hasła,logowanie,SKIP,0
TC-005,Dodanie do koszyka,koszyk,PASS,210
TC-006,Usunięcie z koszyka,koszyk,FAIL,180
TC-007,Płatność kartą,platnosci,PASS,890
TC-008,Płatność BLIK,platnosci,PASS,640
TC-009,Zwrot płatności,platnosci,PASS,abc
```

> Ostatni wiersz celowo ma błędny czas – narzędzie musi sobie z tym poradzić (pominąć wiersz i ostrzec), a nie się wywalić.

### 8.2. Wymagania

| Funkcja | Zadanie |
|---|---|
| `wczytaj_wyniki(sciezka)` | zwraca listę słowników; `czas_ms` jako `int`; błędne wiersze pomija z ostrzeżeniem |
| `podsumowanie(wyniki)` | zwraca słownik: `razem`, `PASS`, `FAIL`, `SKIP`, `pass_rate` (% zaliczonych spośród wykonanych) |
| `nieudane(wyniki)` | zwraca listę identyfikatorów testów `FAIL` |
| `najwolniejsze(wyniki, n=3)` | zwraca `n` najwolniejszych testów |
| `wg_modulu(wyniki)` | zwraca `{modul: {"PASS": x, "FAIL": y, "SKIP": z}}` |
| `zapisz_raport(raport, sciezka)` | zapisuje raport do JSON |
| `main()` | łączy wszystko i wypisuje podsumowanie |

### 8.3. Szkielet – `raport.py`

```python
"""Generator raportu z wyników testów."""
import csv
import json

STATUSY = ("PASS", "FAIL", "SKIP")


def wczytaj_wyniki(sciezka: str) -> list:
    # TODO: csv.DictReader, konwersja czas_ms na int,
    #       pominięcie wierszy z błędnym czasem lub nieznanym statusem
    pass


def podsumowanie(wyniki: list) -> dict:
    # TODO
    pass


def nieudane(wyniki: list) -> list:
    # TODO
    pass


def najwolniejsze(wyniki: list, n: int = 3) -> list:
    # TODO: sorted + lambda
    pass


def wg_modulu(wyniki: list) -> dict:
    # TODO
    pass


def zapisz_raport(raport: dict, sciezka: str) -> None:
    # TODO: json.dump z indent=2 i ensure_ascii=False
    pass


def main() -> None:
    # TODO: obsłuż FileNotFoundError
    pass


if __name__ == "__main__":
    main()
```

### 8.4. Testy narzędzia – `test_raport.py`

Narzędzie testera też trzeba testować! Testy nie korzystają z pliku – dane przygotowujemy w kodzie, dzięki czemu są szybkie i niezależne.

```python
from raport import podsumowanie, nieudane, najwolniejsze, wg_modulu

DANE = [
    {"id": "T1", "nazwa": "a", "modul": "m1", "status": "PASS", "czas_ms": 100},
    {"id": "T2", "nazwa": "b", "modul": "m1", "status": "FAIL", "czas_ms": 300},
    {"id": "T3", "nazwa": "c", "modul": "m2", "status": "SKIP", "czas_ms": 0},
    {"id": "T4", "nazwa": "d", "modul": "m2", "status": "PASS", "czas_ms": 200},
]


def test_podsumowanie():
    p = podsumowanie(DANE)
    assert p["razem"] == 4
    assert p["PASS"] == 2
    assert p["FAIL"] == 1
    assert p["SKIP"] == 1
    assert p["pass_rate"] == 66.67        # 2 z 3 wykonanych


def test_podsumowanie_pusta_lista():
    assert podsumowanie([])["pass_rate"] == 0.0


def test_nieudane():
    assert nieudane(DANE) == ["T2"]


def test_najwolniejsze():
    ids = [w["id"] for w in najwolniejsze(DANE, n=2)]
    assert ids == ["T2", "T4"]


def test_wg_modulu():
    assert wg_modulu(DANE) == {
        "m1": {"PASS": 1, "FAIL": 1, "SKIP": 0},
        "m2": {"PASS": 1, "FAIL": 0, "SKIP": 1},
    }


if __name__ == "__main__":
    test_podsumowanie()
    test_podsumowanie_pusta_lista()
    test_nieudane()
    test_najwolniejsze()
    test_wg_modulu()
    print("Wszystkie testy zaliczone ✅")
```

> Wskazówka: najpierw uruchom testy na pustym szkielecie – wszystkie się wywalą. Potem uzupełniaj funkcje jedną po drugiej, aż testy przejdą. To przedsmak podejścia **TDD**, któremu poświęcimy osobne zajęcia.

### 8.5. Przykładowe rozwiązanie (dla prowadzącego)

<details>
<summary>Pokaż pełne rozwiązanie</summary>

```python
"""Generator raportu z wyników testów."""
import csv
import json

STATUSY = ("PASS", "FAIL", "SKIP")


def wczytaj_wyniki(sciezka: str) -> list:
    """Wczytuje wyniki z CSV. Błędne wiersze pomija z ostrzeżeniem."""
    wyniki = []
    with open(sciezka, encoding="utf-8", newline="") as plik:
        for nr, wiersz in enumerate(csv.DictReader(plik), start=2):
            try:
                wiersz["czas_ms"] = int(wiersz["czas_ms"])
                if wiersz["status"] not in STATUSY:
                    raise ValueError(f"nieznany status {wiersz['status']!r}")
            except ValueError as e:
                print(f"⚠ Pomijam linię {nr}: {e}")
                continue
            wyniki.append(wiersz)
    return wyniki


def podsumowanie(wyniki: list) -> dict:
    wynik = {"razem": len(wyniki)}
    for status in STATUSY:
        wynik[status] = sum(1 for w in wyniki if w["status"] == status)
    wykonane = wynik["PASS"] + wynik["FAIL"]
    wynik["pass_rate"] = round(wynik["PASS"] / wykonane * 100, 2) if wykonane else 0.0
    return wynik


def nieudane(wyniki: list) -> list:
    return [w["id"] for w in wyniki if w["status"] == "FAIL"]


def najwolniejsze(wyniki: list, n: int = 3) -> list:
    return sorted(wyniki, key=lambda w: w["czas_ms"], reverse=True)[:n]


def wg_modulu(wyniki: list) -> dict:
    moduly = {}
    for w in wyniki:
        if w["modul"] not in moduly:
            moduly[w["modul"]] = {s: 0 for s in STATUSY}
        moduly[w["modul"]][w["status"]] += 1
    return moduly


def zapisz_raport(raport: dict, sciezka: str) -> None:
    with open(sciezka, "w", encoding="utf-8") as plik:
        json.dump(raport, plik, indent=2, ensure_ascii=False)


def main() -> None:
    try:
        wyniki = wczytaj_wyniki("wyniki_testow.csv")
    except FileNotFoundError:
        print("Nie znaleziono pliku wyniki_testow.csv")
        return

    p = podsumowanie(wyniki)
    print(f"\nTesty: {p['razem']} | PASS: {p['PASS']} | "
          f"FAIL: {p['FAIL']} | SKIP: {p['SKIP']} | pass rate: {p['pass_rate']}%")

    print("\nNiezaliczone:", ", ".join(nieudane(wyniki)) or "brak")

    print("\nNajwolniejsze testy:")
    for w in najwolniejsze(wyniki):
        print(f"  {w['id']:<8}{w['nazwa']:<28}{w['czas_ms']:>6} ms")

    print("\nWyniki według modułu:")
    for modul, staty in wg_modulu(wyniki).items():
        print(f"  {modul:<12} {staty}")

    raport = {
        "podsumowanie": p,
        "nieudane": nieudane(wyniki),
        "wg_modulu": wg_modulu(wyniki),
    }
    zapisz_raport(raport, "raport.json")
    print("\nZapisano raport.json")


if __name__ == "__main__":
    main()
```

Oczekiwany wynik:
```
⚠ Pomijam linię 10: invalid literal for int() with base 10: 'abc'

Testy: 8 | PASS: 5 | FAIL: 2 | SKIP: 1 | pass rate: 71.43%

Niezaliczone: TC-003, TC-006

Najwolniejsze testy:
  TC-007  Płatność kartą                 890 ms
  TC-008  Płatność BLIK                  640 ms
  TC-003  Rejestracja nowego konta       340 ms

Wyniki według modułu:
  logowanie    {'PASS': 2, 'FAIL': 0, 'SKIP': 1}
  rejestracja  {'PASS': 0, 'FAIL': 1, 'SKIP': 0}
  koszyk       {'PASS': 1, 'FAIL': 1, 'SKIP': 0}
  platnosci    {'PASS': 2, 'FAIL': 0, 'SKIP': 0}

Zapisano raport.json
```
</details>

### 8.6. Rozszerzenia dla chętnych

1. Dodaj do raportu średni czas wykonania testów w każdym module.
2. Zapisz listę niezaliczonych testów do osobnego pliku `do_ponownego_uruchomienia.txt`.
3. Wygeneruj raport w formie prostej strony HTML (tabela z kolorami: zielony PASS, czerwony FAIL).
4. Pozwól podać nazwę pliku CSV jako argument uruchomienia: `python raport.py moje_wyniki.csv` (wskazówka: `import sys; sys.argv`).

---

## Podsumowanie dnia 2

Po dzisiejszych zajęciach potrafisz:
- ✅ powtarzać instrukcje pętlami i sterować ich przebiegiem,
- ✅ korzystać z list, krotek, słowników i zbiorów,
- ✅ pisać funkcje i dzielić program na mniejsze części,
- ✅ testować własne funkcje za pomocą `assert`,
- ✅ dobierać dane testowe metodą klas równoważności i wartości brzegowych,
- ✅ obsługiwać i zgłaszać wyjątki,
- ✅ czytać i zapisywać pliki TXT, CSV i JSON.

### Co dalej?
Dzień 3: **programowanie obiektowe**, organizacja kodu i biblioteki zewnętrzne, **biblioteka standardowa**, frameworki testowe **unittest** i **pytest** oraz praktyczne zastosowania Pythona w pracy testera.

### Zadanie domowe

1. **Generator danych testowych:** funkcja `generuj_uzytkownikow(n)` zwraca listę `n` słowników z polami `email` (`user1@test.pl`…), `haslo` (losowe, 10 znaków, co najmniej jedna cyfra), `wiek` (losowy 18–80). Zapisz wynik do CSV. Napisz testy sprawdzające, że każdy e-mail jest unikalny, a każde hasło spełnia wymagania.
2. **Porównywarka plików JSON:** funkcja `porownaj(oczekiwany, rzeczywisty)` przyjmuje dwa słowniki i zwraca słownik z kluczami `brakujace`, `nadmiarowe` i `rozne` (klucze, których wartości się różnią). Przetestuj ją.
3. **Analizator logów (dla chętnych):** dla pliku logów wypisz liczbę błędów na każdą minutę oraz najczęstszy komunikat błędu.

---

## Rozwiązania wybranych ćwiczeń

<details>
<summary>Rozgrzewka 1.1</summary>

```
est
ER
2        ← len = 6, 6 % 4 = 2
3.33
ok
```
</details>

<details>
<summary>Ćwiczenie 1.3</summary>

```python
HASLO = "tajne123"
for proba in range(3):
    if input("Hasło: ") == HASLO:
        print("Zalogowano")
        break
    print(f"Błędne hasło. Pozostało prób: {2 - proba}")
else:
    print("Konto zablokowane")
```
</details>

<details>
<summary>Ćwiczenie 2.3</summary>

```python
dane = ["TC-1", "TC-2", "TC-2", "TC-3", "TC-1"]
unikalne = []
for x in dane:
    if x not in unikalne:
        unikalne.append(x)
print(unikalne)                  # ['TC-1', 'TC-2', 'TC-3']
# alternatywa: list(dict.fromkeys(dane))
```
</details>

<details>
<summary>Ćwiczenie 2.4</summary>

```python
wyniki = [("TC-1", 120), ("TC-2", 890), ("TC-3", 340)]
najwolniejszy = wyniki[0]
for test in wyniki:
    if test[1] > najwolniejszy[1]:
        najwolniejszy = test
print(najwolniejszy)
```
</details>

<details>
<summary>Ćwiczenie 3.1</summary>

```python
wyniki = [("TC-1", "PASS"), ("TC-2", "FAIL"), ("TC-3", "PASS"),
          ("TC-4", "FAIL"), ("TC-5", "SKIP")]
licznik = {}
for _, status in wyniki:
    licznik[status] = licznik.get(status, 0) + 1
niezaliczone = [tc for tc, status in wyniki if status == "FAIL"]
print(licznik, niezaliczone)
```
</details>

<details>
<summary>Ćwiczenie 3.2</summary>

```python
v1 = {"login", "rejestracja", "koszyk", "płatność"}
v2 = {"login", "koszyk", "płatność", "czat", "wishlist"}
print("Usunięte:", v1 - v2)
print("Nowe:", v2 - v1)
print("Do testów regresyjnych:", v1 & v2)
```
</details>

<details>
<summary>Ćwiczenie 3.3</summary>

```python
a = [x for x in range(1, 101) if x % 7 == 0]
zdanie = "tester znajduje błędy zanim zrobi to klient"
b = {s: len(s) for s in zdanie.split()}
c = [f"user{i}@test.pl" for i in range(1, 6)]
```
</details>

<details>
<summary>Ćwiczenia 4.3 i 5.3</summary>

```python
def pass_rate(wyniki):
    zaliczone = wyniki.count("PASS")
    wykonane = zaliczone + wyniki.count("FAIL")
    if wykonane == 0:
        return 0.0
    return round(zaliczone / wykonane * 100, 2)


def test_pass_rate_typowy():
    assert pass_rate(["PASS", "FAIL", "PASS", "SKIP"]) == 66.67


def test_pass_rate_pusta_lista():
    assert pass_rate([]) == 0.0


def test_pass_rate_same_skip():
    assert pass_rate(["SKIP", "SKIP"]) == 0.0


def test_pass_rate_same_pass():
    assert pass_rate(["PASS", "PASS"]) == 100.0
```
</details>

<details>
<summary>Ćwiczenie 5.1</summary>

```python
def ocena(punkty):
    if punkty >= 90:
        return 5.0
    if punkty >= 80:
        return 4.5
    if punkty >= 70:
        return 4.0
    if punkty >= 60:
        return 3.5
    if punkty >= 50:
        return 3.0
    return 2.0


def test_ocena_wartosci_brzegowe():
    przypadki = [
        (0, 2.0), (49, 2.0), (50, 3.0), (59, 3.0), (60, 3.5), (69, 3.5),
        (70, 4.0), (79, 4.0), (80, 4.5), (89, 4.5), (90, 5.0), (100, 5.0),
    ]
    for punkty, oczekiwana in przypadki:
        assert ocena(punkty) == oczekiwana, f"punkty={punkty}"
```
</details>

<details>
<summary>Ćwiczenie 5.2</summary>

```python
def czy_przestepny(rok):
    return (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0


def test_czy_przestepny():
    assert czy_przestepny(2024) is True     # podzielny przez 4
    assert czy_przestepny(2023) is False    # niepodzielny przez 4
    assert czy_przestepny(1900) is False    # podzielny przez 100, nie przez 400
    assert czy_przestepny(2000) is True     # podzielny przez 400
```
</details>

<details>
<summary>Ćwiczenie 5.4 – znalezione błędy</summary>

```python
def test_haslo_dokladnie_8_znakow():
    assert czy_haslo_poprawne("abcdefg1") is True     # ❌ wykrywa błąd: > zamiast >=


def test_haslo_bez_cyfry():
    assert czy_haslo_poprawne("abcdefghij") is False  # ✅


def test_haslo_cyfra_na_poczatku():
    assert czy_haslo_poprawne("1abcdefgh") is True    # ✅


def test_haslo_za_krotkie():
    assert czy_haslo_poprawne("abc1") is False        # ✅
```

Błąd jest jeden, ale ukryty na granicy: warunek `len(haslo) > 8` odrzuca hasła mające **dokładnie 8 znaków**. Wykrywa go tylko test wartości brzegowej. Poprawka: `len(haslo) >= 8`.
</details>

<details>
<summary>Ćwiczenie 6.2</summary>

```python
def pass_rate(wyniki):
    for status in wyniki:
        if status not in ("PASS", "FAIL", "SKIP"):
            raise ValueError(f"Nieznany status: {status!r}")
    zaliczone = wyniki.count("PASS")
    wykonane = zaliczone + wyniki.count("FAIL")
    return round(zaliczone / wykonane * 100, 2) if wykonane else 0.0


def test_pass_rate_nieznany_status():
    try:
        pass_rate(["PASS", "OK"])
    except ValueError:
        pass
    else:
        assert False, "Oczekiwano ValueError"
```
</details>

<details>
<summary>Ćwiczenie 7.1</summary>

```python
licznik = {}
with open("aplikacja.log", encoding="utf-8") as plik:
    for linia in plik:
        poziom = linia.split()[2]
        licznik[poziom] = licznik.get(poziom, 0) + 1
print(licznik)          # {'INFO': 3, 'WARNING': 1, 'ERROR': 2}
```
</details>

<details>
<summary>Ćwiczenie 7.2</summary>

```python
import csv
import json

with open("uzytkownicy.csv", encoding="utf-8", newline="") as plik:
    dane = list(csv.DictReader(plik))

with open("uzytkownicy.json", "w", encoding="utf-8") as plik:
    json.dump(dane, plik, indent=2, ensure_ascii=False)
```
</details>

<details>
<summary>Ćwiczenie 7.3</summary>

```python
import json

DOMYSLNA = {"srodowisko": "test", "timeout_s": 5}


def wczytaj_konfiguracje(sciezka):
    try:
        with open(sciezka, encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return DOMYSLNA.copy()
```
</details>
