a = 0
zahl = 20

while a < 20:
    zahl += 1

    a = 0
    for n in reversed(range(1, 21)):
        if zahl % n == 0:
            a += 1
            print(zahl)
        else:
            break


print("A: " + str(a))
print(zahl)

