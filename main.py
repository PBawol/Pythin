imie = str(input("Podaj imię: "))

if imie[0].islower() or imie[0].isdigit():
    print("Niepoprawne imie!!!")
else:
    if not imie[0:].isalpha():
        print("Niepoprawne imie!!!")
    else:
        nazwisko = str(input("Podaj nazwisko: "))
        if nazwisko[0].islower() or nazwisko[0].isdigit():
            print("Niepoprawne nazwisko!!!")
        else:
            if not imie[0:].isalpha():
                print("Niepoprawne imie!!!")
            else:
                numer = str(input("Podaj numer telefonu: "))
                if numer.isdigit():
                    print(imie)
                    print(nazwisko)
                    print(numer[:9])
                else:
                    print("Niepoprawny numer!!!")