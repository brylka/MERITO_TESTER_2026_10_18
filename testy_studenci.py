

from studenci import Student, BazaStudentow

def test_odpowiedzi_obiektu():
    assert str(Student('1234', 'Bartosz', 'Bryniarski', 'Tester')) == '1234 | Bartosz Bryniarski | Tester'

if __name__ == "__main__":
    test_odpowiedzi_obiektu()