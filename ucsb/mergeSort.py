from pkgutil import resolve_name


def mergeSort(aList):
    if len(aList) > 1:
        mid = len(aList) // 2

        lefthalf = aList[:mid]
        righthalf = aList[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                aList[k] = lefthalf[i]
                i += 1
                k += 1
            else:
                aList[k] = righthalf[j]
                j += 1
                k += 1

        while i < len(lefthalf):
            aList[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            aList[k] = righthalf[j]
            j += 1
            k += 1




def test_mergeSort():
   numList1 = [9,8,7,6,5,4,3,2,1]
   numList2 = [1,2,3,4,5,6,7,8,9]
   numList3 = []
   numList4 = [1,9,2,8,3,7,4,6,5]
   numList5 = [5,4,6,3,7,2,8,1,9]
   mergeSort(numList1)
   mergeSort(numList2)
   mergeSort(numList3)
   mergeSort(numList4)
   mergeSort(numList5)

   assert numList1 == [1,2,3,4,5,6,7,8,9]
   assert numList2 == [1,2,3,4,5,6,7,8,9]
   assert numList3 == []
   assert numList4 == [1,2,3,4,5,6,7,8,9]
   assert numList5 == [1,2,3,4,5,6,7,8,9]


def quickSort(aList):
    quickSortHelper(aList, 0, len(aList)-1)

def quickSortHelper(aList, first, last):
    if first < last:
        splitpoint = partition(aList, first, last)

        quickSortHelper(aList, first, splitpoint-1)
        quickSortHelper(aList, splitpoint+1, last)


def partition(aList, first, last):
    pivotvalue = aList[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        while leftmark <= rightmark and aList[leftmark] < pivotvalue:
            leftmark += 1

        while leftmark <= rightmark and aList[rightmark] > pivotvalue:
            rightmark -= 1

        if rightmark < leftmark:
            done = True

        else:
            aList[leftmark], aList[rightmark] = aList[rightmark], aList[leftmark]

    return rightmark





def bubbleSort(aList):
    for n in range(len(aList)-1, 0, -1):
        for i in range(n):
            if aList[i] > aList[i+1]:
                aList[i], aList[i+1] = aList[i+1], aList[i]

# Bubble sort pytest
def test_bubbleSort():
    list1 = [1,2,3,4,5,6]
    list2 = [2,2,2,2,2,2]
    list3 = []
    list4 = [6,7,5,3,1]
    bubbleSort(list1)
    assert list1 == [1,2,3,4,5,6]
    bubbleSort(list2)
    assert list2 == [2,2,2,2,2,2]
    bubbleSort(list3)
    assert list3 == []
    bubbleSort(list4)
    assert list4 == [1,3,5,6,7]


def selectionSort(aList):
    for n in range(len(aList)-1, 0, -1):
        max = 0
        for i in range(1, n +1):
            if aList[i] > aList[max]:
                max = i
        aList[n], aList[max] = aList[max], aList[n]



def test_selectionSort():
    list1 = [1,2,3,4,5,6]
    list2 = [2,2,2,2,2,2]
    list3 = []
    list4 = [6,7,5,3,1]
    selectionSort(list1)
    assert list1 == [1,2,3,4,5,6]
    selectionSort(list2)
    assert list2 == [2,2,2,2,2,2]
    selectionSort(list3)
    assert list3 == []
    selectionSort(list4)
    assert list4 == [1,3,5,6,7]


def insertionSort(aList):
    for n in range(1, len(aList)):

        value = aList[n]
        position = n

        while n > 0 and aList[position -1 ] > aList[position]:
            aList[position] = aList[position -1]
            position -= 1

        aList[position] = value

def test_insertionSort():
    list1 = [1,2,3,4,5,6]
    list2 = [2,2,2,2,2,2]
    list3 = []
    list4 = [6,7,5,3,1]
    insertionSort(list1)
    assert list1 == [1,2,3,4,5,6]
    insertionSort(list2)
    assert list2 == [2,2,2,2,2,2]
    insertionSort(list3)
    assert list3 == []
    insertionSort(list4)
    assert list4 == [1,3,5,6,7]


def binarySearchWhile(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if alist[mid] == item:
            found = True
            return found

        if item < alist[mid]:
            last = mid -1
        else:
            first = mid + 1
    return found

def binarySearch(alist,item):
    if len(alist) == 0:
        return False

    mid = len(alist) // 2

    if alist[mid] == item:
        return True

    if alist[mid] > item:
        return binarySearch(alist[:mid], item)
    else:
        return binarySearch(alist[mid+1:], item)



def test_binarySearchNormal():
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 5) == True
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], -1) == False
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 11) == False
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 1) == True
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 10) == True

def test_binarSearchDuplicates():
    assert binarySearch([-10,-5,0,1,1,4,4,7,8], 0) == True
    assert binarySearch([-10,-5,0,1,1,4,4,7,8], 2) == False
    assert binarySearch([-10,-5,0,1,1,4,4,7,8], 4) == True
    assert binarySearch([-10,-5,0,1,1,4,4,7,8], 2) == False

def test_binarySearchEmptyList():
    assert binarySearch([], 0) == False

def test_binarySearchSameValues():
    assert binarySearch([5,5,5,5,5,5,5,5,5,5,5], 5) == True
    assert binarySearch([5,5,5,5,5,5,5,5,5,5,5], 0) == False



def countOddDigits(s):
    x = ["1","3","5","7","9"]
    if len(s) > 1:
        if s[0] in x:
            return countOddDigits(s[1:]) + 1
        else:
            return countOddDigits(s[1:])
    elif len(s) == 1 and s[0] in x:
        return 1
    else:
        return 0

def testOdds():
    assert countOddDigits("") == 0
    assert countOddDigits("A") == 0
    assert countOddDigits("A1B3") == 2
    assert countOddDigits("123456") == 3


def isPalindrome(deque):
    if isEmpty(deque) or size(deque) == 1:
        return True

    if removeFront(deque) == removeRear(deque):
        return isPalindrome(deque)
    else:
        return False

def isEmpty(l):
    if len(l) == 0:
        return True
    return False

def size(l):
    return len(l)

def removeFront(l):
    return l.pop(0)

def removeRear(l):
    return l.pop()

def addFront(str, l):
    l.insert(0,str)

def addRear(str, l):
    l.append(str)

def test_isPalindrome():
    d0 = []
    addFront("A", d0)
    assert isPalindrome(d0)==True
    d1 = []
    addRear("A", d1)
    addRear("B", d1)
    addRear("A", d1)
    assert isPalindrome(d1)==True
    d2 = []
    addRear("X",d2)
    addRear("Y",d2)
    assert isPalindrome(d2)==False



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, newNext):
        self.next = newNext

class LinkedList:
    def __init__(self):
        self.head = None
    def addToFront(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def collectEvens(self, node):
        even = [2,4,6,8]
        if not node:
            return []

        if node.data in even:
            if node.next:
                return [node.data] + self.collectEvens(node.next)
            return [node.data]
        if node.next:
            return self.collectEvens(node.next)
        return []

# pytest
def test_collectEvens():
    ll = LinkedList()
    assert ll.collectEvens(ll.head) == []
    ll.addToFront(6)
    assert ll.collectEvens(ll.head) == [6]
    ll.addToFront(1)
    ll.addToFront(3)
    assert ll.collectEvens(ll.head) == [6]
    ll.addToFront(1)
    ll.addToFront(2)
    ll.addToFront(3)
    ll.addToFront(4)
    assert ll.collectEvens(ll.head) == [4,2,6]


