import lib
import math
from datetime import datetime

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL


def main():
    text = []
    sum = 0
    x = 0
    y = 0
    with open('p081_matrix.txt', 'r') as file:
        str = file.read().rstrip()
        text = str.split("\n")
    for i, strin in enumerate(text):
        text[i] = strin.split(",")
    check = [[-1 for n in range(0, 80)]for n in range(0, 80)]
    while True:
        if check[y][x+1] == -1:
            print(text)
    print(check)
    return


if __name__ == '__main__':
    time = datetime.now()
    main()
    print(datetime.now() - time)
