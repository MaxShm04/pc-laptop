import lib

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL


def main(st, e):
    for n in range(st, e):
        br = False
        mark = list(str(n))
        mark.sort()
        for f in range(2, 7):
            check = list(str(n*f))
            check.sort()
            if check != mark:
                br = True
                break
        if br == False:
            return n
    return False

st = 0
e = 10000
while True:
    x = main(st, e)
    if not x:
        st, e = e, e + 10000
        print(F"Start {st}, end {e}")
    else:
        print(x)
        break
