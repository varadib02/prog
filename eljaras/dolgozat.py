def be():
    maxpont=int(input())
    pont=int(input())
    
    print(f"{megfelte(maxpont,pont)}")
    if megfelte(maxpont,pont):
        print(f"{jegy(maxpont,pont)}%")

def megfelte(maxpont,pont):
    if maxpont/2<=pont:
        return "Átment"
    else: return "Nem sikerült" 
def jegy(maxpont,pont):
    return
be()