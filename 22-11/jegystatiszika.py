import random

ljegyek=[]
letszam=int(input("Osztály létszám: "))
lmenyi=[]

for i in range(letszam):
    ljegyek.append(random.randint(1,5))
print(f"Átlag: {round(sum(ljegyek)/letszam,2)}")

for i in range(5): lmenyi.append(0)

for i in range(len(ljegyek)):
    for j in range(1,5,1):
        if(ljegyek.index(ljegyek[i])==(j)):
            lmenyi[j]=lmenyi[j]+1

for i in range(len(lmenyi)):
    print(f"{i+1} jegy: {lmenyi[i]}")

print(f"Legtöbb jegy: {lmenyi.index(max(lmenyi))+1}  {max(lmenyi)}db")