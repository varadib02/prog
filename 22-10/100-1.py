import random
min=1
max=100
proba=0
r=random.randint(min,max)
eltalal=False
print("Gondolj egy számra (1-100)")
while eltalal!=True:
    proba+=1
    print(f"A gép tippel:{r}")
    be=input("nagyobb/kisseb  vagy = (n/k/=):")
    if(be=="n"):
        min=r+1
        r=random.randint(min,max)
    elif(be=="k"):
        max=r-1
        r=random.randint(min,max)
    else:
        print(f"Eltalálta a gép: {r} probálkozás {proba}")
        eltalal=True
    