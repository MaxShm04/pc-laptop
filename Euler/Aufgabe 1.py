import lib
import math
import random
from datetime import datetime

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL




def main():
    list = [random.randint(1, 200) for n in range(100)]
    list = [13, 45, 79, 60, 90, 42, 195, 16, 38, 11, 27, 96, 144, 129, 99, 131, 99, 119, 81, 20, 15, 64, 68, 24, 114, 110, 8, 134, 80, 150, 167, 35, 83, 43, 111, 96, 197, 191, 70, 112, 91, 22, 19, 99, 1, 76, 165, 12, 163, 79, 168, 110, 111, 18, 64, 135, 58, 23, 170, 85, 124, 65, 86, 17, 18, 136, 140, 79, 117, 17, 143, 26, 171, 119, 25, 117, 155, 89, 82, 77, 66, 31, 81, 61, 165, 170, 81, 184, 86, 180, 109, 147, 110, 152, 144, 142, 141, 114, 146, 180]
    med = len(list)/2
    l = list[med:]
    r = list[:med]
    sortL(l, r, med)
    print(list)


def sortL(l, r, m):
    for n in l:
        if n > m:
           l.remove(n)
           r.append(n)
    for n in r:
        if n < m:
           r.remove(n)
           l.append(n)


if __name__ == '__main__':
    time = datetime.now()
    main()
    print(datetime.now() - time)
