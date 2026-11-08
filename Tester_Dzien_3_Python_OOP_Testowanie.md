# Tester oprogramowania – Dzień 3

**Programowanie obiektowe, biblioteki i automatyzacja testów w Pythonie**

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
| 1 | Programowanie obiektowe – klasy i obiekty | Klasa, obiekt, `__init__`, `self`, atrybuty, metody, `__str__`, `__eq__` |
| 2 | Programowanie obiektowe – cd. | Enkapsulacja, `@property`, dziedziczenie, `super()`, polimorfizm, `@dataclass`, Page Object |
| 3 | Organizacja kodu i biblioteki zewnętrzne | Moduły, pakiety, `import`, struktura projektu, venv, `pip`, `requirements.txt` |
| 4 | Biblioteka standardowa w pracy testera | `datetime`, `random`, `re`, `logging`, `collections`, `time`, `os`, `uuid` |
| 5 | Testowanie z `unittest` i debugowanie | `TestCase`, asercje, `setUp`/`tearDown`, debugowanie testów w PyCharm |
| 6 | Testowanie z `pytest` | `assert`, fixtures, `parametrize`, `raises`, `approx`, markery, raporty |
| 7 | Zastosowania Pythona w testowaniu | Testy API z `requests`, mockowanie, Faker, Selenium/Playwright |
| 8 | Projekt | Koszyk sklepowy: specyfikacja → testy → zgłoszenia błędów |

---

## 1. Programowanie obiektowe – klasy i obiekty

### Cele
- zrozumieć, czym jest klasa i obiekt,
- tworzyć własne klasy z atrybutami i metodami,
- sterować tym, jak obiekt się wyświetla i porównuje.

### 1.1. Po co obiekty?

W dniu 2 dane i funkcje były **osobno**: słownik z koszykiem i funkcje, które dostawały go jako argument. Programowanie obiektowe łączy je w jedną całość:

| Proceduralnie | Obiektowo |
|---|---|
| `koszyk = {"pozycje": []}` | `koszyk = Koszyk()` |
| `dodaj_produkt(koszyk, "chleb")` | `koszyk.dodaj("chleb")` |
| `wartosc_koszyka(koszyk)` | `koszyk.wartosc()` |

**Dlaczego tester musi znać obiektowość?**
- wszystkie biblioteki testowe są obiektowe (`unittest.TestCase`, `requests.Response`, `webdriver.Chrome`…),
- wzorzec **Page Object Model** w automatyzacji UI to klasy,
- aplikacje, które testujesz, są zbudowane z obiektów.

### 1.2. Pojęcia

- **Klasa** – szablon, „przepis” (np. *Użytkownik*).
- **Obiekt (instancja)** – konkretny egzemplarz utworzony z klasy (np. *Anna, anna@test.pl*).
- **Atrybut** – dana przechowywana w obiekcie (`email`).
- **Metoda** – funkcja należąca do obiektu (`zaloguj()`).

Wszystko w Pythonie jest obiektem:
```python
tekst = "tester"
print(type(tekst))       # <class 'str'>
print(tekst.upper())     # upper() to metoda obiektu klasy str
```

### 1.3. Pierwsza klasa

```python
class Uzytkownik:
    def __init__(self, email, haslo):
        self.email = email            # atrybuty instancji
        self.haslo = haslo
        self.zalogowany = False

    def zaloguj(self, haslo):
        if haslo == self.haslo:
            self.zalogowany = True
        return self.zalogowany

    def wyloguj(self):
        self.zalogowany = False


anna = Uzytkownik("anna@test.pl", "Haslo123!")     # utworzenie obiektu
jan = Uzytkownik("jan@test.pl", "tajne")

print(anna.email)                 # anna@test.pl
print(anna.zaloguj("zle"))        # False
print(anna.zaloguj("Haslo123!"))  # True
print(jan.zalogowany)             # False – każdy obiekt ma własny stan
```

- `__init__` – **konstruktor**, wywoływany automatycznie przy tworzeniu obiektu,
- `self` – odwołanie do **tego konkretnego** obiektu; każda metoda dostaje go jako pierwszy parametr,
- nazwy klas piszemy w stylu `PascalCase`.

### 1.4. Atrybuty klasy a atrybuty instancji

```python
class Uzytkownik:
    MIN_DLUGOSC_HASLA = 8             # atrybut klasy – wspólny dla wszystkich
    licznik = 0

    def __init__(self, email, haslo):
        if len(haslo) < Uzytkownik.MIN_DLUGOSC_HASLA:
            raise ValueError("Hasło za krótkie")
        self.email = email
        self.haslo = haslo
        Uzytkownik.licznik += 1


Uzytkownik("a@test.pl", "Haslo123!")
Uzytkownik("b@test.pl", "Haslo456!")
print(Uzytkownik.licznik)             # 2
```

### 1.5. Metody specjalne: `__str__`, `__repr__`, `__eq__`

```python
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):                # dla użytkownika – print()
        return f"{self.nazwa} ({self.cena:.2f} zł)"

    def __repr__(self):               # dla programisty – debugger, listy
        return f"Produkt({self.nazwa!r}, {self.cena!r})"

    def __eq__(self, other):          # porównanie ==
        return (self.nazwa, self.cena) == (other.nazwa, other.cena)


chleb = Produkt("chleb", 4.5)
print(chleb)                          # chleb (4.50 zł)
print([chleb])                        # [Produkt('chleb', 4.5)]
print(chleb == Produkt("chleb", 4.5)) # True
```

> **Dlaczego `__eq__` jest ważne dla testera?** Bez niego `assert wynik == Produkt("chleb", 4.5)` zawsze się wywali – Python porównuje wtedy, czy to **ten sam obiekt w pamięci**, a nie czy ma te same dane.

### Ćwiczenie 1.1
Napisz klasę `KontoBankowe` z atrybutami `wlasciciel` i `saldo` (domyślnie 0) oraz metodami `wplac(kwota)` i `wyplac(kwota)`. Wypłata większa niż saldo oraz kwoty niedodatnie mają zgłaszać `ValueError`. Dodaj `__str__`.

### Ćwiczenie 1.2
Napisz testy (`assert`) do `KontoBankowe`: wpłata, wypłata, wypłata całego salda (wartość brzegowa!), wypłata o 1 grosz za dużo, kwota ujemna.

### Ćwiczenie 1.3
Napisz klasę `PrzypadekTestowy` z atrybutami `id`, `tytul`, `kroki` (lista) i `status` (domyślnie `"NIE_URUCHOMIONY"`) oraz metodami `dodaj_krok(opis)`, `oznacz(status)` (dopuszczalne: PASS, FAIL, SKIP – inne → `ValueError`) i `__str__`.

---

## 2. Programowanie obiektowe – cd.

### Cele
- chronić dane obiektu przed niepoprawnymi wartościami,
- budować hierarchie klas (dziedziczenie),
- korzystać z `@dataclass`,
- poznać ideę wzorca Page Object.

### 2.1. Enkapsulacja i `@property`

Python nie ma „prywatnych” pól jak Java. Stosujemy **konwencję**: atrybut zaczynający się od `_` jest wewnętrzny – „nie ruszaj z zewnątrz”.

`@property` pozwala kontrolować odczyt i zapis atrybutu:

```python
class KontoBankowe:
    def __init__(self, wlasciciel):
        self.wlasciciel = wlasciciel
        self._saldo = 0.0

    @property
    def saldo(self):                  # odczyt: konto.saldo
        return self._saldo

    def wplac(self, kwota):
        if kwota <= 0:
            raise ValueError("Kwota musi być dodatnia")
        self._saldo += kwota


konto = KontoBankowe("Anna")
konto.wplac(100)
print(konto.saldo)                    # 100.0
# konto.saldo = 1_000_000             # AttributeError – nie da się „dopisać” pieniędzy
```

Właściwość z walidacją przy zapisie:
```python
class Uzytkownik:
    def __init__(self, email):
        self.email = email            # przechodzi przez setter poniżej!

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, wartosc):
        if "@" not in wartosc:
            raise ValueError(f"Niepoprawny e-mail: {wartosc!r}")
        self._email = wartosc.lower()


u = Uzytkownik("Anna@Test.PL")
print(u.email)                        # anna@test.pl
# u.email = "zly-adres"               # ValueError
```

### 2.2. Dziedziczenie

Klasa potomna **przejmuje** atrybuty i metody klasy bazowej i może je rozszerzać lub nadpisywać.

