# feladat_009
"""
Kérjük be két egész számot, szám1 és szám2.
Hasonlítsuk össze a két számot, és írassuk ki, hogy szám1 kisebb mint a szám2, vagy a szám2 kisebb mint a szám1, vagy a szám1 egyenlő szám2-vel.
"""
szam1 = input(f"Kérek egy számot! ")
szam1 = int(szam1)
szam2 = input(f"Kérek egy másik számot! ")
szam2 = int(szam2)

#----------------------------------------
"""
if szam1 < szam2:
    print(f"A szam1 kisebb mint a szam2.")
elif szam1 > szam2:
    print(f"A szam2 kisebb mint a szam1.")
else:
    print(f"A szam1 és a szam2 egyenlő.")
"""

#----------------------------------------
""""
if szam1 < szam2:
    print(f"A szam1 kisebb mint a szam2.")
if szam1 > szam2:
    print(f"A szam2 kisebb mint a szam1.")
if szam1 == szam2:
    print(f"A szam1 és a szam2 egyenlő.")
"""

#----------------------------------------
if szam1 < szam2:
    print(f"A szam1 kisebb mint a szam2.")
elif szam1 > szam2:
    print(f"A szam2 kisebb mint a szam1.")
elif szam1 == szam2:
    print(f"A szam1 és a szam2 egyenlő.")