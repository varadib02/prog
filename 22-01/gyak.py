#beírás
f=open("22-01/dolgozok.txt","w")

#random
from random import *
szam10=[]

for i in range(10):
    r=randint(1,101)
    szam10.append(str(r))
    f.writelines(szam10[i]+"\n")


f.close()
#olvasas
f=open("22-01/dolgozok.txt","r")
jav=[]
for i in f:
    x=i.rstrip()
    jav.append(int(x))

print(f)
print(jav)

print(sum((jav))/len(jav))