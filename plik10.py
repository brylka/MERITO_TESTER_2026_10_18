d = int(input("Podaj numer dnia tygodnia (1-7): "))

# if d == 1 or d == 2 or d == 3 or d == 4 or d == 5:
# #if d >= 1 and d <= 6:
#     print("Dzień roboczy")
# elif d == 6 or d == 7:
#     print("Weekend")
# else:
#     print("Nieprawidłowy numer")

match d:
    case 1 | 2 | 3 | 4 | 5:
        print("Dzień roboczy")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Nieprawidłowy numer")

