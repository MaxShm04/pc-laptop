c = 0
numbers = [False] * 10
zif = [False] * 10
allNum = []

for q in range(0, 10):
    zif[q] = True
    for w in range(0, 10):
        if not zif[w]:
            zif[w] = True
            for e in range(0, 10):
                if not zif[e]:
                    zif[e] = True
                    for r in range(0, 10):
                        if not zif[r]:
                            zif[r] = True
                            for t in range(0, 10):
                                if not zif[t]:
                                    zif[t] = True
                                    for z in range(0, 10):
                                        if not zif[z]:
                                            zif[z] = True
                                            for u in range(0, 10):
                                                if not zif[u]:
                                                    zif[u] = True
                                                    for i in range(0, 10):
                                                        if not zif[i]:
                                                            zif[i] = True
                                                            for o in range(0, 10):
                                                                if not zif[o]:
                                                                    zif[o] = True
                                                                    for p in range(0, 10):
                                                                        if not zif[p]:
                                                                            allNum.append(int(F'{q}{w}{e}{r}{t}{z}{u}{i}{o}{p}'))
                                                                    zif[o] = False
                                                            zif[i] = False
                                                    zif[u] = False
                                            zif[z] = False
                                    zif[t] = False
                            zif[r] = False
                    zif[e] = False
            zif[w] = False
    zif[q] = False
print(allNum[999999])
