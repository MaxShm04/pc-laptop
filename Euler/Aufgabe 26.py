from eulerLibrary import eulerLib as eL

leng = 0

for n in range(101, 102):
    print(F"{eL.givePeriod(1/n, 0)}, {n}")
    if eL.givePeriod(1/n, 1) > leng:
        leng = n
        print(F"length: {leng}, {1/n}")
print(leng)
#print(eL.givePeriod(1/leng, 1))
#print(eL.givePeriod(1/leng, 0))
