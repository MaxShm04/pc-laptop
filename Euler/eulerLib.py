def properDivisors(x):
    ret = []
    for n in range(1, x):
        if x % n == 0:
            ret.append(n)
    # print(ret)
    return ret


def sumOfNumArr(x):
    c = 0
    for n in x:
        c += n
    # print(sum)
    return c


def BoolArrToSum(x):
    y = 0
    for n in range(0, len(x)):
        if x[n] == False:
            y += n
    return y


def givePeriod(x):
    if type(x)==float:
        nk = str(x).split(".")[1]
        print(nk)
        period = []
        ind = 0
        for n in nk:
            ind +=1
            if n in period:
                rem = period[:period.index(n)]
                print(rem)
                period.remove(rem)
                if getFollow(period, nk[ind-1:]):
                    print("finishing")
                    return F'({listToString(period)})'
                else:
                    period.append(n)
                    period = rem + period
            else:
                print(F"add {n}")
                period.append(n)
        return False
    return False


def getFollow(liste, strin):
    print(strin)
    ind = 0
    for s in strin:
        ind += 1
        if ind-1 == len(liste):
            print(True)
            return True
        elif s != liste[strin.index(s)]:
            print(False)
            return False


def listToString(x):
    outp = ""
    for n in x:
        outp += str(n)
    return outp


def StringToList(x):
    out = []
    for n in x:
        out.append(n)
    return out
