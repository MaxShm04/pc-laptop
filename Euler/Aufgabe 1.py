import lib
import math
import random
from datetime import datetime

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL


def main():
    list = [random.randint(1, 2000) for n in range(200000000)]
    list = [13, 45, 79, 60, 90, 42, 195, 16, 38, 11, 27, 96, 144, 129, 99, 131, 99, 119, 81, 20, 15, 64, 68, 24, 114,
            110, 8, 134, 80, 150, 167, 35, 83, 43, 111, 96, 197, 191, 70, 112, 91, 22, 19, 99, 1, 76, 165, 12, 163, 79,
            168, 110, 111, 18, 64, 135, 58, 23, 170, 85, 124, 65, 86, 17, 18, 136, 140, 79, 117, 17, 143, 26, 171, 119,
            25, 117, 155, 89, 82, 77, 66, 31, 81, 61, 165, 170, 81, 184, 86, 180, 109, 147, 110, 152, 144, 142, 141,
            114, 146, 180]
    med = int(len(list) / 2)
    l = list[med:]
    r = list[:med]
    #x = sortL(l, r, list[med])
    x = list
    x.sort()
    print(x)


def sortL(l, r, m):
    #print(f"sortStart, med: {m}")
    i = 0
    if len(l) == 1 and len(r)==1:
        if l[0] > r[0]:
            l[0], r[0] = r[0], l[0]
            return l, r
    if len(l) > 1:
        #print(f"len: {len(l)}, {l}")
        for x in range(len(l)):
            if l[i] > m:
                r.append(l[i])
                #print(F"l remove {l[i]}, ind {i}")
                l.remove(l[i])
                i -= 1
            # print(i)
            i += 1

        i = 0
    if len(r) > 1:
        #print(f"len: {len(r)}, {r}")
        for x in range(len(r)):
            # print(r[i])
            if r[i] < m:
                l.append(r[i])
                #print(F"r remove {r[i]}, ind {i}")
                r.remove(r[i])
                i -= 1
            i += 1
    if len(l) > 1:
        med = int(len(l) / 2)
        lN = l[med:]
        rN = l[:med]
        #print(f"sortL({lN},{rN},{med})")
        y = sortL(lN, rN, l[med])
        l = y[0] + y[1]
        #print(f"l finished: l ={y[0]}+{y[1]}")
    if len(r) > 1:
        med = int(len(r) / 2)
        lN = r[med:]
        rN = r[:med]
        #print(f"sortL({lN},{rN},{med})")
        y = sortL(lN, rN, r[med])
        #print(f"r finished: r ={y[0]}+{y[1]}")
        r = y[0] + y[1]
    #print(l, r)
    return l, r


if __name__ == '__main__':
    time = datetime.now()
    #print("[1, 4, 7, 9], [2, 3, 4, 6, 7, 9]")
    #x = sortL([1, 4, 7, 9], [2, 3, 4, 6, 7, 9], 5)
    main()
    #print(x[0] + x[1])
    #print(x)
    print(datetime.now() - time)
    print("-" * 90)
    print("-" * 90)
    print("-" * 90)
    print("-" * 90)
    print("-" * 90)
