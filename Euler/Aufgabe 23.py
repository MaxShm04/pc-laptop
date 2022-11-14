import eulerLib as eL

abundant = []
x = 11
res = []
lim = 28123
while x < lim:
    x += 1
    print(x)
    if eL.sumOfNumArr(eL.properDivisors(x)) > x:
        abundant.append(x)
print(abundant)


expr = [False] * lim
for n in range(1, lim):
    for i in range(1, lim):
        if n + i < lim:
            expr[n+i] = True

print(eL.truefalseArrInnumToSum(expr))
