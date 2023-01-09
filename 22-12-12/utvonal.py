be=open("22-12-12/utvonal.txt","r")

nev=[]
hossz=[]
a=[]

for i in be:
     db=i.split("\t")
     nev.append(db[0])
     hossz.append(db[1])
     a.append(db[2].split("\n"))

print(len(nev))
print(a)
