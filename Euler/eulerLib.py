import math
import random


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
    if type(x) == float:
        nk = str(x).split(".")[1]
        vk = str(x).split(".")[0]
        # print(nk)
        period = []
        ind = 0
        zeros = []
        rem = []
        for n in nk:
            if n != "0":
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
    # print(strin)
    ind = 0
    for s in strin:
        ind += 1
        if ind - 1 == len(liste):
            # print(True)
            return True
        elif s != liste[strin.index(s)]:
            # print(False)
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
    ret = [False] * len(x)
    return ret


def stringToIntList(x):
    ret = []
    for n in x:
        ret.append(int(n))
    return ret


def givePrimes(rang):
    prim = [2, 3, 5, 7]
    state = False
    i = 0
    for n in range(8, rang):
        for m in range(2, math.floor(n / 2) + 1):
            if n % m == 0:
                state = True
        if not state:
            prim.append(n)
            i += 1
            if i == 1000:
                print(n)
                i = 0
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


def NumbToBin(x, l=8):
    return f'{x:0{l}b}'


def isPalindrom(data):
    if type(data) == str:
        if is_even(len(data)):
            if split(data)[0] == rotate(split(data)[1]):
                return True
            return False
        else:
            data = data
            data = deleteMid(data)
            return isPalindrom(data)
    else:
        try:
            return isPalindrom(str(data))
        except:
            return ValueError



def split(data):
    data = str(data)
    x = len(data)
    return [data[:x // 2], data[x // 2:x]]


def rotate(data):  # rotating number and return list
    data = str(data)
    out = []
    for n in data:
        out.insert(0, n)
    return listToString(out)


def deleteMid(data):
    data = str(data)
    if len(data) % 2 == 1:
        x = StringToList(data)
        del x[math.floor(len(data)/2)]
        #print(x)
    return listToString(x)


def matrToText(data):
    out = ""
    for m in data:
        out += "(\t"
        for e in m:
            out += F"{e}\t"
        out += ")\n"
    return out


def matrSetRand(data, ran=10):
    for n in range(0, len(data)):
        for i in range(0, len(data[n])):
            data[n][i] = random.randint(0, (ran + 1))
    return data

def createMatrix(h, l):
    x = []
    for n in range(0, h):
        for i in range(0, l):
            x[n].append(0)
        x.append([])
    return x
