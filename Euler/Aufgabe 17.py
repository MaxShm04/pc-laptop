

t = 0
sum = 11
ones = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3] #one two three four five six seven eight nine ten
tentwenty = ["", 6, 6, 8, 8, 7, 7, 9, 8, 8] #11-19 eleven
tens = [6, 6, 5, 5, 5, 7, 6, 6] #20-90 in tens
for i in range(1,1000):
    print(f"T: {t}")
    t = 0
    print(i)
    if i >= 100:
        sum += ones[(i // 100)-1]
        t += ones[(i // 100)-1]
        t += 7
        sum += 7
        i -= (i//100)*100
        if (i%100) == 0:
            continue
        else:
            sum += 3
            t += 3
    if i >= 20:
        sum += tens[(i//10)-2]
        t += tens[(i//10)-2]
        if (i%10) == 0:
            continue
    elif 10 < i < 20:
        sum += tentwenty[i - 10]
        t += tentwenty[i - 10]
        continue
    sum += ones[(i%10)-1]
    t += ones[(i%10)-1]
#nine hundred and ninty eight
#4 7 3 5 5

print(sum)


