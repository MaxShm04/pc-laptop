count = 1
nmb = 1
curPrim = 1
i = True

while count != 10001:
    nmb +=1
    for n in range(2, nmb):
        if(nmb % n == 0):
            i = True
            #print("break")
            break
        else:
            i = False
    if i == False:
        count += 1
        print("Prim: " + str(nmb))
    #print(nmb)
