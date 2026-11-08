# Tester oprogramowania – Konwencje kodu

**Od przykładów edukacyjnych do kodu „jak w projekcie”**

| | |
|---|---|
| **Uczelnia** | Uniwersytet WSB Merito we Wrocławiu |
| **Kierunek** | Studia podyplomowe: Tester oprogramowania |
| **Moduł** | Tester jako developer narzędzi z pomocą Pythona |
| **Opracował** | Bartosz Bryniarski |
| **Charakter** | Materiał uzupełniający – zamknięcie bloku Python |

---

## 1. Dlaczego do tej pory pisaliśmy po polsku?

W materiałach z dni 1–3 stosowaliśmy prostą zasadę:

> **Co należy do Pythona – jest po angielsku. Co jest nasze – jest po polsku.**

```python
def oblicz_rabat(cena, procent):          # nasze: oblicz_rabat, cena, procent
    if procent < 0:                       # Pythona: def, if, return, raise
        raise ValueError("Ujemny rabat")  # Pythona: ValueError
    return round(cena * procent / 100, 2) # Pythona: round
```

Dzięki temu od razu było widać, które słowa **trzeba znać na pamięć** (słowa kluczowe, funkcje wbudowane, biblioteki), a które **wymyśliliśmy sami** i mogłyby brzmieć zupełnie inaczej. Dla osoby, która dopiero zaczyna programować, to ogromne ułatwienie.

**W prawdziwych projektach tak się jednak nie robi.** Od kolejnych zajęć wszystkie przykłady i materiały (TDD, Git, BDD) będą pisane po angielsku.

### Dlaczego kod pisze się po angielsku?

- **Zespoły są międzynarodowe** – kod musi przeczytać kolega z Indii, Brazylii czy Niemiec.
- **Spójność** – Python, biblioteki i dokumentacja są po angielsku; mieszanka `koszyk.add_item()` czyta się źle.
- **Wyszukiwanie pomocy** – błąd z `cart_total` łatwiej znaleźć w sieci niż z `wartosc_koszyka`.
- **Polskie znaki** – `wartość = 10` technicznie działa w Pythonie 3, ale potrafi sprawić problemy w narzędziach, terminalach i przy przenoszeniu plików. W nazwach **nigdy** nie używamy polskich znaków.
- **Rynek pracy** – na rozmowie rekrutacyjnej i w zadaniu domowym oczekuje się kodu po angielsku.

### Co może zostać po polsku?

| Element | Język |
|---|---|
| nazwy zmiennych, funkcji, klas, plików | 🇬🇧 zawsze angielski |
| komentarze i docstringi | 🇬🇧 zwykle angielski (polski tylko w zespole w 100% polskim i gdy taka jest umowa) |
| komunikaty Git (commit message) | 🇬🇧 angielski |
| teksty widoczne dla użytkownika aplikacji | język użytkownika – np. polski |
| dane testowe (`"Jan Kowalski"`, `"Wrocław"`) | dowolny – często celowo polskie, by sprawdzić obsługę znaków `ąęłóśżź` |
| zgłoszenia błędów, dokumentacja testów | zgodnie z ustaleniami zespołu/klienta |

---

## 2. Ten sam kod – przed i po

**Wersja edukacyjna (dni 1–3):**
```python
class Koszyk:
    PROG_DARMOWEJ_DOSTAWY = 200.0

    def __init__(self):
        self._pozycje = {}

    def dodaj(self, produkt, ilosc=1):
        if ilosc <= 0:
            raise ValueError("Ilość musi być dodatnia")
        ...

    def czy_pusty(self):
        return not self._pozycje


def test_ponowne_dodanie_zwieksza_ilosc(koszyk, chleb):
    koszyk.dodaj(chleb, 2)
    koszyk.dodaj(chleb, 3)
    assert koszyk.ilosc("chleb") == 5
```

