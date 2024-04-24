import random

lista = []
for _ in range(30):
    véletlen_szamok = random.randint(0,9)
    lista.append(véletlen_szamok)

meredek_szakasz = 0
for véletlen_szamok in lista:
    if véletlen_szamok >= 2:
        meredek_szakasz += 1

print(f'{meredek_szakasz}')