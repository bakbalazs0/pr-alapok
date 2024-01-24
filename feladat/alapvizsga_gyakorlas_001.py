# életszakaszok
knev = input("Adja meg a keresztnevét: ")
eletkor = int(input("Adja meg az  életkorát: "))
if eletkor < 1:
    print(f"A kora alapján {knev} csecsemő!")
elif eletkor > 65:
    print(f"A kora alapján {knev} nyugdíjas!")
elif eletkor <= 6:
    print(f"A kora alapján {knev} kisgyerek!")
elif eletkor <= 12:
    print(f"A kora alapján {knev} gyerek!")
elif eletkor <= 16:
    print(f"A kora alapján {knev} serdülő!")
elif eletkor <= 25:
    print(f"A kora alapján {knev} ifjú!")
elif eletkor <= 65:
    print(f"A kora alapján {knev} felnőtt")