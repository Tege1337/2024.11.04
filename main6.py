"""
6. Szorzótábla
Írasd ki egy adott szám szorzótábláját 1-től 10-ig. Például, ha a felhasználó 5-öt ad meg, akkor az eredmény legyen:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""

number = int(input("Adj meg egy számot! "))
current = 1

for x in range(1, 11):
    eredmeny = current * number
    print(f"{current} x {number} = {eredmeny}")
    current += 1