def be():
    maxpont=int(input())
    pont=int(input())
    
    print(f"{megfelte(maxpont,pont)}")
    if megfelte(maxpont,pont):
        print(f"{round(pont/maxpont*100,2)}% {pont} ponttal")

def megfelte(maxpont,pont):
    if maxpont/2<=pont:
        return "Átment"
    else: return "Nem sikerült" 
be()