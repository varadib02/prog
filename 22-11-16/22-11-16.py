import random
letszam=27
lmagassag=[]

for i in range(letszam):
    lmagassag.append(random.randint(160,200))

print(f"Átlagmagasság: {round((sum(lmagassag)/letszam),2)}")
print(f"A legmagassabb a {lmagassag.index(max(lmagassag))}. {max(lmagassag)}cm")
print(f"A legmagassabb és a legalacsonyabb közzöti különbség: {max(lmagassag)-min(lmagassag)}cm")
print(f"A torony magassága: {round(sum(lmagassag)/100,2)}m lenne")
lmagassag.append(182)
lmagassag.sort()
for i in range(len(lmagassag)-1):
    if(lmagassag[i]==lmagassag[i+1]):
        print("Van egyforma")
        break
    elif(lmagassag[-1]==lmagassag[i+1]):
        print("Nincs")
    