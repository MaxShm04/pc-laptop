import math



import eulerLib as eL

matr =[[1]]
size = 1
posX = 0
posY = 0
dir = ""
add = 0
for n in range(2, 10):
    add = (size-1)/2
    if n > math.pow(size, 2):
        size+=2
        for i in matr:
            i.insert(0, None)
            i.append(None)
        matr.insert(0, eL.emptyList(size))
        matr.append(eL.emptyList(size))
        print(matr)
        posX +=1
        matr[posY+add[posX+add]]=n
        dir = "south"
        print(matr)
        continue
    if posX > 0 and abs(posX)*2+1 == size:                 #rechts unten
        if posY < 0 and abs(posY)*2+1 == size:
            dir = "west"
    if posX < 0 and abs(posX)*2+1 == size:                 #links unten
        if posY < 0 and abs(posY) * 2 + 1 == size:
            dir = "north"
    if posX < 0 and abs(posX) * 2 + 1 == size:             #links oben
        if posY > 0 and abs(posY) * 2 + 1 == size:
            dir = "east"
    if dir == "south":
        posY -= 1
        matr[posY+add[posX+add]] = n
        print(matr)
    if dir == "west":
        posX -= 1
        matr[posY+add[posX+add]] = n
        print(matr)
    if dir == "north":
        posY += 1
        matr[posY+add[posX+add]] = n
        print(matr)
    if dir == "east":
        posX += 1
        matr[posY+add[posX+add]] = n
        print(matr)

    print(matr)


