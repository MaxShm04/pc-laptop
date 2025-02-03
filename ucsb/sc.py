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
"""

class A(Exception):
	pass

class B(A): # B inherits from A (B IS-A A type)
	pass

class C(Exception):
	pass

try:
	x = int(input("Enter a positive number: "))
	if x < 0:
		raise C() # Change this to A() and C() and observe...
except C:
	print("Exception of type C caught")
except A:
	print("Exception of type A caught")
except B:
	print("Exception of type B caught") # Will never get called
except Exception:
	print("Exception of type Exception caught")

print("Resuming execution")