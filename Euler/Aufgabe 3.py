n = 600851475143
i = 0
prim = 2

while n!=1:
    if n % prim == 0:
        n = n / prim
    else:
        prim +=1

print(prim)
