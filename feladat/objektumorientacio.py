import random

class Kor:
    def __init__(self, sugar, kozeppont = (0, 0)):
        self.sugar = sugar 
        self.kozeppont = kozeppont

    def terulet(self):
        return self.sugar * pow(3.14, 2)

    def kerulet(self):
        return self.sugar * 3.14 * 2

""" #objektum létrhozása
kor_01 = Kor(5, (2, 6))
"""
""" #objektum tesztelése
print(kor_01)
    print(type(kor_01))
    print(isinstance(kor_01, Kor))
"""
"""
A korok nevű listában tárol 5 darab kor obejktumot, melyek surgara
[0; 10] tartományba eső, véletlenszerűen előállított számérték.
"""

korok = []
for _ in range(5):
    kor = Kor(random.randint(0, 10))
    korok.append(kor)

for kor in korok: 
    kor.info()

# hivatkozás a lista egy elemére:
korok[0].sugar()

"""
kor01 = Kor(5)
print(kor01.kozeppont)

kor02 = Kor(10, (1, 1))
print(kor02.kozeppont)
"""
