def vizsgal(kor):
    if kor>=18:
        return True
    else:
        return False
nev=input("Neved: ")
while (nev!=""):
    kor=int(input("Korod: "))
    if (vizsgal(kor)):
        print("Kaphat")
    else:
        print("Nem kaphat")
    nev=input("Neved: ")