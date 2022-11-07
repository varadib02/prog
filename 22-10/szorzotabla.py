import random

hossz = int(input("Hány feladat legyen: "))
jo=0
for i in range(hossz):
    sz1 = random.randint(1, 10)
    sz2 = random.randint(1, 10)
    eredmeny=sz1*sz2
    valasz=int(input(str(i+1)+". feladat "+str(sz1)+"*"+str(sz2) +"="))
    if eredmeny==valasz:
        print("Helyes válasz!")
        jo+=1
    else:
        print(f"Rossz Eredmény! A helyes válasz {sz1*sz2}")

print(f"statisztika: {hossz}/{jo} {round(jo/hossz*100,2)}%")