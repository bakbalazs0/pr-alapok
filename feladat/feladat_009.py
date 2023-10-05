# feladat_009
"""
Kérjük be két egész számot, szám1 és szám2.
Hasonlítsuk össze a két számot, és írassuk ki, hogy szám1 kisebb mint a szám2, vagy a szám2 kisebb mint a szám1, vagy a szám1 egyenlő szám2-vel.
"""
szam1 = input(f"Kérek egy számot! ")
szam1 = int(szam1)
szam2 = input(f"Kérek egy másik számot! ")
szam2 = int(szam2)
if szam1 == szam2:
    print(f"{szam1} és {szam2} egyenlő.")
elif szam1 < szam2:
    print(f"Az {szam1} kisebb mint {szam2}.")
else:
    print(f"Az {szam1} nagyobb mint {szam2}.")