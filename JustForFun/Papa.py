import math

x = True
i4 = -130319
i5 = 23389
while(True):
    print(f"Bitte alles in Mikrometern eingeben, keine Kommazahlen \nzum Abbruch -1 eingeben \nUm die Maaße zu ändern, -2 eingeben \nAktuell: D1 = {i4*-1}, D2 {i5}")
    i1 = float(input("R1: "))
    if i1 == -1:
        exit()
    if i1 == -2:
        i4 = int(input("Distanz1: "))*-1
        i5 = int(input("Distanz2: "))
        i1 = float(input("R1: "))
    i2 = float(input("R2: "))           # 300, 50
    i3 = float(input("0-180: "))

    p1 = [i4, i1, 0] #mikrometer


    x = round(i2 * math.cos(i3 * math.pi / 180), 8)
    y = round(i2 * math.sin(i3 * math.pi / 180), 8)

    p2 = [i5, x, y]

    pM = [0,0,0]

    x1 = p1
    x2 = [p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2]] # v1 + lambda * v2

    # d = abs((pM - x1) x x2) / abs(x2)

    t1 = [pM[0]-x1[0], pM[1]-x1[1], pM[2]-x1[2]] #pM - x1
    t2 = [t1[1]*x2[2] - t1[2]*x2[1], t1[2]*x2[0] - t1[0]*x2[2], t1[0]*x2[1] - t1[1]*x2[0]]#t1 x x2
    t3 = math.sqrt(t2[0]*t2[0] + t2[1]*t2[1] + t2[2]*t2[2])
    t4 = math.sqrt(x2[0]*x2[0] + x2[1]*x2[1] + x2[2]*x2[2])
    t5 = t3/t4

    print(t5/1000)
    print("-"*25)
