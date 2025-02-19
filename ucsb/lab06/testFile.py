import pytest
from Apartment import Apartment
from lab06 import mergesort, ensureSortedAscending, getBestApartment, getWorstApartment, getAffordableApartments



def test_apartment_getters_and_details():
    apt = Apartment(1204, 200, "bad")
    assert apt.getRent() == 1204
    assert apt.getMetersFromUCSB() == 200
    assert apt.getCondition() == "bad"
    expected = "(Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad"
    assert apt.getApartmentDetails() == expected


def test_apartment_comparison():
    apt1 = Apartment(950, 215, "excellent")
    apt2 = Apartment(950, 215, "average")
    apt3 = Apartment(950, 190, "excellent")

    assert apt1 < apt2
    assert apt3 < apt1

    apt4 = Apartment(950, 215, "excellent")
    assert apt1 == apt4


def test_mergesort_and_ensureSortedAscending():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert not ensureSortedAscending(apartmentList)
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList)

    expected_order = [a5, a4, a3, a2, a1, a0]
    for i in range(len(apartmentList)):
        assert apartmentList[i] == expected_order[i]


def test_getBestApartment_and_getWorstApartment():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    best = getBestApartment(apartmentList)
    worst = getWorstApartment(apartmentList)

    expected_best = "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    expected_worst = "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"
    assert best == expected_best
    assert worst == expected_worst


def test_getAffordableApartments():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(970, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    result = getAffordableApartments(apartmentList, 950)
    expected = "\n".join([
        "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad",
        "(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent",
        "(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent",
        "(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average"
    ])
    assert result == expected


def test_getAffordableApartments_empty():
    a0 = Apartment(1200, 200, "bad")
    a1 = Apartment(1300, 150, "excellent")
    apartmentList = [a0, a1]

    result = getAffordableApartments(apartmentList, 1000)
    assert result == ""


def test_empty_list_ensureSorted():
    apartmentList = []
    assert ensureSortedAscending(apartmentList) == True


def test_single_element_list():
    # single-element list is inherently sorted
    apt = Apartment(1000, 150, "excellent")
    apartmentList = [apt]
    assert ensureSortedAscending(apartmentList) == True
    mergesort(apartmentList)
    assert apartmentList[0] == apt


def test_mergesort_already_sorted():
    # already sorted list
    a0 = Apartment(500, 200, "excellent")
    a1 = Apartment(600, 250, "average")
    a2 = Apartment(700, 300, "bad")
    apartmentList = [a0, a1, a2]  # already sorted in ascending order
    assert ensureSortedAscending(apartmentList) == True
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True


def test_mergesort_reverse_sorted():
    # reverse sorted list
    a0 = Apartment(700, 300, "bad")
    a1 = Apartment(600, 250, "average")
    a2 = Apartment(500, 200, "excellent")
    apartmentList = [a0, a1, a2]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    # Expected sorted order: a2, a1, a0
    expected = [a2, a1, a0]
    for i in range(len(apartmentList)):
        assert apartmentList[i] == expected[i]


def test_duplicate_apartments():
    # same attributes
    a0 = Apartment(1000, 150, "average")
    a1 = Apartment(1000, 150, "average")
    a2 = Apartment(1000, 150, "average")
    apartmentList = [a1, a2, a0]
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    # Best and worst should be identical.
    best = getBestApartment(apartmentList)
    worst = getWorstApartment(apartmentList)
    expected = "(Apartment) Rent: $1000, Distance From UCSB: 150m, Condition: average"
    assert best == expected
    assert worst == expected


def test_boundary_values():
    # Test edge cases where rent and distance are zero.
    a0 = Apartment(0, 0, "excellent")
    a1 = Apartment(0, 100, "bad")
    a2 = Apartment(100, 0, "average")
    apartmentList = [a2, a1, a0]
    mergesort(apartmentList)
    # Expected: among a0 and a1 (both rent 0), a0 is better since distance 0 < 100;
    # then a2 (rent 100) comes last.
    expected = [a0, a1, a2]
    for i in range(len(apartmentList)):
        assert apartmentList[i] == expected[i]


def test_getAffordableApartments_boundary_budget():
    # rent genauso wie budget
    a0 = Apartment(950, 190, "excellent")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(1000, 250, "bad")
    apartmentList = [a0, a1, a2]
    # With budget exactly 950, only a0 and a1 should be returned.
    result = getAffordableApartments(apartmentList, 950)
    expected = "\n".join([
        a0.getApartmentDetails(),
        a1.getApartmentDetails()
    ])
    assert result == expected


def test_getBestWorst_single_element():
    # bei nur einem beide identisch
    apt = Apartment(800, 180, "excellent")
    apartmentList = [apt]
    best = getBestApartment(apartmentList)
    worst = getWorstApartment(apartmentList)
    expected = apt.getApartmentDetails()
    assert best == expected
    assert worst == expected


def test_apartment_comparison_edge_conditions():
    # Test nur condition
    a_ex = Apartment(1000, 200, "excellent")
    a_avg = Apartment(1000, 200, "average")
    a_bad = Apartment(1000, 200, "bad")
    assert a_ex < a_avg
    assert a_avg < a_bad
    assert a_ex < a_bad
    # Equality for same values.
    another_a_ex = Apartment(1000, 200, "excellent")
    assert a_ex == another_a_ex


def test_getAffordableApartments_no_matches():
    # Test retrun empty
    a0 = Apartment(1500, 300, "bad")
    a1 = Apartment(1600, 350, "average")
    apartmentList = [a0, a1]
    result = getAffordableApartments(apartmentList, 1000)
    assert result == ""
