#hazi_feladat_016
#Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!
megadott_alkalom = int(input("Adja meg, hány alkalommal szeretné megismételni a szöveget: "))
szoveg = input("Adjon meg egy szöveget: ")

alkalom = 0

while alkalom < megadott_alkalom:
    print(szoveg)
    alkalom += 1