#hazi_feladat_007
#Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
import random

gep = random.randint(1,5)
felhasznalo = int(input('Kérek egy számot 1 és 5 között! '))
if gep == felhasznalo:
    print('A gép által gondolt és a felhasználó által gondolt szám egyezik.')
elif gep > felhasznalo:
    print('A gép által gondolt szám nagyobb mint a felhasználó által gondolt szám.')
elif gep < felhasznalo:
    print('A gép által gondolt szám kisebb mint a felhasználó által gondolt szám.')