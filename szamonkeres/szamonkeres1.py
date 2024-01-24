# Bak Balázs 10.D 1. csoport
"""
Bekérek egy egész számot, irassuk ki hogy a szám pozitív vagy negatív vagy nulla.
"""
egesz_szam = int(input("Kérek egy egész számot! "))
if egesz_szam == 0:
    print("A szám nulla.")
elif egesz_szam < 0:
    print("A szám negatív.")
else:
    print("A szám pozitív.")