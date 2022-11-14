sum1 = 0
sum2 = 0

for n in range(1, 101):
    sum1 += n.__pow__(2)
for n in range(1, 101):
    sum2 += n
sum2 = sum2.__pow__(2)
print(sum2 - sum1)