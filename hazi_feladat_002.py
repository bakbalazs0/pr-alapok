#hazi_feladat_002
#Készíts egy rövid programot, amely a felhasználótól bekéri a kör sugarát, és ennek alapján kiszámolja a kör kerületét és területét!
import math

kor_sugara = float(input("Adja meg a kör sugarát: "))
kerulet = 2 * math.pi * kor_sugara
terulet = math.pi * kor_sugara**2
print(f"A kör kerülete: {kerulet:.2f}cm")
print(f"A kör területe: {terulet:.2f}cm2")