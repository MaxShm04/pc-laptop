x = 1
y = 2
count = 3

while len(str(y)) < 1000:
    count += 1
    z = x+y
    x = y
    y = z
print(count)
