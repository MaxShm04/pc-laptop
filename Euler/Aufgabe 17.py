
#nicht gelöst


sum = 0
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", ""]
tens = ["", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", ""]
for n in range(1000):
    if n == 0:
        print()
    elif n < 20:
        sum += len(ones[n-1])
        print(F'num {n}, add {len(ones[n-1])}')
    elif n < 100:
        s = str(n)
        sum += len(tens[int(s[0])-1])
        sum += len(ones[int(s[1])-1])
        print(F'num {n}, add {len(ones[int(s[1])-1])} + {len(tens[int(s[0])-1])}')
    else:
        s = str(n)
        sum += 7
        sum += len(ones[int(s[0]) - 1])
        print(F'num {n}, add {len(ones[int(s[0]) - 1])}')
        if int(s[1]) != 0 or int(s[2] != 0):
            sum += 3
            print(F'num {n}, add 3')
        if 20 > n - int(s[0]) > 0:
            sum += len(ones[n-int(s[0])]-1)
            print(F'num {n}, add {len(ones[n-int(s[0])]-1)}')
        else:
            sum += len(tens[int(s[1]) - 1])
            sum += len(ones[int(s[2]) -1])
            print(F'num {n}, add {len(tens[int(s[1]) - 1])} + {len(ones[int(s[2]) -1])}')


print(sum  + 11)
