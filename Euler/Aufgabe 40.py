import eulerLib as eL

nmb = "0."
i = 0
d = 1
out = 1
while len(nmb)-2 < 1000000:
    i += 1
    nmb += str(i)
    #print(nmb)
i = 1
for n in nmb:
    if i % d == 0:
        out *= int(nmb[i+1])
        #print(nmb[d+1])
        #print(i)
        d *= 10
    i += 1

print(out)