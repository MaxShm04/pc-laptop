import lib

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL
import math

prims = [3, 7, 9, 11]
ps, pe = 10, 10
def main(s, e):
    global ps
    global pe
    for n in range(s, e):
        #print(n)
        if n % 2 == 1 and not eL.isPrim(n):
            state = False
            out = []
            for l in eL.givePrimes(n, start=ps):
                prims.append(l)
            ps = n
            #print(prims)
            for p in prims:
                r = n - p
                print(F"{r} = {n} - {p}")
                if r != 0 and r == (2 * (math.pow(a, 2) for a in range(1, int(r)))):
                    print(F"state True")
                    state = True
                    break
                else:
                    out = [n, r, p]
            if not state:
                return out
    return False


st = 10
e = 1000
while True:
    x = main(st, e)
    if not x:
        st, e = e, e*10
        print(F"Start {st}, end {e}")
    else:
        print(x)
        break
