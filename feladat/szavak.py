szo1 = str(input('Adj meg egy szót! '))
szo2 = str(input('Adj meg egy másik szót! '))
szo1 = len(szo1)
szo2 = len(szo2)
szo1 = str(szo1)
szo2 = str(szo2)

if szo1 < szo2:
    print(f'A hosszabb szó: {szo2}')
elif szo1 > szo2:
    print(f'A hosszabb szó: {szo1}')
else:
    print(f'A két szó egyforma hosszú.')