from datetime import datetime
x = 0
y = 0           #irr
countG = 0
count = 0

time = datetime.now()

while countG <=500:
    if countG == 500:
        break
    count = 1
    for n in range(1, round(x/2)+2):
        if x % n == 0:
            count += 1
            #print(F"{x} / {n} = 0, new count is {count}")
    if count > countG:      #vergleich zum höhersetzen
        #print(F"{count} > {countG}, countG bei {n} ist {count}")
        countG = count
    y += 1
    x += y
    print(x, str(countG))
print(x-y)
print(time-datetime.now())