```python
class Uzytkownik:
    def __init__(self, email):
        self.email = email

    def uprawnienia(self):
        return {"czytanie"}

    def __str__(self):
        return f"{self.__class__.__name__}: {self.email}"


class Administrator(Uzytkownik):              # dziedziczy po Uzytkownik
    def __init__(self, email, poziom=1):
        super().__init__(email)               # wywołanie konstruktora klasy bazowej
        self.poziom = poziom

    def uprawnienia(self):                    # nadpisanie metody
        return super().uprawnienia() | {"edycja", "usuwanie"}


admin = Administrator("root@test.pl", poziom=2)
print(admin)                          # Administrator: root@test.pl
print(admin.uprawnienia())            # {'czytanie', 'edycja', 'usuwanie'}
print(isinstance(admin, Uzytkownik))  # True – admin JEST użytkownikiem
```

### 2.3. Polimorfizm

Różne obiekty, ta sama metoda – każdy zachowuje się „po swojemu”:

```python
class RaportTekstowy:
    def generuj(self, wyniki):
        return "\n".join(f"{k}: {v}" for k, v in wyniki.items())


class RaportCSV:
    def generuj(self, wyniki):
        return "status,liczba\n" + "\n".join(f"{k},{v}" for k, v in wyniki.items())


wyniki = {"PASS": 5, "FAIL": 2}
for raport in [RaportTekstowy(), RaportCSV()]:
    print(raport.generuj(wyniki))      # ten sam kod – różny wynik
    print("---")
```

### 2.4. `@dataclass` – klasy na dane bez pisania szablonu

Większość klas „na dane” wymaga tego samego: `__init__`, `__repr__`, `__eq__`. Dekorator `@dataclass` generuje je automatycznie:

```python
from dataclasses import dataclass, field


@dataclass
class WynikTestu:
    id: str
    status: str
    czas_ms: int = 0
    tagi: list = field(default_factory=list)   # mutowalna wartość domyślna – tak!

    def __post_init__(self):                   # walidacja po utworzeniu
        if self.status not in ("PASS", "FAIL", "SKIP"):
            raise ValueError(f"Nieznany status: {self.status}")


w = WynikTestu("TC-1", "PASS", 120)
print(w)                                       # WynikTestu(id='TC-1', status='PASS', czas_ms=120, tagi=[])
print(w == WynikTestu("TC-1", "PASS", 120))    # True – __eq__ za darmo
```

> `@dataclass(frozen=True)` tworzy obiekty **niezmienne** – idealne do danych testowych, których nikt nie powinien przypadkiem zmodyfikować.

### 2.5. Klasy abstrakcyjne (krótko)

```python
from abc import ABC, abstractmethod


class Raport(ABC):
    @abstractmethod
    def generuj(self, wyniki):
        """Każdy raport MUSI implementować tę metodę."""


# Raport()   # TypeError – nie można utworzyć obiektu klasy abstrakcyjnej
```

### 2.6. Zapowiedź: wzorzec Page Object Model

W automatyzacji testów UI każdą stronę aplikacji opisujemy **klasą**. Test nie wie nic o selektorach HTML – korzysta z czytelnych metod:

```python
class StronaBazowa:
    def __init__(self, przegladarka):
        self.przegladarka = przegladarka

    def tytul(self):
        return self.przegladarka.title


class StronaLogowania(StronaBazowa):
    URL = "https://sklep.example.com/login"

    def otworz(self):
        self.przegladarka.get(self.URL)
        return self

    def zaloguj(self, email, haslo):
        self.przegladarka.find_element("id", "email").send_keys(email)
        self.przegladarka.find_element("id", "haslo").send_keys(haslo)
        self.przegladarka.find_element("id", "zaloguj").click()


# W teście:
# strona = StronaLogowania(driver).otworz()
# strona.zaloguj("anna@test.pl", "Haslo123!")
```

Gdy zmieni się wygląd strony, poprawiamy **jedną klasę**, a nie sto testów. To czysta obiektowość: enkapsulacja + dziedziczenie.

### Ćwiczenie 2.1
Przerób `KontoBankowe` z ćw. 1.1 tak, aby `saldo` było tylko do odczytu (`@property`).

### Ćwiczenie 2.2
Napisz klasę `KontoOszczednosciowe(KontoBankowe)` z atrybutem `oprocentowanie` i metodą `nalicz_odsetki()`. Wypłata z konta oszczędnościowego jest dozwolona tylko raz w miesiącu – druga wypłata zgłasza `ValueError` (licznik wypłat w atrybucie).

### Ćwiczenie 2.3
Zapisz `PrzypadekTestowy` z ćw. 1.3 jako `@dataclass`. Porównaj długość kodu.

---

## 3. Organizacja kodu i biblioteki zewnętrzne

### Cele
- dzielić kod na moduły i pakiety,
- poprawnie importować,
- instalować biblioteki i zapisywać zależności projektu.

### 3.1. Moduły

**Moduł** to po prostu plik `.py`. Plik `generatory.py`:
```python
"""Generatory danych testowych."""
import random

DOMENA = "test.pl"


def email(numer):
    return f"user{numer}@{DOMENA}"


def haslo(dlugosc=10):
    znaki = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(random.choice(znaki) for _ in range(dlugosc))
```

Użycie w innym pliku (w tym samym katalogu):
```python
import generatory
print(generatory.email(1))

from generatory import email, haslo
print(email(2), haslo())

import generatory as gen               # alias
print(gen.DOMENA)

# from generatory import *             # NIE – nie wiadomo, co trafia do przestrzeni nazw
```

### 3.2. `if __name__ == "__main__":` – raz jeszcze

```python
# generatory.py
def email(numer):
    return f"user{numer}@test.pl"


if __name__ == "__main__":
    # wykona się przy: python generatory.py
    # NIE wykona się przy: import generatory
    print(email(1))
```

Przy uruchomieniu pliku `__name__` ma wartość `"__main__"`, przy imporcie – nazwę modułu (`"generatory"`).

### 3.3. Pakiety

**Pakiet** to katalog z modułami i (zwyczajowo) plikiem `__init__.py`:

```
narzedzia_qa/
├── __init__.py
├── generatory.py
└── raporty.py
```

```python
from narzedzia_qa.generatory import email
from narzedzia_qa import raporty
```

### 3.4. Typowa struktura projektu testowego

```
projekt_sklep/
├── sklep/                 ← kod testowanej aplikacji / narzędzia
│   ├── __init__.py
│   ├── produkt.py
│   └── koszyk.py
├── tests/                 ← testy
│   ├── conftest.py
│   └── test_koszyk.py
├── .venv/                 ← środowisko wirtualne (nie trafia do repozytorium)
├── pytest.ini             ← konfiguracja pytest
├── requirements.txt       ← lista zależności
└── README.md
```

### 3.5. Instalacja zewnętrznych bibliotek – `pip`

