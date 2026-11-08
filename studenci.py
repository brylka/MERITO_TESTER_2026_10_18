class Student:
    def __init__(self, nr_albumu, imie, nazwisko, kierunek):
        self.nr_albumu = nr_albumu
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek
    def __str__(self):
        return f"{self.nr_albumu} | {self.imie} {self.nazwisko} | {self.kierunek}"
    def set_imie(self, nowe_imie):
        self.imie = nowe_imie


if __name__ == "__main__":
    bartosz = Student(1234, "Bartosz", "Bryniarski", "Tester")
    anna = Student(1235, "Anna", "Nowak", "Python")
    print(bartosz)
    print(anna)
    bartosz.set_imie("Paweł")
    bartosz.nr_albumu = 1235
    print(bartosz)