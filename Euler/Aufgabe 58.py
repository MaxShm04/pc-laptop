import lib
import math
from datetime import datetime

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL

def main(st, en, matr, diags):
    for n in range(st, en, 2):
        matr = eL.create_spiral_matrix_rt_add_ring(matr, 1)
        #matr = eL.create_spiral_matrix_rt(n)
        diags = eL.get_diagonals_of_matrix(matr, diags)
        #diags = eL.get_diagonals_of_matrix(matr)
        out = [n for n in diags if eL.isPrim(n)]
        if len(out)/len(diags)<0.1:
            print(out)
            return True
    return matr, diags

if __name__ == '__main__':
    time = datetime.now()
    st = 5
    en = 100
    time2 = datetime.now()
    matr = eL.create_spiral_matrix_rt(3)
    diags = eL.get_diagonals_of_matrix(matr)
    while True:
        x = main(st, en, matr, diags)
        if x == True:
            break
        matr = x[0]
        diags = x[1]
        print(en, time2 - datetime.now())
        time2 = datetime.now()
        st = en
        en += 100
    print(time - datetime.now())


