class Autotip:
    def __init__(self,marka,típus,nemzetiseg):
        self.marka=marka
        self.típus=típus
        self.nemzetiseg=nemzetiseg

    def nemzet(self):
        if(self.nemzetiseg=='d'):
            return "német"
        elif(self.nemzetiseg=='a'):
            return "angol"
        elif(self.nemzetiseg=='h'):
            return "magyar"
        elif(self.nemzetiseg=='o'):
            return "olasz"
        else:
            return "ismeretlen"


Lautok=[]
for _ in range(3):
    marka=input("Gyártó: ")
    típus=input("Típus: ")
    nemzetiseg=input("Nemzetiseg: ")
    auto=Autotip(marka,típus,nemzetiseg)
    Lautok.append(auto)

for i in Lautok:
    print(f"A(z) {i.marka},{i.típus} egy {i.nemzet()} auto")