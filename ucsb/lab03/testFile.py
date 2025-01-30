import pytest

from lab03 import integerDivision, collectEvenInts, countVowels, reverseString, removeSubString

def test_integerDivision():
    assert integerDivision(50, 7) == 7
    assert integerDivision(9, 2) == 4
    assert integerDivision(100, 15) == 6
    assert integerDivision(20, 5) == 4
    assert integerDivision(1, 1) == 1

def test_collectEvenInts():
    assert collectEvenInts([10, 21, 32, 43]) == [10, 32]
    assert collectEvenInts([7, 11, 13]) == []
    assert collectEvenInts([4, 8, 12, 16]) == [4, 8, 12, 16]
    assert collectEvenInts([5, 7, 9]) == []
    assert collectEvenInts([14, 19, 22, 29, 36]) == [14, 22, 36]

def test_countVowels():
    assert countVowels("Recursion is fun!") == 6
    assert countVowels("Why Python?") == 1
    assert countVowels("AEIOUxyz") == 5
    assert countVowels("abcdXYZ") == 1
    assert countVowels("zzzzz") == 0

def test_reverseString():
    assert reverseString("Python") == "nohtyP"
    assert reverseString("Recursion") == "noisruceR"
    assert reverseString("") == ""
    assert reverseString("A") == "A"
    assert reverseString("Data") == "ataD"

def test_removeSubString():
    assert removeSubString("hellohellohello", "hello") == ""
    assert removeSubString("abcabcabc", "bca") == "abc"
    assert removeSubString("testtesttest", "test") == ""
    assert removeSubString("aaabbbccc", "bbb") == "aaaccc"
    assert removeSubString("123123", "23") == "11"
