
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2

        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
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

def bubbleSort(list):
    for i in range(len(list)-1, 0, -1):
        for n in range(i):
            if list[n] > list[n+1]:
                list[n], list[n+1] = list[n+1], list[n]


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


def selectionSort(list):
    for i in range(len(list)-1, 0, -1):
        max = 0
        for n in range(i):
            if list[n] > list[max]:
                max = n

        if list[max] > list[i]:
            list[max], list[i] = list[i], list[max]

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


