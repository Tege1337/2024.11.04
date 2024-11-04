"""
2. Összegszámítás
Kérj be egy egész számot, és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.
"""

number = int(input("Adj meg egy egész számot! "))
current_number = 1

for x in range(1, (number + 1)):
    print(f"{current_number}")
    current_number += 1