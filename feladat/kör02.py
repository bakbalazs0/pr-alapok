class Kor:
    osztaly_valtozo = 111
    evszam = 2024

    def __init__(self, sugar, kozeppont = (0, 0)):
        self.sugar1 = sugar 
        self.kozeppont1 = kozeppont

    def terulet(self):
        #return self.sugar1 * pow(3.14, 2)
        return self.sugar1 * self.sugar1 * 3.14

    def kerulet(self):
        return self.sugar1 * 3.14 * 2

kor_01 = Kor(5, (2, 6))
print(Kor.evszam)
print(kor_01.evszam)

kor_01 = Kor(5, (2, 6))
print(f'A kor_01 területe: {kor_01.terulet():.2f}')
print(f'A kor_01 kerülete: {kor_01.kerulet():.2f}')

kor_02 = Kor(10)
print(f'A kor_02 területe: {kor_02.terulet():.2f}')
print(f'A kor_02 kerülete: {kor_02.kerulet():.2f}')

print(f'A kor_01 és a kor_02 területe: {kor_01.terulet() + kor_02.terulet():.2f}')
print(f'A kor_01 és a kor_02 kerülete: {kor_01.kerulet() + kor_02.kerulet():.2f}')

print(f"{kor_01.sugar1}")
print(f"{kor_02.sugar1}")