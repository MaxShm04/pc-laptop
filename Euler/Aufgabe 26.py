numb = 0
count = 0
for n in range(1, 1000):
    br = True
    l = []
    c = 0
    i = 1
    while br:
        print(l)
        if i in l:
            if c > count:
                count = c
                numb = n
                br = False
                break
            else:
                br = False
                break
        l.append(i)
        i = (i*10) % n
        c += 1
        print(f"¨NI:{i}")

print(f"largest Nubmer:{numb}")