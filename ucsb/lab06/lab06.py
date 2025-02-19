from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        left = apartmentList[:mid]
        right = apartmentList[mid:]

        mergesort(left)
        mergesort(right)

        # 2hälften mergen
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                apartmentList[k] = left[i]
                i += 1
            else:
                apartmentList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            apartmentList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            apartmentList[k] = right[j]
            j += 1
            k += 1

def ensureSortedAscending(apartmentList):
    for i in range(1, len(apartmentList)):
        if apartmentList[i - 1] > apartmentList[i]:
            return False
    return True

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[-1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    mergesort(apartmentList)
    affordable = [apt for apt in apartmentList if apt.getRent() <= budget]
    return "\n".join([apt.getApartmentDetails() for apt in affordable])
