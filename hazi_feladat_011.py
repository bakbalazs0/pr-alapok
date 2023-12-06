#hazi_feladat_011
#Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
import random
generalt_szam = random.randint(1, 3)
szam = int(input("Kérek egy számot 1 és 3 között: "))

# Összehasonlítja a generált és a felhasználó által megadott számot
if szam == generalt_szam:
    print(f"A {generalt_szam} és a {szam} megegyezik.")
else:
    print(f"A {generalt_szam} és a {szam} nem egyezik.")
