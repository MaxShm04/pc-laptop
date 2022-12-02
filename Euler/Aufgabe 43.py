from datetime import datetime

from eulerLibrary import eulerLib as eL

time = datetime.now()
out = []
#state = 0
for n in range(1000000000, 9876543210):#9876543210
    state = 0
    s = str(n)
    #print(n)
    if eL.isPandigital(n, nul=True):
        #print(True)
        if int(F"{s[1]}{s[2]}{s[3]}") % 2 == 0:
            state += 1
        if int(F"{s[2]}{s[3]}{s[4]}") % 3 == 0:
            state += 1
        if int(F"{s[3]}{s[4]}{s[5]}") % 5 == 0:
            state += 1
        if int(F"{s[4]}{s[5]}{s[6]}") % 7 == 0:
            state += 1
        if int(F"{s[5]}{s[6]}{s[7]}") % 11 == 0:
            state += 1
        if int(F"{s[6]}{s[7]}{s[8]}") % 13 == 0:
            state += 1
        if int(F"{s[7]}{s[8]}{s[9]}") % 17 == 0:
            state += 1
        if state == 7:
            print(n)
            out.append(n)


print(out)
print(eL.sumOfNumArr(out))
print(time - datetime.now())