from audioop import avg
from multiprocessing import Value
from random import randint

lszamok = []

for i in range(15):
    #lszamok.append(int(input("Szám: ")))
    lszamok.append(randint(1,200))

'''be = int(input("Szám: "))
while (be != 0):
    lszamok.append(be)
    be = int(input("Szám: "))
'''


db = 0
for i in lszamok:
    if (i % 2 == 0):
        print(i,end=", ")
        db += 1
print(f"Páros: {db}")
osszeg=sum(lszamok)
print(f"Átlag: {round(osszeg/len(lszamok),2)}")
#sorren fordítása
lszamok.reverse()

keresett=input("Add meg a keresett számot: ")
if (keresett in lszamok):
    print("Van ilyen szám a listában")
if(keresett not in lszamok and keresett):
    print("Nincs ilyen szám")