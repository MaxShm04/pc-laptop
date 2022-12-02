import math

ges = []

for a in range(2, 101):
    for b in range(2, 101):
        if not math.pow(a, b) in ges:
            ges.append(math.pow(a, b))


print(len(ges))