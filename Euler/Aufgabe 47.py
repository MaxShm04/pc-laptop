import lib

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL


def main(st, e):
    check = []
    for n in range(st, e):
        if len(eL.list_remove_duplicates(eL.distinct_prime_factors(n))) == 4:
            if len(check) == 0:  # erster
                check.append(n)
            elif check[len(check)-1] + 1 == n:  # wenn folger
                check.append(n)
                if len(check) == 4:
                    for x in check:
                        print(x, eL.distinct_prime_factors(x), eL.list_remove_duplicates(eL.distinct_prime_factors(x)))
                    return check[0]
            else:
                check.clear()
    return False


st = 10
e = 1000
while True:
    x = main(st, e)
    if not x:
        st, e = e, e + 100
        print(F"Start {st}, end {e}")
    else:
        print(x)
        break
