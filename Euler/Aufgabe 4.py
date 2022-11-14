max = 0

for i in range(0, 999):
    for x in range(0, 999):
        z :str = str(x*i)
        if len(z)==6 and z[0] == z[5] and z[1]==z[4] and z[2]==z[3]:
                if max < int(z):
                    max = int(z)
print(max)