def properDivisors(x):
    ret = []
    for n in range(1, x):
        if x % n == 0:
            ret.append(n)
    #print(ret)
    return ret


def sumOfNumArr(x):
    c = 0
    for n in x:
        c += n
    #print(sum)
    return c

def BoolArrToSum(x):
    y = 0
    for n in range(0, len(x)):
        if x[n]==False:
            y += n
    return y