**Wersja „projektowa” (od kolejnych zajęć):**
```python
class ShoppingCart:
    FREE_SHIPPING_THRESHOLD = 200.0

    def __init__(self):
        self._items = {}

    def add(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        ...

    def is_empty(self):
        return not self._items


def test_adding_same_product_twice_increases_quantity(cart, bread):
    cart.add(bread, 2)
    cart.add(bread, 3)
    assert cart.quantity("bread") == 5
```

Logika jest **identyczna** – zmieniły się tylko nazwy, które wymyśliliśmy sami.

---

## 3. Słowniczek – nazwy z naszych materiałów

| Po polsku (materiały) | Po angielsku (projekty) |
|---|---|
| `wynik`, `wyniki` | `result`, `results` |
| `oczekiwany`, `rzeczywisty` | `expected`, `actual` |
| `dane_testowe` | `test_data` |
| `przypadek_testowy` | `test_case` |
| `zaliczone`, `niezaliczone`, `pominiete` | `passed`, `failed`, `skipped` |
| `czas_ms` | `duration_ms` |
| `uzytkownik`, `haslo` | `user`, `password` |
| `zaloguj`, `wyloguj` | `log_in` / `login`, `log_out` / `logout` |
| `koszyk`, `produkt`, `cena`, `ilosc` | `cart`, `product`, `price`, `quantity` |
| `wartosc`, `suma`, `rabat` | `value` / `total`, `sum`, `discount` |
| `dostawa`, `do_zaplaty` | `shipping`, `amount_due` |
| `dodaj`, `usun`, `zmien` | `add`, `remove`, `update` |
| `wczytaj`, `zapisz` | `load` / `read`, `save` / `write` |
| `sprawdz`, `czy_poprawny` | `check` / `validate`, `is_valid` |
| `oblicz`, `wygeneruj` | `calculate`, `generate` |
| `pobierz`, `wyslij` | `get` / `fetch`, `send` |
| `licznik`, `lista`, `slownik` | `counter`, `list` → konkretnie: `users`, `prices` |
| `sciezka`, `plik`, `katalog` | `path`, `file`, `directory` |
| `raport`, `podsumowanie` | `report`, `summary` |
| `strona_logowania` | `login_page` |
| `blad`, `ostrzezenie` | `error`, `warning` |
| `konfiguracja`, `srodowisko` | `config`, `environment` |

---

## 4. Konwencje nazewnictwa (PEP 8)

| Element | Styl | Przykład |
|---|---|---|
| zmienna, funkcja, metoda | `snake_case` | `user_email`, `calculate_total()` |
| klasa, wyjątek | `PascalCase` | `ShoppingCart`, `InvalidDiscountCode` |
| stała | `UPPER_SNAKE_CASE` | `MAX_RETRIES = 3`, `BASE_URL` |
| moduł (plik), pakiet (katalog) | krótko, `snake_case` | `cart.py`, `test_utils/` |
| atrybut „wewnętrzny” | `_` na początku | `self._items` |
| nazwa zajęta przez Pythona | `_` na końcu | `class_`, `type_`, `id_` |
| metody specjalne | `__nazwa__` | `__init__`, `__eq__` – tylko te z Pythona, nie wymyślamy własnych |
| zmienna nieużywana | `_` | `for _ in range(3):` |

### Dobre nazwy – zasady

- **Funkcja = czasownik** (co robi): `calculate_total()`, `load_users()`, `send_request()`.
- **Klasa = rzeczownik** (czym jest): `User`, `LoginPage`, `TestReport`.
- **Wartość logiczna = pytanie**: `is_empty`, `has_discount`, `can_checkout`, `should_retry`.
- **Kolekcja = liczba mnoga**: `users`, `prices`; element w pętli – liczba pojedyncza: `for user in users:`.
- **Jednostki w nazwie**, gdy nie są oczywiste: `timeout_s`, `duration_ms`, `price_pln`.
- **Bez skrótów i jednoliterowych nazw** (poza `i`, `x` w krótkich pętlach): `usr_lst` ❌ → `users` ✅.
- **Bez nazw „wytrychów”**: `data`, `temp`, `obj`, `stuff`, `x2` – nic nie mówią.
- **Nie zasłaniaj nazw wbudowanych**: `list = [...]`, `id = 5`, `input = "..."` psują działanie `list()`, `id()`, `input()`.

