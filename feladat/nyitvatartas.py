nyitvatartas = int(input('Hány óra van most? '))
odaerni = 16 - nyitvatartas
if 8 > nyitvatartas:
    print(f'A bolt zárva.')
elif 8 <= nyitvatartas < 16:
    print(f'A bolt nyitva. Ennyi órád van még odaérni: {odaerni}')
elif 16 <= nyitvatartas:
    print(f'A bolt zárva.')