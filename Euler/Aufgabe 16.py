time = datetime.now()

x = pow(2, 1000)
sum = 0
for n in str(x):
    sum += int(n)
print(sum)
print(time - datetime.now())
