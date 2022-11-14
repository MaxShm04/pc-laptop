prim = 1
ges = 0
nmb = 1
st = False
anz = 0

while(prim < 2000000):
    nmb += 1
    for n in range(2, nmb):
        if nmb % n == 0:
            st = False
            #print("N " + str(n))
            break
        else:
            st = True
    if st == True:
        print("Prim: " + str(nmb))
        prim = nmb
        ges += nmb
        anz += 1
ges -= nmb
print("Gesamt: " + str(ges+2))
print(anz)
