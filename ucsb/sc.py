'''
x = [2,2] * 2
x = [2,4,6,8][2:4]
x = not 3 in [1,3,5]

x = [5,4,3,2,1].pop()
x = [5,4,3,2,1].pop(2)
x = [5,4,3,2,1].index(2)
#print([5,4,3,2,1].remove(4))
x = list(range(4))
x = list(range(-2,4,2))
x = list(range(10,5,-2))
x = list(range(2,5))


a = "cs9"
b = "UCSB"
c = "Python"

x = c.upper()
x = b.split("C")
x = a.find("9")



#print(x)


def countOdds(numbers):
    count = 0

    for num in numbers:
        if num % 2 != 0:
            count += 1

    return count

assert countOdds([1,2,3]) == 2
assert countOdds([]) == 0
assert countOdds([3,3,5]) == 3
assert countOdds([2,4,6,7,8,9]) == 2

'''

cs9 = "CS9"
try:
    for s in cs9:
        x = len(cs9) + s
    print("DONE LOOPING")
except:
    print("EXCEPTION CAUGHT")