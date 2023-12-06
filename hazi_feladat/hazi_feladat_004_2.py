#hazi_feladat_004/2
#Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"
nap = input('Jó napod volt? ')
if nap == 'Igen':
    print('Az jó!')
elif nap == 'Nem':
    print('Az nem jó!')
else: 
    print('Sajnos nem értem a válaszodat!')