import random
sz=[]
szclone=[]
for i in range(10):
    sz.append(random.randint(-10,10))

szclone.append=sz

print(szclone)
for i in range(len(sz)):
    if sz[i]<0:del szclone[i]
print(szclone)