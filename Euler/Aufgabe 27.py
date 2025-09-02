import math

import duzzelLibrary.eulerLib as euler
max_streak = -1
best = (0, 0)

for b in range(2, 1001):             # b must be prime (and positive)
    if euler.isPrim(b):
        for a in range(-999, 1000):
            n = 0
            while euler.isPrim(n*n + a*n + b):
                n += 1
            if n > max_streak:
                max_streak = n
                best = (a, b)

print(best[0]*best[1])
print(max_streak)
