ges = 0

def d(n):
    sum = 0
    for x in range(1, n):
        if n%x == 0:
            sum += x
    return sum


for a in range (1, 10000):
    print(a, ges)
    b = d(a)
    if d(b) == a and a!=b:
        ges += b
        ges += a
print(ges/2)