import lib
import math
from datetime import datetime

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL


def main():
    ter = 1.45
    ausgabe = 3.75
    rate = 40
    dauer = 7
    normal = 0
    mitkosten = 0
    pa = 8
    print(f"gespart: {12*rate*dauer}")
    for i in range(dauer):
        normal += 12*rate
        normal *= 1+pa/100
        normal -= normal*ter/100
    print(f"normal: {normal:.2f}")
    for i in range(dauer):
        mitkosten += (12 * (rate-rate*ausgabe/100))
        mitkosten *= 1 + pa / 100
        mitkosten -= (normal * (ter / 100))
    print(f"mitkosten: {mitkosten:.2f}")
    print(F"{normal-mitkosten:.2f}")

if __name__ == '__main__':
    time = datetime.now()
    main()
    print(datetime.now() - time)