**PyPI** (<https://pypi.org>) to repozytorium setek tysięcy bibliotek. Instalujemy je narzędziem `pip` – **zawsze w aktywnym środowisku wirtualnym** projektu (dzień 1).

```bash
pip install pytest                 # instalacja
pip install requests==2.32.3       # konkretna wersja
pip install --upgrade pytest       # aktualizacja
pip uninstall requests             # usunięcie
pip list                           # zainstalowane pakiety
pip show pytest                    # informacje o pakiecie
```

W PyCharm: *Settings → Project → Python Interpreter → „+”* albo terminal w PyCharm (venv jest w nim aktywny automatycznie).

### 3.6. `requirements.txt` – powtarzalne środowisko

Każdy członek zespołu i serwer CI musi mieć **te same wersje** bibliotek – inaczej testy mogą zachowywać się różnie.

```bash
pip freeze > requirements.txt      # zapisz zainstalowane wersje
pip install -r requirements.txt    # odtwórz środowisko na innym komputerze
```

Przykładowy `requirements.txt`:
```
pytest==8.3.3
pytest-html==4.1.1
requests==2.32.3
Faker==30.8.2
```

### 3.7. Biblioteki, które tester powinien znać

| Biblioteka | Zastosowanie |
|---|---|
| `pytest` | framework testowy (de facto standard) |
| `pytest-html`, `allure-pytest` | raporty z testów |
| `pytest-cov` | pokrycie kodu testami |
| `requests` | testy API (HTTP) |
| `selenium`, `playwright` | automatyzacja przeglądarki (testy UI) |
| `Faker` | generowanie realistycznych danych testowych |
| `behave`, `pytest-bdd` | BDD – Gherkin (osobne zajęcia) |
| `locust` | testy wydajnościowe |
| `jsonschema` | walidacja struktury odpowiedzi JSON |

### Ćwiczenie 3.1
Utwórz pakiet `narzedzia_qa` z modułami `generatory.py` (funkcje `email(n)`, `haslo(dlugosc)`) i `walidatory.py` (funkcje `czy_email(tekst)`, `czy_haslo_silne(tekst)`). W pliku `main.py` w katalogu nadrzędnym wygeneruj 5 użytkowników i sprawdź ich walidatorami.

### Ćwiczenie 3.2
Utwórz nowe środowisko wirtualne, zainstaluj `pytest` i `requests`, zapisz `requirements.txt`. Usuń folder `.venv`, utwórz go ponownie i odtwórz środowisko z pliku.

---

## 4. Biblioteka standardowa w pracy testera

### Cele
- poznać moduły biblioteki standardowej najczęściej używane w narzędziach testowych.

> „Baterie w zestawie” – wszystkie moduły z tego rozdziału są dostępne od razu, bez `pip install`.

### 4.1. `datetime` – daty i czas

```python
from datetime import datetime, date, timedelta

teraz = datetime.now()
print(teraz.strftime("%Y-%m-%d %H:%M:%S"))         # 2026-10-29 10:15:32
print(f"raport_{teraz:%Y%m%d_%H%M%S}.json")        # unikalna nazwa pliku raportu

jutro = date.today() + timedelta(days=1)
termin = datetime.strptime("31.12.2026", "%d.%m.%Y")  # napis → data
print((termin - teraz).days, "dni do terminu")
```

Przypadki brzegowe dat do testów: 29 lutego, 31 grudnia → 1 stycznia, zmiana czasu letni/zimowy.

### 4.2. `random` – losowe dane

```python
import random

random.seed(42)                       # ziarno → powtarzalna „losowość”!
print(random.randint(1, 100))
print(random.choice(["chrome", "firefox", "edge"]))
print(random.sample(range(1, 50), 6))   # 6 unikalnych liczb
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
```

> Testy z losowymi danymi bez ustawionego `seed` są **niepowtarzalne** – gdy test się wywali, nie da się odtworzyć błędu. Zapisuj użyte ziarno w logu!

### 4.3. `uuid` – unikalne identyfikatory

```python
import uuid

email = f"test_{uuid.uuid4().hex[:8]}@test.pl"
print(email)                          # np. test_3f9a1c2b@test.pl
```

Unikalny e-mail przy każdym uruchomieniu – rejestracja w teście nie zawiedzie na „użytkownik już istnieje”.

### 4.4. `re` – wyrażenia regularne

Wyrażenia regularne to „wzorce” do wyszukiwania i walidacji tekstu.

| Wzorzec | Znaczenie |
|---|---|
| `\d` | cyfra |
| `\w` | litera, cyfra lub `_` |
| `\s` | biały znak |
| `.` | dowolny znak |
| `+`, `*`, `?` | 1 lub więcej, 0 lub więcej, 0 lub 1 |
| `{3}`, `{2,4}` | dokładnie 3, od 2 do 4 |
| `[A-Z]` | znak z zakresu |
| `^`, `$` | początek, koniec |
| `( )` | grupa – fragment do wyciągnięcia |

```python
import re

# Walidacja
print(bool(re.fullmatch(r"\d{2}-\d{3}", "50-001")))          # kod pocztowy: True
print(bool(re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.]+", "anna@test.pl")))  # True

# Wyszukiwanie wszystkich wystąpień
tekst = "Zamówienia: ORD-1023, ORD-2048 oraz ORD-777"
print(re.findall(r"ORD-\d+", tekst))      # ['ORD-1023', 'ORD-2048', 'ORD-777']

# Rozbiór linii logu na części
linia = "2026-10-29 10:15:09 ERROR [platnosci] Timeout po 5000 ms"
wzorzec = r"(\S+) (\S+) (\w+) \[(\w+)\] (.*)"
m = re.match(wzorzec, linia)
if m:
    data, czas, poziom, modul, komunikat = m.groups()
    print(poziom, modul, komunikat)       # ERROR platnosci Timeout po 5000 ms
```

> Do testowania wyrażeń regularnych przydaje się <https://regex101.com> (wybierz *Python*).

### 4.5. `logging` – zamiast `print`

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    handlers=[logging.FileHandler("testy.log", encoding="utf-8"),
              logging.StreamHandler()],
)
log = logging.getLogger("testy")

log.debug("Szczegóły – nie pojawią się przy poziomie INFO")
log.info("Start testów na środowisku TEST")
log.warning("Wolna odpowiedź: 1200 ms")
log.error("Test TC-003 niezaliczony")
```

Przewaga nad `print`: poziomy ważności, znaczniki czasu, zapis do pliku, wyłączanie szczegółów bez zmiany kodu.

### 4.6. `collections.Counter`

```python
from collections import Counter

statusy = ["PASS", "FAIL", "PASS", "SKIP", "PASS", "FAIL"]
licznik = Counter(statusy)
print(licznik)                    # Counter({'PASS': 3, 'FAIL': 2, 'SKIP': 1})
print(licznik.most_common(1))     # [('PASS', 3)]
```

### 4.7. `time` – pomiar czasu

```python
import time

start = time.perf_counter()
sum(range(5_000_000))             # operacja, której czas mierzymy
czas = time.perf_counter() - start
print(f"Czas: {czas * 1000:.1f} ms")
assert czas < 2, "Operacja trwa za długo"

time.sleep(0.5)                   # czekanie – używaj rozważnie, spowalnia testy!
```

### 4.8. `os` i `sys` – środowisko

```python
import os
import sys

