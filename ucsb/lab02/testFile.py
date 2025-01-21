import pytest
from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

# Tests for Beverage class
def test_beverage_initialization():
    b1 = Beverage(16, 20.5)
    assert b1.getOunces() == 16
    assert b1.getPrice() == 20.5

def test_beverage_update_methods():
    b1 = Beverage(12, 15.0)
    b1.updateOunces(20)
    b1.updatePrice(25.0)
    assert b1.getOunces() == 20
    assert b1.getPrice() == 25.0

def test_beverage_getInfo():
    b1 = Beverage(16, 20.5)
    assert b1.getInfo() == "16 oz, $20.50"

# Tests for Coffee class
def test_coffee_initialization():
    c1 = Coffee(8, 3.0, "Espresso")
    assert c1.getOunces() == 8
    assert c1.getPrice() == 3.0

def test_coffee_getInfo():
    c1 = Coffee(8, 3.0, "Espresso")
    assert c1.getInfo() == "Espresso Coffee, 8 oz, $3.00"

# Tests for FruitJuice class
def test_fruitjuice_initialization():
    juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
    assert juice.getOunces() == 16
    assert juice.getPrice() == 4.5

def test_fruitjuice_getInfo():
    juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
    assert juice.getInfo() == "Apple/Guava Juice, 16 oz, $4.50"

# Tests for DrinkOrder class
def test_drinkorder_initialization():
    order = DrinkOrder()
    assert len(order.drinks) == 0

def test_drinkorder_addBeverage():
    order = DrinkOrder()
    c1 = Coffee(8, 3.0, "Espresso")
    juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
    order.addBeverage(c1)
    order.addBeverage(juice)
    assert len(order.drinks) == 2

def test_drinkorder_getTotalOrder():
    c1 = Coffee(8, 3.0, "Espresso")
    juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
    order = DrinkOrder()
    order.addBeverage(c1)
    order.addBeverage(juice)
    assert order.getTotalOrder() == (
        "Order Items:\n"
        "* Espresso Coffee, 8 oz, $3.00\n"
        "* Apple/Guava Juice, 16 oz, $4.50\n"
        "Total Price: $7.50"
    )

def test_drinkorder_empty_order():
    order = DrinkOrder()
    assert order.getTotalOrder() == (
        "Order Items:\n"
        "Total Price: $0.00"
    )

