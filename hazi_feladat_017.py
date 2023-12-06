#hazi_feladat_017
#Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.
while True:
    megadott_szam = int(input("Kérek egy páros számot: "))
    
    if megadott_szam % 2 == 0:
        print(f"A megadott páros: {megadott_szam}")
        break
    else:
        print("A megadott szám páratlan.")
