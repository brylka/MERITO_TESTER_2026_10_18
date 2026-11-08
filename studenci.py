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
    def edytuj(self, nr_albumu, nowe_imie, nowe_nazwisko, nowy_kierunek):
        student = self.znajdz(nr_albumu)
        if student is None:
            return False
        student.imie = nowe_imie
        student.nazwisko = nowe_nazwisko
        student.kierunek = nowy_kierunek
        return True
    def usun(self, nr_albumu):
        student = self.znajdz(nr_albumu)
        if student is None:
            return False
        self.studenci.remove(student)
        return True

def pokaz_menu():
    print("\n=== OBSŁUGA STUDENTÓW ===")
    print("1. Lista studentów")
    print("2. Dodaj studenta")
    print("3. Znajdź studenta")
    print("4. Edytuj studenta")
    print("5. Usuń studenta")
    print("6. Wyjdź z programu")

if __name__ == "__main__":
    baza = BazaStudentow()
    while True:
        pokaz_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            if not baza.studenci:
                print("Brak studentów")
            else:
                print("Lista studentów:")
                for student in baza.studenci:
                    print(student)
        elif wybor == "2":
            print("Dodaj studenta:")
            nr_albumu = input("Nr albumu: ")
            imie = input("Imię: ")
            nazwisko = input("Nazwisko: ")
            kierunek = input("Kierunek: ")
            if baza.dodaj(Student(nr_albumu, imie, nazwisko, kierunek)):
                print("Dodano studenta.")
            else:
                print("Student o taki numerze albumu istnieje.")
        elif wybor == "3":
            nr_albumu = input("Nr albumu: ")
            student = baza.znajdz(nr_albumu)
            if student:
                print(student)
            else:
                print("Student nie istnieje.")
        elif wybor == "4":
            nr_albumu = input("Nr albumu: ")
            student = baza.znajdz(nr_albumu)
            if student is None:
                print("Student nie istnieje.")
            else:
                print(student)
                nowe_imie = input("Podaj nowe imię: ")
                nowe_nazwisko = input("Podaj nowe nazwisko: ")
                nowy_kierunek = input("Podaj nowy kierunek: ")
                baza.edytuj(nr_albumu, nowe_imie, nowe_nazwisko, nowy_kierunek)
                print("Zapisano zmiany.")
        elif wybor == "6":
            print("Dziękuję za używanie programu!")
            break
        else:
            print("Nieznana opcja! Wybierz istniejącą.")



