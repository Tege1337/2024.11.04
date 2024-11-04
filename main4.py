"""
4. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
b) Ha a nagyobb, mint b, akkor csökkenő sorrendben írasd ki őket.
"""

a = int(input("Adj meg egy számot! "))
b = int(input("Adj meg még egy számot! "))

if a < b:
    current = a
    for x in range(a, (b + 1)):
        print(f"{current}")
        current += 1
elif a > b:
    current = a
    for x in reversed(range(b, (a + 1))):
        print(f"{current}")
        current -= 1