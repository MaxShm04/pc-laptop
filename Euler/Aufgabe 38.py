from eulerLibrary import eulerLib as eL

count = 0
h = 0
for n in range(1, 999999999):
    c = ""
    count += 1
    if count == 10000000:
        print(n)
        count = 0
    for i in range(1, int("0"+"9"*(10-len(str(n))))):
        if(len(str(n)))>=8:
            print(F"{n}*{i}")
        c += str(n*i)
        if len(c) >= 10:
            break
        if len(c) == 9:
            eL.isPandigital(c)
            if eL.isPandigital(c):
                if int(c)>h:
                    h = int(c)
            print(F"{c}:{eL.isPandigital(c)}")
            print(h)
            break
print(h)