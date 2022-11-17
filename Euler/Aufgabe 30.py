import math

ges = []

for n in range(0, 100):
    print(n)
    for m in range(0, 100):
        for i in range(0, 100):
            for q in range(0, 100):
                for s in range(0, 100):
                    amount = math.pow(n, 5) + math.pow(m, 5) + math.pow(i, 5) + math.pow(q, 5) + math.pow(s, 5)
                    #print(F"{n}{m}{i}{q}{s}, {amount}")
                    if str(int(amount)) == F"{n}{m}{i}{q}{s}":
                        ges.append(amount)
                        print(amount)

print(ges)
am = 0
for n in ges:
    am += n
print(am)