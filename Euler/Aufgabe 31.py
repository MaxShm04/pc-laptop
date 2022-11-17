
pos = []

maxP = 200
c = 0
for n in range(0, int(maxP+1)):
    for m in range(0, int((maxP/2)+1)):
        for b in range(0, int((maxP / 5) + 1)):
            for v in range(0, int((maxP / 10) + 1)):
                for c in range(0, int((maxP / 20) + 1)):
                    for x in range(0, int((maxP / 50) + 1)):
                        for y in range(0, int((maxP / 100) + 1)):
                            for g in range(0, int((maxP / 200) + 1)):
                                amount = n*1 + m*2 + b*5 + v*10 + c*20 + x*50+ y*100+ g*200
                                if amount == 200:
                                    c += 1
                                    pos.append([n, m, b, v, c, x, y, g])
                                    if(c==10):
                                        c=0
                                        print([n, m, b, v, c, x, y, g])
print(pos)
print(len(pos))
