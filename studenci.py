class Student:
    def __init__(self, nr_albumu, imie, nazwisko, kierunek):
        self.nr_albumu = nr_albumu
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek
    def __str__(self):
        return f"{self.nr_albumu} | {self.imie} {self.nazwisko} | {self.kierunek}"

class BazaStudentow:
    def __init__(self):
        self.studenci = []
    def znajdz(self, nr_albumu):
        for student in self.studenci:
            if student.nr_albumu == nr_albumu:
                return student
        return None
    def dodaj(self, student):
        if self.znajdz(student.nr_albumu) is not None:
            return False
        self.studenci.append(student)
        return True


if __name__ == "__main__":
    baza = BazaStudentow()
    baza.dodaj(Student(1234, "Bartosz", "Bryniarski", "Tester"))
    baza.dodaj(Student(1235, "Anna", "Nowak", "Python"))
    baza.dodaj(Student(1235, "Tomasz", "Kowalski", "Tester"))
    for stident in baza.studenci:
        print(stident)
    # print(bartosz)
    # print(anna)


