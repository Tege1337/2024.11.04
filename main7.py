"""
8. Prímszám ellenőrzés
Kérj be egy számot, és döntsd el, hogy prímszám-e vagy sem. A program akkor jelezze, ha prímszámot talált, és akkor is, ha nem az.
"""

number = int(input("Adj meg egy számot: "))

if number <= 1:
    print(f"{number} az nem egy prímszám! ")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} az egy prímszám! ")
    else:
        print(f"{number} az nem egy prímszám. ")
