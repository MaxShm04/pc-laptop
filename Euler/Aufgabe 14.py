time = datetime.now()
start = 13
count = 0
x = start
maxC = 0
maxN = 0

while start < 1000000:
    if x == 1:
        print(F'{start}, {maxC}')
        if maxC < count:
            maxC = count
            maxN = start
        start += 1
        x = start
        count = 0
    else:
        count += 1
        if x % 2 == 0:
            x = x / 2
            #print("x/2")
        else:
            x = 3 * x + 1
            #print("3x+1")

print(maxC+1)
print(maxN)
print(time - datetime.now())
