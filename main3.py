"""
3. Számok listázása és összegzése
Írj egy programot, amely bekér  n számot a felhasználótól, majd egy while ciklussal megkérdezi a felhasználót, hogy szeretne-e újabb számot megadni. Addig folytassa a program a számok bekérését,
amíg a felhasználó igennel válaszol. A program végén jelenítse meg a bekért számok összegét.

b) jelenítse meg a bekért számokat (lista használata)
"""

number = int(input("Adj meg egy számot! "))
number_store = []
number_store.append(number)

running = True
while running:
    question = input("Szeretnél megadni még egy számot? (y/n): ").upper()
    if question == "Y":
        current_number = int(input("Add meg a következő számot! "))
        number_store.append(current_number)
        number += (current_number)
    else:
        running = False
print(f"A számok összege: {number}")
print(f"A számaid: {number_store}")