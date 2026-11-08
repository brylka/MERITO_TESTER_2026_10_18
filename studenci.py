class Student:
    def __init__(self, nr_albumu, imie, nazwisko, kierunek):
        self.nr_albumu = nr_albumu
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek


if __name__ == "__main__":
    bartosz = Student(1234, "Bartosz", "Bryniarski", "Tester")
    print(f"Obiekt imię: {bartosz.imie} nazwisko: {bartosz.nazwisko} nr: {bartosz.nr_albumu}")
    anna = Student(1235, "Anna", "Nowak", "Python")
    print(f"Obiekt imię: {anna.imie} nazwisko: {anna.nazwisko} nr: {anna.nr_albumu}")