from datetime import datetime

import eulerLib as eL

time = datetime.now()
out = []
o = 0
for n in eL.givePrimes(999999):   #999999999
    if eL.isPandigital(n, len(str(n))):
        print(F"n:{n}")
        if n > o:
            o = n

#print(F"n:{n}")
print(F"o:{o}")
print(time - datetime.now())