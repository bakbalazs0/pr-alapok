#hazi_feladat_010
#Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy: csak 3-mal osztható, csak 4-gyel osztható, 3-mal és 4-gyel is osztható, sem 3-mal, sem 4-gyel nem osztható!
szam = int(input('Kérek egy egész számot! '))
if szam % 3 == 0:
    print('A megadott egész szám csak 3-mal osztható.')
elif szam % 4 == 0:
    print('A megadott egész szám csak 4-gyel osztható.')
elif szam % 3 == 0 and szam % 4 == 0:
    print('A megadott egész szám 3-mal és 4-gyel is osztható.')
else:
    print('A megadott egész szám sem 3-mal sem 4-gyel nem osztató.')