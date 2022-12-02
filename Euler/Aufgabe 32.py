from eulerLibrary import eulerLib as eL

amount = 0
stat = 10*[False]
ges = []
fac = []

def checkStr(stri):
    global stat
    stat = eL.resetBoolList(stat)
    #print(stat)
    #print(F"Check string {stri}")
    if(len(stri))!=9 or "0" in stri:
        return False
    for n in stri:
        if stat[int(n)]:
            return False
        else:
            stat[int(n)] = True

    return True

#45228
for n in range(1, 1000):
    for m in range(1, 1000):
        amount = n*m
        #print(F"{n}*{m} = {amount}")
        if checkStr(F"{amount}{n}{m}") and amount not in ges:
            print(F"{amount} = {n}*{m}")
            ges.append(amount)
            fac.append(n+m)

print(eL.sumOfNumArr(ges)+eL.sumOfNumArr(fac))