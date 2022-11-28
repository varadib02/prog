adat=input()

lszam=[]
lszoveg=[]

for i in range(len(adat)):
    #száme?
    if(adat[i].isnumeric()==True):lszam.append(adat[i])
    #szöveg-e
    if(adat[i].isalpha()==True): lszoveg.append(adat[i])

print(lszam)
print(lszoveg)