srodowisko = os.getenv("SRODOWISKO", "test")     # zmienna środowiskowa z wartością domyślną
print(f"Testy na środowisku: {srodowisko}")
print(sys.version)                                # wersja Pythona
print(sys.argv)                                   # argumenty uruchomienia skryptu
```

> Hasła i tokeny do środowisk testowych trzymaj w **zmiennych środowiskowych**, nigdy w kodzie, który trafia do repozytorium.

### Ćwiczenie 4.1
Napisz funkcję `parsuj_log(linia)` zwracającą słownik `{"data", "czas", "poziom", "modul", "komunikat"}` (użyj `re`) lub `None`, gdy linia nie pasuje do formatu. Napisz testy, w tym dla linii niepoprawnej.

### Ćwiczenie 4.2
Napisz funkcję `czy_kod_pocztowy(tekst)` i przetestuj ją na danych: `"50-001"`, `"50001"`, `"5-0001"`, `"ab-cde"`, `""`, `" 50-001"`.

### Ćwiczenie 4.3
Skonfiguruj `logging` tak, aby komunikaty `DEBUG` trafiały tylko do pliku, a od `INFO` w górę – także na ekran.

---

## 5. Testowanie z `unittest` i debugowanie

### Cele
- pisać testy z wbudowanym frameworkiem `unittest`,
- przygotowywać i sprzątać dane testowe,
- debugować testy w PyCharm.

### 5.1. Testowany kod – `kalkulator.py`

```python
class Kalkulator:
    def dodaj(self, a, b):
        return a + b

    def odejmij(self, a, b):
        return a - b

    def pomnoz(self, a, b):
        return a * b

    def podziel(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero")
        return a / b
```

### 5.2. Pierwsza klasa testowa – `test_kalkulator.py`

```python
import unittest

from kalkulator import Kalkulator


class TestKalkulator(unittest.TestCase):

    def setUp(self):
        """Wykonuje się PRZED każdym testem – świeży obiekt dla każdego testu."""
        self.kalk = Kalkulator()

    def tearDown(self):
        """Wykonuje się PO każdym teście – sprzątanie."""
        self.kalk = None

    def test_dodawanie(self):
        self.assertEqual(self.kalk.dodaj(2, 3), 5)

    def test_dodawanie_liczb_ujemnych(self):
        self.assertEqual(self.kalk.dodaj(-2, -3), -5)

    def test_dodawanie_ulamkow(self):
        # Pamiętacie dzień 1? Tu jest rozwiązanie problemu 0.1 + 0.2:
        self.assertAlmostEqual(self.kalk.dodaj(0.1, 0.2), 0.3)

    def test_dzielenie(self):
        self.assertEqual(self.kalk.podziel(10, 4), 2.5)

    def test_dzielenie_przez_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.kalk.podziel(1, 0)

    @unittest.skip("Funkcja potęgowania jeszcze nie istnieje")
    def test_potegowanie(self):
        pass


if __name__ == "__main__":
    unittest.main()
```

> `assertAlmostEqual` porównuje liczby z dokładnością do 7 miejsc po przecinku – i nasz pierwszy, „oblany” przypadek testowy z dnia 1 wreszcie przechodzi ✅. Kalkulator (aplikacja) nadal powinien wyświetlać użytkownikowi `0.3` – ale **test** nie może porównywać liczb zmiennoprzecinkowych operatorem `==`.

### 5.3. Najważniejsze asercje `unittest`

| Metoda | Sprawdza |
|---|---|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` / `assertFalse(x)` | `bool(x)` jest True / False |
| `assertIs(a, b)` / `assertIsNone(x)` | tożsamość / `x is None` |
| `assertIn(a, b)` / `assertNotIn(a, b)` | `a in b` |
| `assertIsInstance(obj, cls)` | `isinstance(obj, cls)` |
| `assertAlmostEqual(a, b)` | liczby prawie równe |
| `assertGreater(a, b)`, `assertLess(a, b)` | `a > b`, `a < b` |
| `assertRaises(Wyjatek)` | kod zgłasza wyjątek |
| `assertCountEqual(a, b)` | te same elementy, dowolna kolejność |

### 5.4. Uruchamianie testów

```bash
python -m unittest                         # wszystkie testy (pliki test*.py)
python -m unittest -v                      # z nazwami testów
python -m unittest test_kalkulator         # jeden moduł
python -m unittest test_kalkulator.TestKalkulator.test_dzielenie   # jeden test
```

Wynik:
```
test_dodawanie (test_kalkulator.TestKalkulator.test_dodawanie) ... ok
test_dodawanie_liczb_ujemnych (...) ... ok
test_dodawanie_ulamkow (...) ... ok
test_dzielenie (...) ... ok
test_dzielenie_przez_zero (...) ... ok
test_potegowanie (...) ... skipped 'Funkcja potęgowania jeszcze nie istnieje'

Ran 6 tests in 0.001s
OK (skipped=1)
```

W PyCharm: zielony trójkąt obok klasy lub metody testowej → *Run*. Wyniki pojawiają się w drzewku – zielone ✅ / czerwone ❌.

### 5.5. Jak czytać niezaliczony test?

Zmieńmy celowo oczekiwanie: `self.assertEqual(self.kalk.dodaj(2, 3), 6)`:

```
FAIL: test_dodawanie (test_kalkulator.TestKalkulator.test_dodawanie)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_kalkulator.py", line 15, in test_dodawanie
    self.assertEqual(self.kalk.dodaj(2, 3), 6)
AssertionError: 5 != 6
```

**FAIL** – asercja niespełniona (wynik inny niż oczekiwany). **ERROR** – test wywalił się wcześniej, nieoczekiwanym wyjątkiem (np. literówka w nazwie metody). To ważne rozróżnienie przy analizie wyników!

### 5.6. Debugowanie testów w PyCharm

1. Postaw breakpoint w linii testu (lub w testowanym kodzie).
2. Prawy klik na test → **Debug 'test_…'**.
3. Panel *Variables* pokazuje stan obiektów (`self.kalk`, argumenty, wyniki).
4. **F8** – następna linia, **F7** – wejdź do wywoływanej funkcji (*Step Into*), **Shift + F8** – wyjdź z funkcji.
5. **Evaluate Expression** (**Alt + F8**) – wykonaj dowolne wyrażenie w trakcie debugowania, np. `self.kalk.dodaj(0.1, 0.2)`.

> Gdy test się wywala i nie wiesz dlaczego – nie dopisuj `print`-ów na ślepo. Postaw breakpoint i **zobacz**.

### Ćwiczenie 5.1
Dodaj do `Kalkulator` metodę `potega(a, b)`, usuń `@skip` i napisz test. Dodaj też testy `odejmij` i `pomnoz` (w tym mnożenie przez 0).

### Ćwiczenie 5.2
Napisz klasę testową `unittest` dla `KontoBankowe` z ćw. 1.1. W `setUp` utwórz konto z saldem 100 zł.

### Ćwiczenie 5.3
Celowo zepsuj metodę `podziel` (np. `return a // b`). Uruchom testy, przeanalizuj komunikat, znajdź błąd debuggerem i napraw.

---

## 6. Testowanie z `pytest`

### Cele
- pisać zwięzłe testy w `pytest`,
- korzystać z fixtures i parametryzacji,
- uruchamiać wybrane testy i generować raporty.

### 6.1. Dlaczego pytest?

```bash
pip install pytest
```

Te same testy co w `unittest` – krócej:
```python
import pytest

from kalkulator import Kalkulator


def test_dodawanie():
    assert Kalkulator().dodaj(2, 3) == 5


def test_dzielenie_przez_zero():
    with pytest.raises(ZeroDivisionError):
        Kalkulator().podziel(1, 0)


def test_ulamki():
    assert Kalkulator().dodaj(0.1, 0.2) == pytest.approx(0.3)   # 0.1 + 0.2 ✅
```

- zwykłe funkcje i zwykły `assert` – bez klas i metod `assertXxx`,
- przy niezaliczonym teście pytest **pokazuje wartości** po obu stronach porównania,
- uruchamia też testy `unittest` i… nasze funkcje `test_` z dnia 2!

**Konwencje wykrywania testów:** pliki `test_*.py` lub `*_test.py`, funkcje `test_*`, klasy `Test*` (bez `__init__`).

### 6.2. Uruchamianie

```bash
pytest                          # wszystkie testy
pytest -v                       # szczegółowo
pytest test_kalkulator.py       # jeden plik
pytest -k "dziel"               # testy, których nazwa zawiera "dziel"
pytest -x                       # zatrzymaj po pierwszym błędzie
pytest --lf                     # uruchom tylko testy, które ostatnio nie przeszły
pytest -s                       # pokaż print() z testów
```

Czytelny komunikat błędu:
```
    def test_dodawanie():
>       assert Kalkulator().dodaj(2, 3) == 6
E       assert 5 == 6
E        +  where 5 = dodaj(2, 3)
```

W PyCharm: *Settings → Tools → Python Integrated Tools → Testing → Default test runner: **pytest***.

> Wróć do projektu z dnia 2 i uruchom `pytest test_raport.py -v` – pytest znajdzie i uruchomi napisane tam funkcje testowe bez żadnych zmian.

### 6.3. `pytest.raises` – szczegóły wyjątku

```python
def test_dzielenie_przez_zero_komunikat():
    with pytest.raises(ZeroDivisionError, match="przez zero"):
        Kalkulator().podziel(1, 0)
```

`match` sprawdza (wyrażeniem regularnym), czy komunikat wyjątku zawiera podany tekst.

### 6.4. Fixtures – przygotowanie danych testowych

**Fixture** to funkcja przygotowująca coś, czego test potrzebuje. Test dostaje ją, podając jej nazwę jako parametr:

```python
import pytest

from kalkulator import Kalkulator


@pytest.fixture
def kalk():
    return Kalkulator()


def test_dodawanie(kalk):          # pytest sam wywoła kalk() i przekaże wynik
    assert kalk.dodaj(2, 3) == 5


def test_odejmowanie(kalk):
    assert kalk.odejmij(2, 3) == -1
```

**Przygotowanie i sprzątanie (`yield`):**
```python
@pytest.fixture
def plik_z_danymi(tmp_path):                      # tmp_path – wbudowana fixture: katalog tymczasowy
    sciezka = tmp_path / "dane.csv"
    sciezka.write_text("id,status\nT1,PASS\n", encoding="utf-8")
    yield sciezka                                 # ← tu wykonuje się test
    print("Sprzątanie po teście")                 # ← to wykona się po teście


def test_odczyt_pliku(plik_z_danymi):
    assert "PASS" in plik_z_danymi.read_text(encoding="utf-8")
```

**Zasięg (scope)** – jak często fixture jest tworzona:

| `scope=` | Tworzona |
|---|---|
| `"function"` (domyślnie) | dla każdego testu osobno |
| `"module"` | raz na plik |
| `"session"` | raz na całe uruchomienie (np. połączenie z bazą, sesja HTTP) |

**`conftest.py`** – plik z fixtures **wspólnymi** dla wszystkich testów w katalogu. Nie trzeba go importować – pytest wczytuje go sam.

### 6.5. Parametryzacja – jeden test, wiele danych

Klasy równoważności i wartości brzegowe z dnia 2 – teraz w eleganckiej formie:

```python
import pytest


def rodzaj_biletu(wiek):
    if wiek < 0:
        raise ValueError("Wiek nie może być ujemny")
    if wiek < 18:
        return "ulgowy"
    if wiek < 65:
        return "normalny"
    return "senioralny"


@pytest.mark.parametrize("wiek, oczekiwany", [
    (0, "ulgowy"),
    (17, "ulgowy"),
    (18, "normalny"),
    (64, "normalny"),
    (65, "senioralny"),
])
def test_rodzaj_biletu(wiek, oczekiwany):
    assert rodzaj_biletu(wiek) == oczekiwany


@pytest.mark.parametrize("wiek", [-1, -100])
def test_rodzaj_biletu_ujemny_wiek(wiek):
    with pytest.raises(ValueError):
        rodzaj_biletu(wiek)
```

Każdy zestaw danych to **osobny test** w raporcie:
```
test_bilety.py::test_rodzaj_biletu[0-ulgowy] PASSED
test_bilety.py::test_rodzaj_biletu[17-ulgowy] PASSED
test_bilety.py::test_rodzaj_biletu[18-normalny] PASSED
...
```

Czytelne nazwy przypadków: `pytest.param(18, "normalny", id="granica-pelnoletnosci")`.

### 6.6. Markery – kategorie testów

```python
import sys

import pytest


@pytest.mark.smoke
def test_strona_glowna_dziala():
    assert True


@pytest.mark.skip(reason="Czeka na poprawkę błędu BUG-123")
def test_eksport_pdf():
    pass


@pytest.mark.skipif(sys.platform == "win32", reason="Tylko Linux/macOS")
def test_uprawnienia_plikow():
    pass


@pytest.mark.xfail(reason="Znany błąd BUG-456 – zaokrąglanie rabatu")
def test_rabat_zaokraglenie():
    assert round(2.675, 2) == 2.68       # 2.67 – znowu liczby zmiennoprzecinkowe!
```

- `skip` – nie uruchamiaj,
- `skipif` – nie uruchamiaj pod warunkiem,
- `xfail` – „spodziewamy się porażki” (znany błąd); gdy test nagle przejdzie – pytest to zgłosi (`XPASS`).

Własne markery rejestrujemy w `pytest.ini` i uruchamiamy wybiórczo:
```ini
[pytest]
testpaths = tests
pythonpath = .
addopts = -v
markers =
    smoke: szybkie testy dymne
    api: testy API (wymagają internetu)
```

```bash
pytest -m smoke              # tylko testy smoke
pytest -m "not api"          # wszystko oprócz API
```

### 6.7. Raporty

```bash
pip install pytest-html
pytest --html=raport.html --self-contained-html
```

Otwórz `raport.html` w przeglądarce – gotowy raport do załączenia w zgłoszeniu lub wysłania zespołowi.

Pokrycie kodu testami:
```bash
pip install pytest-cov
pytest --cov=sklep --cov-report=term-missing
```

### Ćwiczenie 6.1
Przepisz testy `Kalkulator` z rozdziału 5 na pytest z fixture `kalk`. Użyj `parametrize` dla dodawania (min. 5 zestawów, w tym liczby ujemne, zero i ułamki z `approx`).

### Ćwiczenie 6.2
Przepisz testy `ocena(punkty)` z dnia 2 (ćw. 5.1) na jeden test sparametryzowany. Dodaj czytelne `id` dla każdego przypadku.

### Ćwiczenie 6.3
Napisz fixture `konto`, która zwraca `KontoBankowe` z saldem 100 zł, i przenieś ją do `conftest.py`. Napisz 4 testy z niej korzystające.

---

## 7. Zastosowania Pythona w testowaniu

### Cele
- testować REST API z `requests`,
- izolować testy od zewnętrznych usług (mock),
- generować realistyczne dane testowe,
- zobaczyć, jak wygląda automatyzacja przeglądarki.

### 7.1. Testy API z `requests`

```bash
pip install requests
```

Ćwiczymy na darmowym testowym API <https://jsonplaceholder.typicode.com>.

```python
import requests

odp = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)
print(odp.status_code)            # 200
print(odp.headers["Content-Type"])
dane = odp.json()                 # JSON → słownik
print(dane["name"], dane["email"])
```

| Metoda HTTP | Znaczenie | `requests` |
|---|---|---|
| GET | pobierz | `requests.get(url)` |
| POST | utwórz | `requests.post(url, json=dane)` |
| PUT / PATCH | zmień | `requests.put(...)`, `requests.patch(...)` |
| DELETE | usuń | `requests.delete(url)` |

| Kod | Znaczenie |
|---|---|
| 200 / 201 / 204 | OK / utworzono / brak treści |
| 400 / 401 / 403 / 404 | złe żądanie / brak autoryzacji / brak dostępu / nie znaleziono |
| 500 | błąd serwera – zawsze zgłaszamy! |

> Zawsze podawaj `timeout` – bez niego test może „wisieć” w nieskończoność.

### 7.2. Testy API w pytest – `test_api.py`

```python
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api():
    sesja = requests.Session()
    sesja.headers.update({"Accept": "application/json"})
    yield sesja
    sesja.close()


@pytest.mark.api
def test_pobranie_uzytkownika(api):
    odp = api.get(f"{BASE_URL}/users/1", timeout=5)

    assert odp.status_code == 200
    dane = odp.json()
    assert dane["id"] == 1
    assert {"id", "name", "email", "address"} <= dane.keys()   # wymagane pola
    assert "@" in dane["email"]


@pytest.mark.api
def test_nieistniejacy_uzytkownik(api):
    odp = api.get(f"{BASE_URL}/users/9999", timeout=5)
    assert odp.status_code == 404


@pytest.mark.api
def test_utworzenie_posta(api):
    nowy = {"title": "Test z Pythona", "body": "Treść", "userId": 1}

    odp = api.post(f"{BASE_URL}/posts", json=nowy, timeout=5)

    assert odp.status_code == 201
    assert odp.json()["title"] == nowy["title"]
    assert "id" in odp.json()


@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_posty_uzytkownika(api, user_id):
    odp = api.get(f"{BASE_URL}/posts", params={"userId": user_id}, timeout=5)

    assert odp.status_code == 200
    assert all(post["userId"] == user_id for post in odp.json())


@pytest.mark.api
def test_czas_odpowiedzi(api):
    odp = api.get(f"{BASE_URL}/posts", timeout=5)
    assert odp.elapsed.total_seconds() < 2
```

### 7.3. Mockowanie – testy bez prawdziwego serwera

Testy jednostkowe nie powinny zależeć od internetu ani od tego, czy serwer akurat działa. **Mock** to „atrapa” obiektu, której zachowanie ustalamy sami.

Kod narzędzia – `klient_api.py`:
```python
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def nazwa_uzytkownika(user_id):
    odp = requests.get(f"{BASE_URL}/users/{user_id}", timeout=5)
    if odp.status_code == 404:
        return None
    return odp.json()["name"]
```

Test z atrapą – `test_klient_api.py`:
```python
from unittest.mock import Mock, patch

from klient_api import nazwa_uzytkownika, BASE_URL


def test_nazwa_uzytkownika():
    falszywa_odp = Mock(status_code=200)
    falszywa_odp.json.return_value = {"id": 1, "name": "Anna Testowa"}

    with patch("klient_api.requests.get", return_value=falszywa_odp) as mock_get:
        wynik = nazwa_uzytkownika(1)

    assert wynik == "Anna Testowa"
    mock_get.assert_called_once_with(f"{BASE_URL}/users/1", timeout=5)


def test_nazwa_uzytkownika_404():
    with patch("klient_api.requests.get", return_value=Mock(status_code=404)):
        assert nazwa_uzytkownika(9999) is None
```

Mock pozwala łatwo zasymulować sytuacje trudne do wywołania naprawdę: błąd 500, timeout, pustą odpowiedź.

### 7.4. Faker – realistyczne dane testowe

```bash
pip install Faker
```

```python
from faker import Faker

fake = Faker("pl_PL")
Faker.seed(123)                         # powtarzalność!

for _ in range(3):
    print(fake.name(), "|", fake.email(), "|", fake.phone_number())

print(fake.address())
print(fake.pesel())                     # poprawny formalnie PESEL
print(fake.iban())
print(fake.date_of_birth(minimum_age=18, maximum_age=90))
```

Fixture z danymi nowego użytkownika:
```python
import pytest
from faker import Faker


@pytest.fixture
def nowy_uzytkownik():
    fake = Faker("pl_PL")
    return {"imie": fake.first_name(), "nazwisko": fake.last_name(),
            "email": fake.unique.email(), "haslo": fake.password(length=12)}
```

### 7.5. Rzut oka na automatyzację przeglądarki

**Selenium** (`pip install selenium`):
```python
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_wyszukiwarka_python_org():
    driver = webdriver.Chrome()           # Selenium 4 sam pobierze sterownik
    try:
        driver.get("https://www.python.org")
        assert "Python" in driver.title
        pole = driver.find_element(By.NAME, "q")
        pole.send_keys("pytest")
        pole.submit()
        assert "pytest" in driver.page_source
    finally:
        driver.quit()
```

**Playwright** (`pip install pytest-playwright`, następnie `playwright install`):
```python
from playwright.sync_api import Page, expect


def test_wyszukiwarka_python_org(page: Page):      # fixture "page" z pluginu
    page.goto("https://www.python.org")
    expect(page).to_have_title("Welcome to Python.org")
    page.fill("input[name=q]", "pytest")
    page.press("input[name=q]", "Enter")
    expect(page.locator("body")).to_contain_text("pytest")
```

> Oba narzędzia to temat na osobny kurs. Ważne, że to **zwykły Python + pytest** – wszystko, czego nauczyliśmy się przez trzy dni, ma tu bezpośrednie zastosowanie (klasy → Page Object, fixtures → przeglądarka, parametrize → wiele przeglądarek).

### 7.6. Gdzie jeszcze Python pomaga testerowi?

- generowanie i czyszczenie danych w bazie (`sqlite3`, `psycopg`),
- porównywanie plików eksportu (CSV, JSON, XML),
- analiza logów i raportów z CI,
- testy wydajności (`locust`),
- skrypty wspierające testy manualne (np. przygotowanie 100 kont testowych).

### Ćwiczenie 7.1
Napisz testy API dla `https://jsonplaceholder.typicode.com/todos`: (a) lista ma 200 elementów, (b) każdy element ma pola `id`, `title`, `completed`, (c) `completed` jest typu `bool`, (d) zadanie o `id=1` ma `userId == 1`.

### Ćwiczenie 7.2
Dopisz do `klient_api.py` funkcję `liczba_postow(user_id)` i przetestuj ją z mockiem dla: 3 postów, 0 postów, odpowiedzi 500 (funkcja ma wtedy zgłosić `RuntimeError`).

### Ćwiczenie 7.3
Używając Fakera, wygeneruj plik `uzytkownicy.csv` z 50 użytkownikami (imię, nazwisko, e-mail, telefon, data urodzenia). Napisz test sprawdzający, że wszystkie e-maile są unikalne.

---

## 8. Projekt: Koszyk sklepowy – od specyfikacji do zgłoszenia błędu

### Scenariusz
Programista przekazał do testów moduł koszyka sklepu internetowego. Twoje zadanie jako testera-automatyka:
1. przeczytać specyfikację,
2. zaprojektować przypadki testowe (klasy równoważności, wartości brzegowe),
3. napisać testy w pytest,
4. uruchomić je i **zgłosić znalezione błędy**.

### 8.1. Specyfikacja (wymagania)

| ID | Wymaganie |
|---|---|
| R1 | Produkt ma nazwę (niepustą) i cenę (≥ 0). Niepoprawne dane → `ValueError`. |
| R2 | Do koszyka dodajemy produkt w ilości ≥ 1. Ilość 0 lub ujemna → `ValueError`. |
| R3 | Ponowne dodanie tego samego produktu **zwiększa** jego ilość. |
| R4 | Usunięcie produktu, którego nie ma w koszyku → `KeyError`. |
| R5 | Wartość koszyka = suma (cena × ilość). |
| R6 | Kody rabatowe: `STUDENT10` (−10%), `MERITO20` (−20%). Wielkość liter i spacje na brzegach nie mają znaczenia. Nieznany kod → `NieznanyKodRabatowy`. |
| R7 | Dostawa kosztuje 15 zł. Jest **darmowa**, gdy wartość koszyka **po rabacie** wynosi **co najmniej 200 zł**. Pusty koszyk – dostawa 0 zł. |
| R8 | Do zapłaty = wartość po rabacie + dostawa, zaokrąglone do 2 miejsc. |

### 8.2. Struktura projektu

```
projekt_sklep/
├── sklep/
│   ├── __init__.py          ← pusty plik
│   ├── produkt.py
│   └── koszyk.py
├── tests/
│   ├── conftest.py
│   └── test_koszyk.py
├── pytest.ini
└── requirements.txt         ← pytest, pytest-html
```

`pytest.ini`:
```ini
[pytest]
testpaths = tests
pythonpath = .
addopts = -v
```

### 8.3. Kod przekazany do testów

`sklep/produkt.py`:
```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Produkt:
    nazwa: str
    cena: float

    def __post_init__(self):
        if not self.nazwa:
            raise ValueError("Nazwa produktu nie może być pusta")
        if self.cena < 0:
            raise ValueError(f"Cena nie może być ujemna: {self.cena}")
```

`sklep/koszyk.py`:
```python
from sklep.produkt import Produkt


class NieznanyKodRabatowy(Exception):
    """Zgłaszany przy próbie użycia nieistniejącego kodu rabatowego."""


class Koszyk:
    KODY_RABATOWE = {"STUDENT10": 0.10, "MERITO20": 0.20}
    PROG_DARMOWEJ_DOSTAWY = 200.0
    KOSZT_DOSTAWY = 15.0

    def __init__(self):
        self._pozycje = {}            # nazwa produktu -> [Produkt, ilość]
        self._rabat = 0.0

    def dodaj(self, produkt: Produkt, ilosc: int = 1) -> None:
        if ilosc <= 0:
            raise ValueError("Ilość musi być dodatnia")
        self._pozycje[produkt.nazwa] = [produkt, ilosc]

    def usun(self, nazwa: str) -> None:
        if nazwa not in self._pozycje:
            raise KeyError(f"Brak produktu w koszyku: {nazwa}")
        del self._pozycje[nazwa]

    def ilosc(self, nazwa: str) -> int:
        if nazwa not in self._pozycje:
            return 0
        return self._pozycje[nazwa][1]

    @property
    def czy_pusty(self) -> bool:
        return not self._pozycje

    def wartosc(self) -> float:
        return round(sum(p.cena * il for p, il in self._pozycje.values()), 2)

    def zastosuj_kod(self, kod: str) -> None:
        if kod not in self.KODY_RABATOWE:
            raise NieznanyKodRabatowy(kod)
        self._rabat = self.KODY_RABATOWE[kod]

    def _wartosc_po_rabacie(self) -> float:
        return self.wartosc() * (1 - self._rabat)

    def dostawa(self) -> float:
        if self.czy_pusty:
            return 0.0
        if self._wartosc_po_rabacie() > self.PROG_DARMOWEJ_DOSTAWY:
            return 0.0
        return self.KOSZT_DOSTAWY

    def do_zaplaty(self) -> float:
        return round(self._wartosc_po_rabacie() + self.dostawa(), 2)
```

> W kodzie ukryto **trzy błędy** niezgodne ze specyfikacją. Nie szukaj ich czytając kod – znajdź je **testami**. Tak wygląda praca testera: kod często jest dla nas czarną skrzynką.

### 8.4. Zadania

1. Dla każdego wymagania R1–R8 wypisz przypadki testowe (tabela: ID wymagania, dane, oczekiwany wynik). Zaznacz wartości brzegowe.
2. W `tests/conftest.py` przygotuj fixtures: `koszyk` (pusty koszyk), `chleb`, `mleko`, `laptop` (produkty).
3. W `tests/test_koszyk.py` napisz testy. Użyj `parametrize` (kody rabatowe, próg dostawy) i `pytest.raises` (R1, R2, R4, R6).
4. Uruchom `pytest` i wygeneruj raport HTML.
5. Dla każdego niezaliczonego testu napisz **zgłoszenie błędu**: tytuł, kroki do odtworzenia, wynik oczekiwany, wynik rzeczywisty, wymaganie.
6. *(Dla chętnych)* Popraw kod, aż wszystkie testy przejdą.

Szablon zgłoszenia:
```
Tytuł:      [Koszyk] …
Wymaganie:  R?
Kroki:      1. …  2. …  3. …
Oczekiwane: …
Rzeczywiste: …
Test:       tests/test_koszyk.py::test_…
Priorytet:  …
```

### 8.5. Przykładowe rozwiązanie (dla prowadzącego)

<details>
<summary>tests/conftest.py</summary>

```python
import pytest

from sklep.koszyk import Koszyk
from sklep.produkt import Produkt


@pytest.fixture
def koszyk():
    return Koszyk()


@pytest.fixture
def chleb():
    return Produkt("chleb", 4.50)


@pytest.fixture
def mleko():
    return Produkt("mleko", 3.99)


@pytest.fixture
def laptop():
    return Produkt("laptop", 1000.00)
```
</details>

<details>
<summary>tests/test_koszyk.py</summary>

```python
import pytest

from sklep.koszyk import Koszyk, NieznanyKodRabatowy
from sklep.produkt import Produkt


# --- R1: produkt ---------------------------------------------------------

@pytest.mark.parametrize("nazwa, cena", [("", 10), ("chleb", -0.01)])
def test_produkt_niepoprawne_dane(nazwa, cena):
    with pytest.raises(ValueError):
        Produkt(nazwa, cena)


def test_produkt_cena_zero_dozwolona():
    assert Produkt("gratis", 0).cena == 0


# --- R2, R3: dodawanie -----------------------------------------------------

def test_nowy_koszyk_jest_pusty(koszyk):
    assert koszyk.czy_pusty
    assert koszyk.wartosc() == 0
    assert koszyk.do_zaplaty() == 0


def test_dodanie_produktu(koszyk, chleb):
    koszyk.dodaj(chleb, 2)
    assert not koszyk.czy_pusty
    assert koszyk.ilosc("chleb") == 2


def test_domyslna_ilosc_to_jeden(koszyk, chleb):
    koszyk.dodaj(chleb)
    assert koszyk.ilosc("chleb") == 1


@pytest.mark.parametrize("ilosc", [0, -1])
def test_niedodatnia_ilosc(koszyk, chleb, ilosc):
    with pytest.raises(ValueError):
        koszyk.dodaj(chleb, ilosc)


def test_ponowne_dodanie_zwieksza_ilosc(koszyk, chleb):
    koszyk.dodaj(chleb, 2)
    koszyk.dodaj(chleb, 3)
    assert koszyk.ilosc("chleb") == 5


# --- R4: usuwanie ----------------------------------------------------------

def test_usuniecie_produktu(koszyk, chleb):
    koszyk.dodaj(chleb)
    koszyk.usun("chleb")
    assert koszyk.czy_pusty


def test_usuniecie_nieistniejacego_produktu(koszyk):
    with pytest.raises(KeyError):
        koszyk.usun("kawior")


# --- R5: wartość -----------------------------------------------------------

def test_wartosc_koszyka(koszyk, chleb, mleko):
    koszyk.dodaj(chleb, 2)       # 9.00
    koszyk.dodaj(mleko, 3)       # 11.97
    assert koszyk.wartosc() == pytest.approx(20.97)


# --- R6: kody rabatowe -----------------------------------------------------

@pytest.mark.parametrize("kod, oczekiwana_kwota", [
    pytest.param("STUDENT10", 900.00, id="student10"),
    pytest.param("MERITO20", 800.00, id="merito20"),
    pytest.param("merito20", 800.00, id="male-litery"),
    pytest.param("  STUDENT10 ", 900.00, id="spacje"),
])
def test_kody_rabatowe(koszyk, laptop, kod, oczekiwana_kwota):
    koszyk.dodaj(laptop)
    koszyk.zastosuj_kod(kod)
    assert koszyk.do_zaplaty() == pytest.approx(oczekiwana_kwota)


def test_nieznany_kod_rabatowy(koszyk):
    with pytest.raises(NieznanyKodRabatowy):
        koszyk.zastosuj_kod("DARMOWO100")


# --- R7: dostawa -----------------------------------------------------------

def test_pusty_koszyk_bez_dostawy(koszyk):
    assert koszyk.dostawa() == 0


@pytest.mark.parametrize("cena, oczekiwana_dostawa", [
    pytest.param(199.99, 15.0, id="ponizej-progu"),
    pytest.param(200.00, 0.0, id="dokladnie-prog"),
    pytest.param(200.01, 0.0, id="powyzej-progu"),
])
def test_prog_darmowej_dostawy(koszyk, cena, oczekiwana_dostawa):
    koszyk.dodaj(Produkt("towar", cena))
    assert koszyk.dostawa() == oczekiwana_dostawa


def test_prog_dostawy_liczony_po_rabacie(koszyk):
    koszyk.dodaj(Produkt("towar", 220.00))
    koszyk.zastosuj_kod("STUDENT10")              # 198.00 < 200 → płatna dostawa
    assert koszyk.dostawa() == 15.0


# --- R8: do zapłaty --------------------------------------------------------

def test_do_zaplaty_z_dostawa(koszyk, chleb):
    koszyk.dodaj(chleb, 2)                        # 9.00 + 15.00
    assert koszyk.do_zaplaty() == pytest.approx(24.00)


def test_do_zaplaty_z_rabatem_i_dostawa(koszyk):
    koszyk.dodaj(Produkt("towar", 220.00))
    koszyk.zastosuj_kod("STUDENT10")              # 198.00 + 15.00
    assert koszyk.do_zaplaty() == pytest.approx(213.00)
```
</details>

<details>
<summary>Wynik na kodzie od programisty i znalezione błędy</summary>

```
FAILED tests/test_koszyk.py::test_ponowne_dodanie_zwieksza_ilosc - AssertionError: assert 3 == 5
FAILED tests/test_koszyk.py::test_kody_rabatowe[male-litery] - sklep.koszyk.NieznanyKodRabatowy: merito20
FAILED tests/test_koszyk.py::test_kody_rabatowe[spacje] - sklep.koszyk.NieznanyKodRabatowy:   STUDENT10
FAILED tests/test_koszyk.py::test_prog_darmowej_dostawy[dokladnie-prog] - assert 15.0 == 0.0
========================= 4 failed, 20 passed =========================
```

| Błąd | Wymaganie | Opis |
|---|---|---|
| 1 | R3 | Ponowne dodanie produktu **nadpisuje** ilość zamiast ją zwiększać (2 + 3 daje 3, a nie 5). |
| 2 | R6 | Kody rabatowe są wrażliwe na wielkość liter i spacje (`merito20`, `" STUDENT10 "` odrzucone). |
| 3 | R7 | Przy wartości **dokładnie 200 zł** naliczana jest dostawa (warunek `>` zamiast `>=`). Wykrył go tylko test wartości brzegowej! |

Przykładowe zgłoszenie:
```
Tytuł:      [Koszyk] Dostawa płatna przy wartości zamówienia dokładnie 200 zł
Wymaganie:  R7
Kroki:      1. Dodaj do pustego koszyka produkt o cenie 200,00 zł.
            2. Sprawdź koszt dostawy.
Oczekiwane: 0,00 zł (darmowa dostawa od 200 zł włącznie)
Rzeczywiste: 15,00 zł
Test:       tests/test_koszyk.py::test_prog_darmowej_dostawy[dokladnie-prog]
Priorytet:  wysoki – klient płaci więcej, niż obiecuje regulamin
```

Poprawki w `sklep/koszyk.py`:
```python
    def dodaj(self, produkt: Produkt, ilosc: int = 1) -> None:
        if ilosc <= 0:
            raise ValueError("Ilość musi być dodatnia")
        if produkt.nazwa in self._pozycje:
            self._pozycje[produkt.nazwa][1] += ilosc          # błąd 1
        else:
            self._pozycje[produkt.nazwa] = [produkt, ilosc]

    def zastosuj_kod(self, kod: str) -> None:
        kod = kod.strip().upper()                              # błąd 2
        if kod not in self.KODY_RABATOWE:
            raise NieznanyKodRabatowy(kod)
        self._rabat = self.KODY_RABATOWE[kod]

    def dostawa(self) -> float:
        if self.czy_pusty:
            return 0.0
        if self._wartosc_po_rabacie() >= self.PROG_DARMOWEJ_DOSTAWY:   # błąd 3
            return 0.0
        return self.KOSZT_DOSTAWY
```

Po poprawkach: `========================= 24 passed =========================`
</details>

### 8.6. Rozszerzenia dla chętnych

1. Dodaj do specyfikacji wymaganie R9: maksymalnie 10 sztuk jednego produktu w koszyku. Najpierw napisz testy (wartości 9, 10, 11), potem kod – to właśnie **TDD**.
2. Wczytuj produkty z pliku `produkty.json` w fixture o zasięgu `session`.
3. Wygeneruj 100 losowych koszyków (Faker + `random.seed`) i sprawdź, że `do_zaplaty()` nigdy nie jest ujemne i zawsze ma maksymalnie 2 miejsca po przecinku.
4. Zmierz pokrycie kodu: `pytest --cov=sklep --cov-report=term-missing`. Które linie nie są testowane?

---

## Podsumowanie dnia 3 i całego bloku Python

Po trzech dniach potrafisz:
- ✅ pisać programy w Pythonie: zmienne, warunki, pętle, kolekcje, funkcje,
- ✅ obsługiwać wyjątki i pracować z plikami TXT, CSV, JSON,
- ✅ projektować klasy, korzystać z dziedziczenia i `@dataclass`,
- ✅ organizować kod w moduły i pakiety, zarządzać bibliotekami przez `pip`,
- ✅ korzystać z biblioteki standardowej: `re`, `logging`, `datetime`, `random`…
- ✅ pisać testy w `unittest` i `pytest`: fixtures, parametryzacja, markery, raporty,
- ✅ testować API, używać mocków i generować dane testowe,
- ✅ projektować przypadki testowe metodą klas równoważności i wartości brzegowych – i automatyzować je.

### Zadanie domowe

1. **Biblioteka:** zaprojektuj klasy `Ksiazka` i `Biblioteka` (wypożycz, zwróć, limit 3 książek na czytelnika, kara za przetrzymanie: 0,50 zł/dzień, maks. 20 zł). Napisz specyfikację w formie tabeli wymagań, a potem testy w pytest z parametryzacją wartości brzegowych.
2. **Testy API:** dla `https://jsonplaceholder.typicode.com/comments` napisz min. 6 testów (pozytywne i negatywne), w tym jeden sparametryzowany i jeden z walidacją formatu e-maila wyrażeniem regularnym.
3. **Narzędzie (dla chętnych):** przerób generator raportu z dnia 2 na wersję obiektową (`WynikTestu` jako `@dataclass`, klasa `Raport` z metodami), dodaj `logging` i generowanie raportu HTML. Przenieś testy na pytest.

---

## Rozwiązania wybranych ćwiczeń

<details>
<summary>Ćwiczenia 1.1, 1.2 i 2.1</summary>

```python
class KontoBankowe:
    def __init__(self, wlasciciel, saldo=0.0):
        self.wlasciciel = wlasciciel
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def wplac(self, kwota):
        if kwota <= 0:
            raise ValueError("Kwota musi być dodatnia")
        self._saldo += kwota

    def wyplac(self, kwota):
        if kwota <= 0:
            raise ValueError("Kwota musi być dodatnia")
        if kwota > self._saldo:
            raise ValueError("Niewystarczające środki")
        self._saldo -= kwota

    def __str__(self):
        return f"Konto {self.wlasciciel}: {self._saldo:.2f} zł"


def test_wplata():
    konto = KontoBankowe("Anna")
    konto.wplac(100)
    assert konto.saldo == 100


def test_wyplata_calego_salda():
    konto = KontoBankowe("Anna", 100)
    konto.wyplac(100)
    assert konto.saldo == 0


def test_wyplata_o_grosz_za_duzo():
    konto = KontoBankowe("Anna", 100)
    try:
        konto.wyplac(100.01)
    except ValueError:
        pass
    else:
        assert False, "Oczekiwano ValueError"
    assert konto.saldo == 100          # saldo nie mogło się zmienić!
```
</details>

<details>
<summary>Ćwiczenie 1.3 / 2.3</summary>

```python
from dataclasses import dataclass, field

STATUSY = ("PASS", "FAIL", "SKIP")


@dataclass
class PrzypadekTestowy:
    id: str
    tytul: str
    kroki: list = field(default_factory=list)
    status: str = "NIE_URUCHOMIONY"

    def dodaj_krok(self, opis):
        self.kroki.append(opis)

    def oznacz(self, status):
        if status not in STATUSY:
            raise ValueError(f"Nieznany status: {status}")
        self.status = status

    def __str__(self):
        return f"[{self.status}] {self.id}: {self.tytul} ({len(self.kroki)} kroków)"
```
</details>

<details>
<summary>Ćwiczenie 2.2</summary>

```python
class KontoOszczednosciowe(KontoBankowe):
    def __init__(self, wlasciciel, saldo=0.0, oprocentowanie=0.05):
        super().__init__(wlasciciel, saldo)
        self.oprocentowanie = oprocentowanie
        self._wyplaty_w_miesiacu = 0

    def nalicz_odsetki(self):
        self._saldo += round(self._saldo * self.oprocentowanie / 12, 2)

    def wyplac(self, kwota):
        if self._wyplaty_w_miesiacu >= 1:
            raise ValueError("Limit wypłat w tym miesiącu wyczerpany")
        super().wyplac(kwota)
        self._wyplaty_w_miesiacu += 1
```
</details>

<details>
<summary>Ćwiczenie 4.1</summary>

```python
import re

WZORZEC_LOGU = re.compile(r"(\S+) (\S+) (\w+) \[(\w+)\] (.*)")


def parsuj_log(linia):
    m = WZORZEC_LOGU.fullmatch(linia.strip())
    if not m:
        return None
    klucze = ("data", "czas", "poziom", "modul", "komunikat")
    return dict(zip(klucze, m.groups()))


def test_parsuj_log_poprawna_linia():
    wynik = parsuj_log("2026-10-29 10:15:09 ERROR [platnosci] Timeout po 5000 ms")
    assert wynik["poziom"] == "ERROR"
    assert wynik["modul"] == "platnosci"
    assert wynik["komunikat"] == "Timeout po 5000 ms"


def test_parsuj_log_niepoprawna_linia():
    assert parsuj_log("to nie jest log") is None
```
</details>

<details>
<summary>Ćwiczenie 4.2</summary>

```python
import re

import pytest


def czy_kod_pocztowy(tekst):
    return re.fullmatch(r"\d{2}-\d{3}", tekst) is not None


@pytest.mark.parametrize("tekst, oczekiwany", [
    ("50-001", True), ("50001", False), ("5-0001", False),
    ("ab-cde", False), ("", False), (" 50-001", False),
])
def test_czy_kod_pocztowy(tekst, oczekiwany):
    assert czy_kod_pocztowy(tekst) == oczekiwany
```
</details>

<details>
<summary>Ćwiczenie 4.3</summary>

```python
import logging

log = logging.getLogger("testy")
log.setLevel(logging.DEBUG)

do_pliku = logging.FileHandler("testy.log", encoding="utf-8")
do_pliku.setLevel(logging.DEBUG)

na_ekran = logging.StreamHandler()
na_ekran.setLevel(logging.INFO)

format_ = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
do_pliku.setFormatter(format_)
na_ekran.setFormatter(format_)

log.addHandler(do_pliku)
log.addHandler(na_ekran)

log.debug("tylko w pliku")
log.info("w pliku i na ekranie")
```
</details>

<details>
<summary>Ćwiczenie 6.1</summary>

```python
import pytest

from kalkulator import Kalkulator


@pytest.fixture
def kalk():
    return Kalkulator()


@pytest.mark.parametrize("a, b, wynik", [
    (2, 3, 5), (-2, -3, -5), (-2, 3, 1), (0, 0, 0), (0.1, 0.2, 0.3),
])
def test_dodawanie(kalk, a, b, wynik):
    assert kalk.dodaj(a, b) == pytest.approx(wynik)


def test_mnozenie_przez_zero(kalk):
    assert kalk.pomnoz(123, 0) == 0


def test_dzielenie_przez_zero(kalk):
    with pytest.raises(ZeroDivisionError, match="przez zero"):
        kalk.podziel(1, 0)
```
</details>

<details>
<summary>Ćwiczenie 7.1</summary>

```python
import pytest
import requests

URL = "https://jsonplaceholder.typicode.com/todos"


@pytest.fixture(scope="module")
def todos():
    odp = requests.get(URL, timeout=5)
    assert odp.status_code == 200
    return odp.json()


def test_liczba_zadan(todos):
    assert len(todos) == 200


def test_wymagane_pola(todos):
    for t in todos:
        assert {"id", "title", "completed"} <= t.keys(), f"Zadanie {t.get('id')}"


def test_completed_jest_bool(todos):
    assert all(isinstance(t["completed"], bool) for t in todos)


def test_zadanie_1(todos):
    assert todos[0]["id"] == 1
    assert todos[0]["userId"] == 1
```
</details>

<details>
<summary>Ćwiczenie 7.2</summary>

```python
# klient_api.py
def liczba_postow(user_id):
    odp = requests.get(f"{BASE_URL}/posts", params={"userId": user_id}, timeout=5)
    if odp.status_code != 200:
        raise RuntimeError(f"Błąd API: {odp.status_code}")
    return len(odp.json())


# test_klient_api.py
from unittest.mock import Mock, patch

import pytest

from klient_api import liczba_postow


@pytest.mark.parametrize("posty, oczekiwana", [([{}, {}, {}], 3), ([], 0)])
def test_liczba_postow(posty, oczekiwana):
    odp = Mock(status_code=200)
    odp.json.return_value = posty
    with patch("klient_api.requests.get", return_value=odp):
        assert liczba_postow(1) == oczekiwana


def test_liczba_postow_blad_serwera():
    with patch("klient_api.requests.get", return_value=Mock(status_code=500)):
        with pytest.raises(RuntimeError, match="500"):
            liczba_postow(1)
```
</details>
