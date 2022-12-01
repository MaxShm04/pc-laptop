import eulerLib as eL

pen = []
penR = []
out = []
s = 1
e = 10
def run(start, end):
    for n in range(start, end):
        pen.append(int(n*(3*n-1)/2))
        penR.append(int(n*(3*n-1)/2))
    penR.reverse()

    for j in penR:
        state = False
        for k in pen:
            if (j + k) in pen:
                #print(F"Add true:{j}+{k}={j+k}")
                state = True
            if not (j - k) in pen:
                #print(F"Sub true:{j}-{k}={j-k}")
                state = False

            if state:
                out.append(j)
                out.append(k)
                break
        if state:
            break
while len(out)==0:
    run(s, e)
    print(F"length {len(pen)}:last number {pen[-1]}:{pen}")
    s = e
    e *= 10
print(out)
print(pen)
print(penR)