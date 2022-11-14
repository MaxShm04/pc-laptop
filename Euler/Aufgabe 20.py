x = 100
sum = 0
y = 1

while x > 0:
    y *= x
    x -= 1
for n in str(y):
    sum += int(n)
print(sum)