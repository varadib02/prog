from random import *

fajl=open("beolvasas/szamok.txt","w")
for i in range(10):
    fajl.write(str(randint(1,100))+"\n")
fajl.close()

fajl=open("beolvasas/szamok.txt","r")
#a /n sornak veszi a print
#egymas alá
lszam=[]
for i in fajl:
    i=i.rstrip()
    lszam.append(i)
    print(i)

print(lszam)
#egymasmelé
fajl=open("beolvasas/szamok.txt","r")
for i in fajl:
    i=i.rstrip()
    print(i,end=" ")