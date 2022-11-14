m30 = [4, 6, 9, 11]
d = 1
m = 1
y = 1900
wt = 1
count = 0
def isSchalt(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


while y!=2001:
    d += 1
    if wt == 6:
        if y>= 1901 and d == 1:
            count+=1
    if wt == 7:
        wt = 1
    else:
        wt += 1
    print(F"{d}/{m}/{y}, {wt}, {count}")
    if d == 28 and m == 2 and isSchalt(y) == False:
        d = 0
        m += 1
        continue
    if d == 29 and m == 2 and isSchalt(y) == True:
        d = 0
        m += 1
        continue
    if d == 30:
        if m in m30:
            d = 0
            m += 1
            #print(m)
            continue
    if d == 31:
        if m == 12:
            d = 0
            m = 1
            y += 1
            #print(y, m)
            continue
        d = 0
        m += 1

print(count)
