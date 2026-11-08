from studenci import Student, BazaStudentow
import os

PLIK_TESTOWY = "testowy.csv"

def dodaj_bartosza():
    return Student('1234', 'Bartosz', 'Bryniarski', 'Tester')

def test_odpowiedzi_obiektu():
    assert str(dodaj_bartosza()) == '1234 | Bartosz Bryniarski | Tester'

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

if __name__ == "__main__":
    test_odpowiedzi_obiektu()
    test_nowa_pusta_baza_studentow()
    test_dodania_studenta()
    test_nie_mozna_dodac_studenta_z_istniejacym_nr_albumu()