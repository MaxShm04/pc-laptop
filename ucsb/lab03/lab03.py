def integerDivision(n, k):
    if n < k:
        return 0
    return 1 + integerDivision(n - k, k)


def collectEvenInts(listOfInt):
    if not listOfInt:
        return []
    if listOfInt[0] % 2 == 0:
        return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
    else:
        return collectEvenInts(listOfInt[1:])

def countVowels(someString):
    if not someString:
        return 0
    return (1 if someString[0] in 'AEIOUaeiou' else 0) + countVowels(someString[1:])
    
def reverseString(s):
    if s == "":
        return s
    return reverseString(s[1:]) + s[0]

def removeSubString(s, sub):
    if sub not in s:
        return s
    else:
        index = s.find(sub)
        s = s[:index] + s[index + len(sub):]
        return removeSubString(s, sub)



