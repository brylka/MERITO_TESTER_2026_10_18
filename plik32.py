from plik31 import suma, roznica, iloczyn, iloraz

def test_suma():
    assert suma(2, 3) == 5

def test_suma_ujemne():
    assert suma(-2,-5) == -7

def test_suma_ulamki():
    assert suma(0.1, 0.2) == 0.3

def test_suma_dwie_takie_same_dodatnie():
    assert suma(1000,1000) == 2000

def test_iloraz():
    assert iloraz(10, 4) == 2.5

def test_iloraz_przez_zero():
    try:
        iloraz(10, 0)
    except ZeroDivisionError:
        pass
    else:
        assert False, "Oczekiwano ZeroDivisionError"


if __name__ == "__main__":
    test_suma()
    test_suma_ujemne()
    test_suma_ulamki()
    test_suma_dwie_takie_same_dodatnie()
    test_iloraz()
    test_iloraz_przez_zero()
    #print(suma(0.1,0.2))