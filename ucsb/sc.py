"""def binarySearch(intList, target):
    first = 0
    last = len(intList) -1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if intList[mid] == target:
            found = True
        else:
            if target < intList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

def recursiveBinarySearch(intList, target):
    if len(intList) == 0:
        return False
    else:
        mid = len(intList) // 2
        if intList[mid] == target:
            return True
        else:
            if target < intList[mid]:
                return recursiveBinarySearch(intList[:mid], target)
            else:
                return recursiveBinarySearch(intList[mid+1:], target)

class A(Exception):
    pass
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
def f(n):
    try:
        if n < 0:
            raise A()
        if n >= 0 and n < 5:
            raise B()x
        if n >= 5 and n < 10:
            raise C()
        if n >= 10 and n < 15:
            raise D()
        raise Exception()
    except A:
        print("A")
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
    except Exception:
        print("Exception")

f(2)

class Vehicle:
    def __init__(self, name, topSpeed):
        self.name = name
        self.topSpeed = topSpeed

    def setName(self, name):
        self.name = name

    def setTopSpeed(self, topSpeed):
        self.topSpeed = topSpeed

    def getName(self):
        return self.name
    def getTopSpeed(self):
        return self.topSpeed
    def getInfo(self):
        return "Name: {}, Top Speed: {} mph".format(self.name, self.topSpeed)


class Plane(Vehicle):
    def __init__(self, name, topSpeed, altitude):
        super().__init__(name, topSpeed)
        self.altitude = a   ltitude

    def getInfo(self):
        return super().getInfo() + ", Altitude: {} ft".format(self.altitude)

    def __lt__(self, rhs):
        return self.altitude < rhs.altitude


p1 = Plane("Dreamliner", 594, 33000)
p2 = Plane("900LX", 667, 38000)
assert p1.getInfo() == "Name: Dreamliner, Top Speed: 594 mph, Altitude: 33000 ft"
assert p2.getInfo() == "Name: 900LX, Top Speed: 667 mph, Altitude: 38000 ft"
assert (p1 < p2) == True
assert (p2 < p1) == False

"""
def findNum(num, intList):
    if len(intList)== 0:
        return False
    else:
        mid = len(intList) // 2
        if intList[mid] == num:
            return True
        else:
            if num < mid:
                return findNum(num, intList[:mid])
            else:
                return findNum(num, intList[mid+1:])



def findList(num, intList):
    if len(intList) == 0:
        return False
    else:
        if intList[0] == num:
            return True
        else:
            return findList(num, intList[1:])

def test(lista):
    a = lista
    a = []
    return a

lista = [1,2,3,4]
print(test(lista))
print(lista)

