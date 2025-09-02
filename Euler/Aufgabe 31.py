l = [1, 2, 5, 10 , 20, 50, 100, 200]
goal =[]
max = 200
count = 0

def lower(ma, ind):
    for i in range(0, ind):
        for x in range(0, int(200 / l[i])):  # for each max amount of coins of index
            m = max
            m -= l[i]
            if m <= 0:
                count += 1
                continue
            else:
                lower(m, i)

if __name__ == '__main__':
    count = 0
    for i in range(0, len(l)):  # for each index in l
        for x in range(0, int(200 / l[i])):  # for each max amount of coins of index
            m = max
            m -= l[i]
            if m <= 0:
                count += 1
                continue
            else:
                lower(m, i, count)





