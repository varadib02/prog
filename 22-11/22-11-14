list = []

be=input("Szám: ")
while (be!=""):
    be=int(be)
    while(be in list):
        print("Van már ilyen szám")
        be=input("Szám: ")
    if (be!=""):
        list.append(int(be))
        be=(input("Szám: "))

print(list)

for i in range(len(list)-1):
    if(((list[i]+1)==list[i+1])or((list[i]-1)==list[i-1])):
        print("Van egymást követő szám")
        break
    elif(list[-1]==list[i+1]):
        print("Nincs")
