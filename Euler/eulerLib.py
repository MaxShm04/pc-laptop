def properDivisors(x):
    ret = []
    for n in range(1, x):
        if x % n == 0:
            ret.append(n)
    #print(ret)
    return ret


def sumOfNumArr(x):
    sum = 0
    for n in x:
        sum += n
    #print(sum)
    return sum

def truefalseArrInnumToSum(x):
    y = 0
    for n in range(0, len(x)):
        if x[n]==True:
            y += n
    return y



