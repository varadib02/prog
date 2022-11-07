import random

lmagaság=[]
lsziget=[]
lviz=[]

for i in range(20):
    r = random.randint(0,1)
    if r==0:
        lviz.append(r)
    else:
        r = random.randint(1,9)
        lsziget.append(r)
    lmagaság.append(r)

print(lmagaság)
print(f"A legmagassabb pont: {max(lmagaság)}")

print(f"A legalacsonyabb és legmagasabb hegy közötti különbség: {max(lsziget)-min(lsziget)}")

if len(lsziget)>len(lviz):
    print("Több a szárazföld")
elif len(lsziget)<len(lviz):
    print("Több a viz")
else:
    print("Egyforma")