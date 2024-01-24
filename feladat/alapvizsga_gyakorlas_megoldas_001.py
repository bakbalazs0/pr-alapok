nev = input("Adja meg a kersztnevét: ")
kor = int(input("Adja meg az életkorát: "))
if kor < 1:
    print("A kora alapján", nev, "csecsemő!")
elif kor < 6: 
    print("A kora alapján", nev, "kisgyerek!")
elif kor < 12:
    print("A kora alapján", nev, "gyerek!")
elif kor < 16:
    print("A kora alapján", nev, "serdülő!")
elif kor < 25:
    print("A kora alapján", nev, "ifjú!")
