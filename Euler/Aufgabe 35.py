import eulerLib as eL

prim = eL.givePrimes(1000000)


def rotations(num):  # rotating number and return list
    list = []
    m = str(num)
    counter = 0
    while counter < len(str(num)):
        m = m[1:] + m[0]
        list.append(int(m))
        counter += 1
    list1 = sorted(list, key=int)
    return list1


print(prim)
state = False

out = []
for n in prim:
    for i in rotations(n):
        if i not in prim:
            state = True
    if state == False:
        out.append(n)
    state = False

print(len(out))
