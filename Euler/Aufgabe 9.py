a = 0
b = 0
c = 0

for x in range(0, 1000):
    for y in range(x, 1000):
        for z in range(y, 1000):
            if x + y + z == 1000 and x.__pow__(2) + y.__pow__(2) == z.__pow__(2):
                a = x
                b = y
                c = z
print(a*b*c)
