import datetime
import time

def ido():
    
    return datetime.datetime.now()

for i in range(10):
    print(ido())
    time.sleep(1)