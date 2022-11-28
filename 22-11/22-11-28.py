adat=input()

lszam=[]
lszoveg=[]

for i in range(len(adat)):
    #szám-e?
    if(adat[i].isnumeric()==True):lszam.append(int(adat[i]))
    #szöveg-e
    if(adat[i].isalpha()==True): lszoveg.append(adat[i])
print(lszam)
print(lszoveg)
print(round(sum(lszam)/len(lszam),2))