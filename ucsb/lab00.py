
def areElementsInList(list1, list2):
    for elem in list1:
        if elem not in list2:
            return False
    return True

assert areElementsInList(["one",2], [0,"one",2,"three"]) == True
assert areElementsInList([],[1,2,3,4]) == True
assert areElementsInList([1,2,3],[1,2]) == False
assert areElementsInList([1,2,3],[3,2,1]) == True


def alternateCase(s):
    result = []

    for char in s:
        if char.isupper():
            result.append(char.lower())
        else:
            result.append(char.upper())

    return ''.join(result)


assert alternateCase("") == ""
assert alternateCase("This is a Sentence") == "tHIS IS A sENTENCE"
assert alternateCase("CS9") == "cs9"
assert alternateCase("9.95") == "9.95"

def getCharacterCount(s):
    result = {}
    for char in s:
        if char.isalpha():
            key = char.upper()
        else:
            key = char
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result


x = getCharacterCount("This is a Sentence")
assert x.get("S") == 3
assert x.get("P") == None
assert x.get("I") == 2
assert x.get(" ") == 3

y = getCharacterCount("Pi is Approximately 3.14159")
assert y.get("1") == 2
assert y.get("A") == 2
assert y.get("P") == 3
assert y.get(".") == 1
assert y.get(4) == None