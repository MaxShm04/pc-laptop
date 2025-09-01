from ucsb.mergeSort import partition


def bubbleSort(alist):
    for n in range(len(alist)-1,0,-1):
        for i in range(n):
            if alist[i] > alist[n]:
                swap(i, n)

def selectionSort(alist):
    for n in range(len(alist)-1, 0, -1):
        max = 0
        for i in range(1, n + 1):
            if alist[i] > alist[max]:
                swap(i, max)

        swap(max, alist[n])


def insertionSort(alist):
    for n in range(1, len(alist)):

        position = n
        currentvalue = alist[n]

        while position > 0 and alist[position]  < alist[position - 1]:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = currentvalue



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
            if lefthalf[i] <= righthalf[i]:
                aList[k] = lefthalf[i]
                i += 1
                k += 1
            else:
                aList[k] = lefthalf[j]
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


def quickSort(aList):
    quickSortHelper(aList, 0, len(aList) -1)


def quickSortHelper(aList, first, last):
    if first < last:

        mid = partition(aList, first, last)

        quickSortHelper(aList, 0, mid - 1)
        quickSortHelper(aList, mid + 1, last)


def partition(aList, first, last):

    pivot = aList[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        while leftmark <= rightmark and aList[leftmark] <= pivot:
            leftmark += 1

        while leftmark <= rightmark and aList[rightmark] >= pivot:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            swap(rightmark, leftmark)

    temp = aList[first]
    aList[first] = aList[rightmark]
    aList[rightmark] = temp

    return rightmark




def swap(x, y):
    return