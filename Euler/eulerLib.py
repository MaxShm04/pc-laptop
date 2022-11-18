def properDivisors(x):
    ret = []
    for n in range(1, x):
        if x % n == 0:
            ret.append(n)
    # print(ret)
    return ret

def is_even(x):
    if x % 2 == 0:
        return True
    return False

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


def givePeriod(x, y):
    if type(x)==float:
        nk = str(x).split(".")[1]
        vk = str(x).split(".")[0]
        #print(nk)
        period = []
        ind = 0
        zeros = []
        rem = []
        for n in nk:
            if n!="0":
                break
            else:
                zeros.append(n)
        """        
        #print(zeros)
        for n in nk:
            ind +=1
            if n in period:
                #print("again")
                rem = period[:period.index(n)]
                for r in rem:
                    #print(F"remove {r}")
                    period.remove(r)
                if getFollow(period, nk[ind-1:]):
                    #print("finishing")
                    if y == 0:
                        return F'{vk}.{listToString(zeros)}{listToString(rem)}({listToString(period)})'
                    else:
                        return len(period)
                else:
                    period.append(n)
                    period = rem + period
            else:
                #print(F"add {n}")
                period.append(n)
        return x"""
    return False


def getFollow(liste, strin):
    #print(strin)
    ind = 0
    for s in strin:
        ind += 1
        if ind-1 == len(liste):
            #print(True)
            return True
        elif s != liste[strin.index(s)]:
            #print(False)
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

def emptyList(x):
    ret = []
    for n in range(0, x):
        ret.append(0)
    return ret


def resetBoolList(x):
    ret = [False]*len(x)
    return ret

def stringToIntList(x):
    ret = []
    for n in x:
        ret.append(int(n))
    return ret

def givePrimes(rang):
    prim = [2, 3, 5, 7]
    state = False
    for n in range(8, rang):
        for m in range(2, n):
            if n % m == 0:
                state = True
        if not state:
            prim.append(n)
        state = False
    return prim

def isPrim(x):
    state = False
    for m in range(2, x):
        if x % m == 0:
            state = True
    if not state:
        return True
    return False


