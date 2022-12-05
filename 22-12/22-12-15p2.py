def szamolas(x1,x2,y1,y2):
    import math
    d=math.sqrt(math.pow((x2-x1),2)-math.pow((y2-y1),2))
    return d

print(round(szamolas(2,4,4,3),2))