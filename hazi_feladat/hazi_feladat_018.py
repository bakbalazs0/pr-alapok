#hazi_feladat_018
#Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt.
import random

osszeg = 0
harmas_oszthato_szamok = []

while osszeg < 20:
    veletlenszam = random.randint(1, 12)
    
    if veletlenszam % 3 == 0:
        harmas_oszthato_szamok.append(veletlenszam)
        print(veletlenszam)
        osszeg += 1
print(f"\nA 3-mal osztható számok száma: {osszeg}")