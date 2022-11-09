import random

lmagassag = []

for i in range(5):
    cm = int(input(f"Kérem az {i+1}. ember magassagát(cm): "))
    lmagassag.append(cm)

print(lmagassag)
# másolás
lcopy = lmagassag.copy()
print(lcopy)
# növekvő
lmagassag.sort()
print(lmagassag)
print(max(lmagassag))

# max elem hányadik rendezés után
print("Rendezés után a sorban: ", lmagassag.index(max(lmagassag))+1)
print(f"Eredeti a sorban: {lcopy.index(max(lcopy))+1}")

# törlés a rendezetből
del lmagassag[-1]
print(lmagassag)
