#hazi_feladat_012
#A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
import random
valasztas = input("Válassza ki, fej vagy írás: ").lower()
eredmeny = random.choice(["fej", "írás"])
print(f"A pénzfeldobás eredménye: {eredmeny}")
if valasztas == eredmeny:
    print("Gratulálunk, eltalálta!")
else:
    print("Sajnáljuk, nem találta el.")
