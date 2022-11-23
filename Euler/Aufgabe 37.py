import eulerLib as eL

h = 0
for n in range(1, 123456789):
    c = ""

    for i in range(1, int("9"*(9-len(str(n))))):
        if(len(str(n)))>=7:
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
            break

print(h)