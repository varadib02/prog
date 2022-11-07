
for i in range(99, 0, -3):  # 99töl csökenő sorend 3mal oszthatók
    print(i)

for i in range(101, 50, -1):
    if i % 5 == 0:
        print(2*i)


n = int(input())
eredmeny = 0
for i in range(1, n, 1):
    eredmeny += i*i
print(f"{round(eredmeny/n,2)}")

elso=int(input("Első elem: "))
dif=int(input("Növekves: "))
elemszam=int(input("Elemszam: "))

for i in range(elemszam):
    print(elso)
    elso+=dif
