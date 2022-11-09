import random

ljegyek=[]
letszam=int(input("Osztály létszám: "))
lmenyi=[0,0,0,0,0]

for i in range(letszam):
    ljegyek.append(random.randint(1,5))
print(f"Átlag: {sum(ljegyek)/letszam}")

for i in range(len(ljegyek)):
    for j in range(1,5,1):
        if(ljegyek.index(ljegyek[i])==(j)):
            lmenyi[j]=lmenyi[j]+1

for i in range(len(lmenyi)):
    print(f"{i} jegy: {lmenyi[i]}")

print(f"Legtöbb: {lmenyi.index(max(lmenyi))} jegy {max(lmenyi)}")