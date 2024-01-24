homerseklet = int(input("Kérem írja be a testhőmérsékletét! "))
if homerseklet < 37:
    print("Normális.")
elif homerseklet >= 40:
    print("Kórház.")
elif homerseklet >= 38:
    print("Lázas.")
elif homerseklet >= 37:
    print("Hőemelkedés.")
