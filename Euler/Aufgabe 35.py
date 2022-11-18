import eulerLib as eL

prim = eL.givePrimes(100)

def rotations(num): #rotating number and return list
    list = []
    m = str(num)
    counter = 0
    while counter < len(str(num)):
        m=m[1:] + m[0]
        list.append(int(m))
        counter+=1
    list1=sorted(list,key=int)
    return list1

for n in