```python
# ❌
def proc(d, f=True):
    l = []
    for x in d:
        if x["s"] == "F" or not f:
            l.append(x)
    return l

# ✅
def filter_failed_results(results, only_failed=True):
    selected = []
    for result in results:
        if result["status"] == "FAIL" or not only_failed:
            selected.append(result)
    return selected
```

---

## 5. Konwencje w testach

### 5.1. Pliki, funkcje i klasy testowe

```
project/
├── src/ lub nazwa_pakietu/
│   └── cart.py
└── tests/
    ├── conftest.py              ← wspólne fixtures
    ├── test_cart.py             ← test_<nazwa testowanego modułu>.py
    └── test_api_users.py
```

- pliki: `test_*.py`, funkcje: `test_*`, klasy: `Test*` – inaczej pytest ich **nie znajdzie**,
- jeden plik testowy na jeden moduł/obszar aplikacji,
- fixtures nazywamy **rzeczownikiem** – tym, co zwracają: `cart`, `logged_in_user`, `api_client`.

### 5.2. Nazwa testu opisuje zachowanie

Nazwa testu ma być na tyle dokładna, żeby **po samej nazwie w raporcie** było wiadomo, co się zepsuło.

| ❌ | ✅ |
|---|---|
| `test_cart` | `test_new_cart_is_empty` |
| `test_discount2` | `test_unknown_discount_code_raises_error` |
| `test_shipping` | `test_shipping_is_free_from_200_pln` |
| `test_login_1` | `test_login_fails_with_wrong_password` |

Popularne schematy:
```
def test_<co>_<kiedy>_<oczekiwany_wynik>():          # test_withdraw_more_than_balance_raises_error
def test_should_<oczekiwany_wynik>_when_<kiedy>():   # test_should_raise_error_when_balance_too_low
def test_given_<stan>_when_<akcja>_then_<wynik>():   # styl BDD – wrócimy do niego
```

Wybierz **jeden** schemat i trzymaj się go w całym projekcie.

### 5.3. Budowa testu – AAA

```python
def test_discount_code_reduces_amount_due(cart, laptop):
    # Arrange
    cart.add(laptop)

    # Act
    cart.apply_discount_code("STUDENT10")

    # Assert
    assert cart.amount_due() == pytest.approx(900.00)
```

Pusta linia między sekcjami wystarczy – komentarze `# Arrange` są opcjonalne.

### 5.4. Dobre praktyki testów

- **Jeden test – jedno zachowanie.** Kilka `assert` jest w porządku, jeśli sprawdzają tę samą rzecz.
- **Testy są niezależne** – kolejność uruchomienia nie może mieć znaczenia; nie współdziel stanu między testami.
- **Nazwane wartości zamiast „magicznych liczb”** – `FREE_SHIPPING_THRESHOLD` zamiast `200` rozrzuconego po kodzie.
- **Komunikat w asercji**, gdy wynik nie mówi sam za siebie: `assert response.status_code == 200, response.text`.
- **Bez logiki w testach** – `if` i pętle w teście to sygnał, że warto użyć `parametrize`.
- **Bez `time.sleep()`** tam, gdzie można poczekać na konkretne zdarzenie.
- **Bez sekretów w kodzie** – hasła i tokeny ze zmiennych środowiskowych.

---

## 6. Styl i formatowanie

### 6.1. Najważniejsze zasady PEP 8

