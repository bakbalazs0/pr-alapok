# összeg fügvény 
lista5 = [12, 5, 2, 8, 9, 11, 10, 16, 6]

def osszeg(list):
    szumma = 0
    for szam in list:
        szumma = szumma + szam
    return szumma

print(f'A lista5 elemeinek összege: {osszeg(lista5)}')
