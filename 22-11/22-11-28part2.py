lszemélyi=input()
szam=0
betu=0
while(len(lszemélyi)!=8 or szam!=6 or betu!=2):
    if(len(lszemélyi)==8):print("Hossza: ✓")
    else:
        print("Kérem újból: ")
        lszemélyi=input()


    for i in range(len(lszemélyi)):
        if(lszemélyi[i].isnumeric() and i<=6):szam+=1
        if(lszemélyi[i].isalpha() and i>=6):betu+=1
        
    if(szam==6):print("Szam: ✓")
    if(betu==2):print("Betű: ✓")
    if(szam!=6 or betu!=2):
        print("Kérem újból: ")
        lszemélyi=input()

    