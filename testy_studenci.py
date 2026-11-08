from studenci import Student, BazaStudentow
import os

PLIK_TESTOWY = "testowy.csv"

def dodaj_bartosza():
    return Student('1234', 'Bartosz', 'Bryniarski', 'Tester')

def test_odpowiedzi_obiektu():
    assert str(dodaj_bartosza()) == '1234 | Bartosz Bryniarski | Tester'

def test_mozna_stworzyc_studenta_z_pustym_imieniem():
    try:
        Student("5555", "", "Nowak", "Tester")
    except ValueError:
        pass
    else:
        assert False, f"Oczekiwano ValueError"

def nowa_baza():
    if os.path.exists(PLIK_TESTOWY):
        os.remove(PLIK_TESTOWY)
    return BazaStudentow(PLIK_TESTOWY)

def test_nowa_pusta_baza_studentow():
    baza = nowa_baza()
    assert baza.studenci == []

def test_dodania_studenta():
    baza = nowa_baza()
    assert baza.studenci == []
    assert baza.dodaj(dodaj_bartosza()) is True
    assert len(baza.studenci) == 1

def test_nie_mozna_dodac_studenta_z_istniejacym_nr_albumu():
    baza = nowa_baza()
    baza.dodaj(dodaj_bartosza())
    assert baza.dodaj(Student('1234', 'Anna', 'Nowak', 'Programista')) is False
    assert len(baza.studenci) == 1

def test_znajdz_nieistniejacego_studenta():
    baza = nowa_baza()
    assert baza.znajdz("99999") is None

def test_znajdz_istniejacego_studenta():
    baza = nowa_baza()
    # baza.dodaj(dodaj_bartosza())
    # assert str(baza.znajdz("1234")) == '1234 | Bartosz Bryniarski | Tester'
    bartosz = dodaj_bartosza()
    baza.dodaj(bartosz)
    assert baza.znajdz("1234") is bartosz


if __name__ == "__main__":
    test_odpowiedzi_obiektu()
    test_mozna_stworzyc_studenta_z_pustym_imieniem()
    test_nowa_pusta_baza_studentow()
    test_dodania_studenta()
    test_nie_mozna_dodac_studenta_z_istniejacym_nr_albumu()
    test_znajdz_nieistniejacego_studenta()
    test_znajdz_istniejacego_studenta()