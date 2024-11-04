"""
5. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják. Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""

jelszo = "asd"

rossz = True
while rossz:
    kerdes = input("Kérlek írd be a jelszavad! ")
    if kerdes == jelszo:
        print("Belépés sikeres! ")
        rossz = False
    else:
        print("Helytelen jelszó!")