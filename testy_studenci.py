from studenci import Student, BazaStudentow
import os

PLIK_TESTOWY = "testowy.csv"

def test_odpowiedzi_obiektu():
    assert str(Student('1234', 'Bartosz', 'Bryniarski', 'Tester')) == '1234 | Bartosz Bryniarski | Tester'

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
    assert baza.dodaj(Student('1234', 'Bartosz', 'Bryniarski', 'Tester')) is True
    assert len(baza.studenci) == 1


if __name__ == "__main__":
    test_odpowiedzi_obiektu()
    test_nowa_pusta_baza_studentow()
    test_dodania_studenta()