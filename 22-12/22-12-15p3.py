def be():
    x=input(f"Kérem az szöveget:")
    return x
def ism():
    x=int(input("Hányszor ismétled meg?:"))
    return x

sz=be()
for i in range(ism()):
    print(sz)