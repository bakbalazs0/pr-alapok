# Bak Balázs 10/D 
szelesseg = float(input('Adj meg a téglalap szélességet! '))
magassag = float(input('Adja meg a téglalap magasságot! '))
terulet = magassag * szelesseg
if magassag >  szelesseg:
    print(f'Ez egy álló téglalap. Területe: {terulet}')
elif szelesseg > magassag:
    print(f'Ez egy fekvő téglalap. területe: {terulet}')
else:
    print(f'A téglalap egy négyzet. Területe: {terulet}')