import eulerLib as eL

out = []


for n in range(1, 1000000):
    b = eL.NumbToBin(n, 16)
    #print(b)
    if eL.isPalindrom(n):
        for i in range(0, len(b)):
            if b[0] == "0":
                if eL.isPalindrom(b):
                    out.append(n)
                    #print(True)
                    break
                else:
                    b = b[1:]
                    #print(b)
            else:
                if eL.isPalindrom(b):
                    out.append(n)
                    #print(True)
                    break
                else:
                    #print(False)
                    break
    #else:
        #print(F"{n} False")
print(out)
print(eL.sumOfNumArr(out))