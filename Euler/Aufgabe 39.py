import math

out = []
c = 0
for n in range(1, 1001):
    state = False
    add = []
    c += 1
    if c == 1:
        print(n)
        print(out)
        c = 0
    for a in range(1, 1001):
        if n <= a:
            state = True
            break
            print(F"{n}:{a}")
        for b in range(1, 1001):
            if n <= a+b:
                state = True
                break
            print(F"{n}:{a}:{b}")
            for c in range(1, 1001):
                if a + b + c > n:
                    state = True
                    break
                print(F"{n}:{a}:{b}:{c}")
                if a+b+c==n and math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
                    add.append(a)
                    add.append(b)
                    add.append(c)
            if state == True:
                break
        if state == True:
            break
    out.append(add)