- wcięcia: 4 spacje,
- długość linii: 79–120 znaków (zgodnie z ustaleniem w projekcie),
- dwie puste linie przed definicją funkcji/klasy najwyższego poziomu, jedna – między metodami,
- spacje wokół operatorów: `total = price * quantity`,
- bez spacji przy argumentach nazwanych: `round(value, ndigits=2)`,
- porównanie z `None` przez `is`: `if result is None:`,
- sprawdzanie pustej kolekcji przez truthy/falsy: `if not users:` zamiast `if len(users) == 0:`.

### 6.2. Kolejność importów

```python
# 1. biblioteka standardowa
import json
from pathlib import Path

# 2. biblioteki zewnętrzne
import pytest
import requests

# 3. nasze moduły
from shop.cart import ShoppingCart
```

Grupy oddzielone pustą linią, w każdej grupie alfabetycznie. Bez `from modul import *`.

### 6.3. Narzędzia, które pilnują stylu za nas

| Narzędzie | Do czego |
|---|---|
| **Ruff** | linter i formatter – wykrywa błędy i niezgodności z PEP 8, poprawia automatycznie |
| **Black** | formatter – „jeden słuszny” wygląd kodu, koniec dyskusji o spacjach |
| **mypy** | sprawdza adnotacje typów |
| PyCharm **Ctrl + Alt + L** | formatowanie wbudowane |
| PyCharm **Ctrl + Alt + O** | porządkowanie importów |

```bash
pip install ruff
ruff check .          # znajdź problemy
ruff check . --fix    # popraw, co się da
ruff format .         # sformatuj kod
```

> W zespole o stylu nie decyduje gust, tylko **konfiguracja narzędzia** zapisana w repozytorium. Kod sformatowany automatycznie nie wywołuje dyskusji w code review.

---

## 7. Dokumentowanie kodu

### 7.1. Komentarze – „dlaczego”, nie „co”

```python
# ❌ opisuje to, co widać w kodzie
retries = 3  # set retries to 3

# ✅ wyjaśnia decyzję
retries = 3  # payment sandbox is flaky – usually succeeds by the 2nd attempt
```

Zakomentowanego kodu nie zostawiamy „na wszelki wypadek” – od tego jest Git.

Przydatne znaczniki (PyCharm zbiera je w zakładce *TODO*):
```python
# TODO: add test for negative quantity
# FIXME: fails on Windows – path separator
```

### 7.2. Docstringi i adnotacje typów

```python
def calculate_pass_rate(results: list[str]) -> float:
    """Return the percentage of passed tests among executed ones.

    Skipped tests are not counted as executed.

    Args:
        results: Test statuses: "PASS", "FAIL" or "SKIP".

    Returns:
        Pass rate in percent, rounded to 2 decimal places;
        0.0 when no tests were executed.

    Raises:
        ValueError: If an unknown status is found.
    """
```

Docstring piszemy dla modułów, klas i funkcji publicznych (tych, których używa ktoś inny). W testach zwykle wystarcza dobra nazwa.

---

## 8. Zapowiedź: konwencje w Git

Na zajęciach z Gita poznamy szczegóły – już teraz warto znać zasadę: komunikat commita po angielsku, w trybie rozkazującym, krótko.

```
Add tests for free shipping threshold
Fix discount code case sensitivity
Refactor cart total calculation
```

Popularny standard *Conventional Commits*:
```
test: add boundary tests for shipping threshold
fix: accept lowercase discount codes
feat: add MERITO20 discount code
```

---

## 9. Ćwiczenia

### Ćwiczenie 1
Przetłumacz na „wersję projektową” (nazwy po angielsku, PEP 8, dobre nazwy) funkcję `pass_rate()` z dnia 2 wraz z jej testami.

### Ćwiczenie 2
Popraw nazwy w poniższym kodzie. Co jest nie tak z każdą z nich?
```python
MaxCzas = 5
def Sprawdz(l, id):
    list = []
    for e in l:
        if e["t"] > MaxCzas:
            list.append(e)
    return list
```

