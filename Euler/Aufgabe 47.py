import lib

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL


def main(st, e):
    check = []
    prims = [0]
    for n in range(st, e):
        prims += eL.givePrimes(n, start=prims[-1])
        if len(eL.list_remove_duplicates(eL.distinct_prime_factors(n, prims=prims))) == 4:
            if len(check) == 0:  # erster
                check.append(n)
            elif check[len(check)-1] + 1 == n:  # wenn folger
                check.append(n)
                if len(check) == 4:
                    for x in check:
                        print(x, eL.distinct_prime_factors(x), eL.list_remove_duplicates(eL.distinct_prime_factors(x, prims=prims)))
                    return check[0]
            else:
                check.clear()
    return False


st = 134000
e = 135000
while True:
    x = main(st, e)
    if not x:
        st, e = e, e + 1000
        print(F"Start {st}, end {e}")
    else:
        print(x)
        break
