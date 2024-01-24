# feladat_031

# Amit már tudtunk a szövegekről (sztringekről):

# Szövegek (sztringek) összefűzhetőek
print('Jöttem' + ' ' + 'láttam' + ' ' + 'győztem.')

# Szövegek (sztringek) szorzásjellel megsokszorozhatóak
print('ja' + 'j' * 7)

# Más adattípusok szöveggé (sztringgé) alakíthatóak az str() függvénnyel
print(str(7.53))

# ----------------------------------------------------------------------

# Hasonlítanak a listákhoz:

sztring = 'Ismered ezt a számot?'

# Index-szel hivatkozhatunk egy elemükre
print(sztring[0])      # I
print(sztring[-1])     # ?

# Szeletelhetjük ezeket is
print(sztring[2:11])
print(sztring[:9])
print(sztring[7:])

# Meghatározhatjuk a hosszukat
print(len(sztring))
szamlalo = 0
# for-ciklussal is bejárhatóak
for betu in sztring:
    if betu == 'e' or betu == 'E':
        szamlalo += 1
print(f'A sztringben {szamlalo} db e/E betű van.')

# Ezeknél is használható az in operátor
if 'e' in sztring:
    print('Van benne e betű.')
else:
    print('Nincs benne e betű.')

# ----------------------------------------------------------------------

# Különböznek a listáktól:

# Természetesen csak karaktereket tartalmazhatnak!

# Elemeik (a karakterek) nem módosíthatóak!
# Ez hibát okoz:
sztring = 'Ismered ezt a számot?'
sztring[0] = 'i'

# ----------------------------------------------------------------------
