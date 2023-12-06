#hazi_feladat_008
#Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám: pozitív páros vagy negatív páratlan. Az eredményről tájékoztatja a felhasználót.
szam = int(input('Kérek egy számot! '))
if 0 < szam and szam % 2 == 0:
    print('A megadott szám pozitív és páros.')
else:
    print('A megadott szám negatív és páratlan.')