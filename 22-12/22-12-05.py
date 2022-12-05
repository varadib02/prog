def vizsgal(x):
    ered=False
    if (0>x):
        return not ered
    else:
        return ered

def be():
    x=int(input("Szám: "))
    return x

szam=be()

if (vizsgal(szam)):
    print("Negatív szám")
else:  
  print("Pozítív szám")
    