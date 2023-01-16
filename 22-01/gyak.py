#beírás

f=open("22-01/dolgozok.txt","w")

x=input("Kérek egy nevet: ")
while x!="":
    f.writelines(str(x)+"\n")
    x=input("Kérek egy nevet: ")

#random

from random import *
szam10=[]

for i in range(10):
    r=randint(1,100)
    szam10.append(int(r))

f.close()