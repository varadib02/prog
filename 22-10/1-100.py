import random
r=random.randint(1,100)
be=int(input("Barkópa! Kérek egy számot 1-100 között: "))
proba=0
while r!=be:
    if be>r:
        print("Kisseb számra gondoltam.")
        be=int(input("Kérek egy új számot 1-100 között: "))
    elif be<r:
        print("Nagyobb számra gondoltam.")
        be=int(input("Kérek egy új számot 1-100 között: "))
    proba+=1
print(f"Eltaláltad a szám: {r} próbálkozások száma: {proba}")
    