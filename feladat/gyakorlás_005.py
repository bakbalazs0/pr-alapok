import random
generalt_szam = random.randint(1,3)
megadott_szam = int(input("Kérem adjon meg egy számot! "))
if generalt_szam == megadott_szam:
    print("A két szám egyenlő.")
if generalt_szam > megadott_szam:
    print("A generált szám nagyobb.")
if generalt_szam < megadott_szam:
    print("A generált szám kisebb.")