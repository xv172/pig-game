import random

def rzut_kostka():
    min_wartosc = 1
    max_wartosc = 6
    return random.randint(min_wartosc, max_wartosc)

while True:
    gracze = input("Podaj liczbę graczy (2 - 4): ")
    if gracze.isdigit():
        gracze = int(gracze)
        if 2 <= gracze <= 4:
            break
        else:
            print("Musi być między 2 a 4 graczy.")
    else:
        print("Nieprawidłowe, spróbuj ponownie.")

max_score = 10
wyniki_graczy = [0 for _ in range(gracze)]

game_over = False

while not game_over:
    for idx_gracza in range(gracze):
        print("\nTura gracza numer", idx_gracza + 1, "właśnie się rozpoczęła!")
        print("Twój całkowity wynik to:", wyniki_graczy[idx_gracza], "\n")
        aktualny_wynik = 0

        while True:
            czy_rzucic = input("Czy chcesz rzucić kostką (y)? ")
            if czy_rzucic.lower() != "y":
                break

            wartosc = rzut_kostka()
            if wartosc == 1:
                print("Wyrzuciłeś 1! Tura zakończona!")
                aktualny_wynik = 0
                break
            else:
                aktualny_wynik += wartosc
                print("Wyrzuciłeś:", wartosc)

            print("Twój wynik to:", aktualny_wynik)

            if aktualny_wynik >= max_score:
                game_over = True
                break

        wyniki_graczy[idx_gracza] += aktualny_wynik
        print("Twój całkowity wynik to:", wyniki_graczy[idx_gracza])

        if game_over:
            break

print("Gracz numer", idx_gracza + 1, "jest zwycięzcą z wynikiem:", aktualny_wynik)


       































