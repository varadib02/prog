ladat=[]

for i in range(3):
    adat=float(input("Kérek egy számot: "))
    while(adat<0):
        print("Rosz")
        adat=float(input("Kérek egy számot: "))
    ladat.append(adat)
print(ladat)