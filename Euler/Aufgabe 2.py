int2 = 2
ges = 0

while int1 < 4000000 :
    x = int2
    int2 = int1 + int2
    if int1 % 2 == 0:
        ges += int1
        print(F'+ {int1}')
    int1 = x
print(ges)