### Ćwiczenie 3
Zaproponuj lepsze nazwy testów:
`test_1`, `test_cart_ok`, `test_login_error`, `test_api`, `test_discount_works`.

### Ćwiczenie 4
Zainstaluj `ruff`, uruchom `ruff check .` na projekcie koszyka z dnia 3 i popraw zgłoszone problemy.

### Ćwiczenie 5 (dla chętnych)
Przepisz cały projekt koszyka z dnia 3 na angielski: `shop/product.py`, `shop/cart.py`, `tests/test_cart.py`. Uruchom testy – wynik musi być taki sam jak przed zmianą.

---

## Podsumowanie

- ✅ W materiałach edukacyjnych: **słowa Pythona po angielsku, nasze nazwy po polsku** – żeby odróżnić jedno od drugiego.
- ✅ W prawdziwych projektach i **od kolejnych zajęć: wszystkie nazwy po angielsku**, bez polskich znaków.
- ✅ Polski zostaje w tekstach dla użytkownika i w danych testowych.
- ✅ `snake_case` dla funkcji i zmiennych, `PascalCase` dla klas, `UPPER_CASE` dla stałych.
- ✅ Nazwa testu opisuje zachowanie; test ma budowę AAA i jest niezależny.
- ✅ Styl pilnują narzędzia (Ruff, Black), a nie dyskusje.

---

## Rozwiązania

<details>
<summary>Ćwiczenie 1</summary>

```python
import pytest

VALID_STATUSES = ("PASS", "FAIL", "SKIP")


def calculate_pass_rate(results: list[str]) -> float:
    """Return the percentage of passed tests among executed ones."""
    for status in results:
        if status not in VALID_STATUSES:
            raise ValueError(f"Unknown status: {status!r}")
    passed = results.count("PASS")
    executed = passed + results.count("FAIL")
    return round(passed / executed * 100, 2) if executed else 0.0


def test_pass_rate_ignores_skipped_tests():
    assert calculate_pass_rate(["PASS", "FAIL", "PASS", "SKIP"]) == 66.67


def test_pass_rate_is_zero_when_nothing_executed():
    assert calculate_pass_rate(["SKIP", "SKIP"]) == 0.0


def test_pass_rate_raises_error_for_unknown_status():
    with pytest.raises(ValueError, match="Unknown status"):
        calculate_pass_rate(["PASS", "OK"])
```
</details>

<details>
<summary>Ćwiczenie 2</summary>

```python
MAX_DURATION_MS = 5          # stała → UPPER_SNAKE_CASE, jednostka w nazwie


def find_slow_tests(results):           # funkcja → snake_case, czasownik; bez nieużywanego "id"
    slow_tests = []                     # nie zasłaniamy wbudowanego "list"
    for result in results:              # "l" i "e" nic nie mówią ("l" myli się z "1")
        if result["duration_ms"] > MAX_DURATION_MS:   # "t" → pełna nazwa klucza
            slow_tests.append(result)
    return slow_tests
```

Problemy: `MaxCzas` (styl klasy zamiast stałej, polski, brak jednostki), `Sprawdz` (PascalCase dla funkcji, nazwa nie mówi, co sprawdza), `l` i `e` (nieczytelne), `id` i `list` (zasłaniają funkcje wbudowane, `id` dodatkowo nieużywane), `"t"` (skrót).
</details>

<details>
<summary>Ćwiczenie 3</summary>

| Było | Propozycja |
|---|---|
| `test_1` | `test_new_cart_is_empty` |
| `test_cart_ok` | `test_cart_total_is_sum_of_item_prices` |
| `test_login_error` | `test_login_fails_with_wrong_password` |
| `test_api` | `test_get_user_returns_200_and_email` |
| `test_discount_works` | `test_student10_code_reduces_total_by_10_percent` |
</details>
