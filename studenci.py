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
    def dodaj(self, student):
        self.studenci.append(student)
        return True


if __name__ == "__main__":
    baza = BazaStudentow()
    baza.dodaj(Student(1234, "Bartosz", "Bryniarski", "Tester"))
    baza.dodaj(Student(1235, "Anna", "Nowak", "Python"))
    baza.dodaj(Student(2345, "Tomasz", "Kowalski", "Tester"))
    for stident in baza.studenci:
        print(stident)
    # print(bartosz)
    # print(anna)


