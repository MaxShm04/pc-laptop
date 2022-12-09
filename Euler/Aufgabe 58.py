import lib
import math

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL


def printMatr(matr):
    for yL in matr:
        print(yL)
    print("------")
    return




matr = eL.create_spiral_matrix_rb(7)
printMatr(matr)
print(eL.calc_diagonals_of_matrix(matr))