abundant = []
x = 11
res = []
while x < 28123:
    x += 1
    # print(x)
    if eL.sumOfNumArr(eL.properDivisors(x)) > x:
        abundant.append(x)
print(abundant)
for x in range(1, 28123):
    s = False
    print(x)
    for n in abundant:
        if s:
            break
        if n < x:
            for m in abundant:
                if m < x - n:
                    if n + m == x:
                        s = True
                        break
    if s == False:
        res.append(x)
print(x)
print(eL.sumOfNumArr(res))
