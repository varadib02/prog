def be():
    a=int(input())
    b=int(input())
    c=int(input())

    if(szerk(a,b,c)==True):
        print("Szerkezthető")
        print(terulet(a,b,c))
        print(kerulet(a,b,c))
    else:
        print("Nem Szerkezhető")

def szerk(a,b,c):
    if (a<b+c and b<a+c and c<a+b):
        terulet(a,b,c)
        kerulet(a,b,c)
        return True
    else:
        return False

def terulet(a,b,c):
    T=a*b*0.5
    return T

def kerulet(a,b,c):
    K=a+b+c
    return K

be()
