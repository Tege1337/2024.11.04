"""
9. Piramis rajzolása csillagokkal
Kérj be egy számot, amely megadja a piramis magasságát, majd rajzolj ki egy csillagpiramist ennek megfelelően. Például egy 5 magas piramis:
   *
   ***
  *****
 *******
*********
"""

height = int(input("Add meg a piramis magasságát: "))

for x in range(1, height + 1):
    stars = 2 * x - 1
    space = height - x
    print(" " * space + "*" * stars)
