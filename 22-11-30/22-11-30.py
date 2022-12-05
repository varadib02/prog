be="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

szo=be.split(" ")
mondat=be.split(".")
lszam=[]

print(f"1. feladat: Karakterek száma {len(be)}")
print(szo)
print(f"2. feladat: Szavak száma {len(szo)}")
print(f"3. feladat: Mondatok száma {len(mondat-1)}")

for i in range(len(szo)):
    x=szo[i]
    number=""    
    for k in range(len(x)):
        if(x[k].isdigit()==True):
            number=number+str(x[k])
    if(number!=""):lszam.append(int(number))

print(f"4. feladat: Évszámok kiszedése {lszam}")
print(f"5. feladat: Különbség {max(lszam)-min(lszam)}")