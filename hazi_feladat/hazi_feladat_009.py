#hazi_feladat_009
#Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni! Például így: Jön Henrik ma kosarazni? (igen/nem). A program írja ki, hogy melyik állítás igaz az alábbiak közül: egyikük sem jön kosarazni, mind a ketten jönnek kosarazni, csak az egyikük jön kosarazni.
henrik_kosarazik = input("Jön Henrik ma kosarazni? (igen/nem): ").lower() == 'igen'

hanna_kosarazik = input("Jön Hanna ma kosarazni? (igen/nem): ").lower() == 'igen'
if not henrik_kosarazik and not hanna_kosarazik:
    print("Egyikük sem jön kosarazni.")
elif henrik_kosarazik and hanna_kosarazik:
    print("Mind a ketten jönnek kosarazni.")
else:
    print("Csak az egyikük jön kosarazni.")
