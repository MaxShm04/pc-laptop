import math
import eulerLib as eL


def printMatr(matr):
    for yL in matr:
        print(yL)
    print("------")
    return

matr =[[1]]
size = 1
posX = 0
posY = 0
dir = ""
add = 0
n = 1
maxS = 1001
while True:
    n += 1
    add = (size-1)/2
    if n > math.pow(size, 2):
        size+=2
        if size > maxS:
            size -= 2
            break
        for i in matr:
            i.insert(0, 0)
            i.append(0)
        matr.insert(0, eL.emptyList(size))
        matr.append(eL.emptyList(size))
        #printMatr(matr)
        add = (size - 1) / 2
        #print(add)
        posX +=1
        matr[int(posY+add)][int(posX+add)] = n
        dir = "south"
        #printMatr(matr)
        continue
    if posX > 0 and abs(posX)*2+1 == size:                 #rechts unten
        if posY > 0 and abs(posY)*2+1 == size:
            dir = "west"
    if posX < 0 and abs(posX)*2+1 == size:                 #links unten
        if posY > 0 and abs(posY) * 2 + 1 == size:
            dir = "north"
    if posX < 0 and abs(posX) * 2 + 1 == size:             #links oben
        if posY < 0 and abs(posY) * 2 + 1 == size:
            dir = "east"
    if dir == "south":
        posY += 1
        matr[int(posY+add)][int(posX+add)] = n
        #printMatr(matr)
    if dir == "west":
        posX -= 1
        matr[int(posY+add)][int(posX+add)] = n
        #printMatr(matr)
    if dir == "north":
        posY -= 1
        matr[int(posY+add)][int(posX+add)] = n
        #printMatr(matr)
    if dir == "east":
        posX += 1
        matr[int(posY+add)][int(posX+add)] = n
        #printMatr(matr)


# calc diagonals
amount = 1
for n in range(0, int((size-1)/2)):
    amount += matr[n][n]
    print(F"+ {matr[n][n]}")
    amount += matr[(-1*n)-1][n]
    print(F"+ {matr[(-1*n)-1][n]}")
    amount += matr[n][(-1*n)-1]
    print(F"+ {matr[n][(-1*n)-1]}")
    amount += matr[(-1*n)-1][(-1*n)-1]
    print(F"+ {matr[(-1*n)-1][(-1*n)-1]}")
    print("------")




printMatr(matr)
print(amount)


