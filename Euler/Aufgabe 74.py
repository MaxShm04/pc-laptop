import lib
import math
from datetime import datetime

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL


def main():
    max = []
    for n in range(1, 1000_000):
        if n % 100_000 == 0:
            print(n)
        summ = 0
        check = []
        c = 0
        check.append(n)
        for l in str(n):
            c += math.factorial(int(l))
        check.append(c)
        while True:
            c = 0
            for l in str(check[-1]):
                c += math.factorial(int(l))
            if c in check:
                break
            else:
                check.append(c)
        #print(F"chekc: {check}")
        if len(check) == 60:
            max.append(n)
    print(max)
    print(len(max))
    return


if __name__ == '__main__':
    time = datetime.now()
    main()
    print(datetime.now() - time)
