def nevelo(szo):
    maganhangzok="aáeéiíuúüűoóöő"
    
    if szo[0] in maganhangzok:
        return "Az"
    else:
        return "A"
    

szo=input("Kérem a szót: ")
szo=szo.lower()
print(f"{nevelo(szo)} {szo}")