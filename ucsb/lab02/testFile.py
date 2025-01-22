import pytest
from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder


#Beverage
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

def test_beverage_invalid_updates():
    b1 = Beverage(10, 5.0)
    with pytest.raises(ValueError):
        b1.updateOunces(-5)
    with pytest.raises(ValueError):
        b1.updatePrice(-10.0)

def test_beverage_getInfo():
    b1 = Beverage(16, 20.5)
    assert b1.getInfo() == "16 oz, $20.50"

#Coffee
def test_coffee_initialization():
    c1 = Coffee(8, 3.0, "Espresso")
    assert c1.getOunces() == 8
    assert c1.getPrice() == 3.0
    assert c1.getInfo() == "Espresso Coffee, 8 oz, $3.00"

def test_coffee_different_styles():
    c1 = Coffee(12, 5.5, "Cappuccino")
    c2 = Coffee(16, 4.0, "Americano")
    assert c1.getInfo() == "Cappuccino Coffee, 12 oz, $5.50"
    assert c2.getInfo() == "Americano Coffee, 16 oz, $4.00"

#FruitJuice
def test_fruitjuice_initialization():
    juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
    assert juice.getOunces() == 16
    assert juice.getPrice() == 4.5
    assert juice.getInfo() == "Apple/Guava Juice, 16 oz, $4.50"

def test_fruitjuice_multiple_fruits():
    juice = FruitJuice(20, 6.0, ["Orange", "Pineapple", "Strawberry"])
    assert juice.getInfo() == "Orange/Pineapple/Strawberry Juice, 20 oz, $6.00"

def test_fruitjuice_empty_fruits_list():
    with pytest.raises(ValueError):
        FruitJuice(16, 4.5, [])

#DrinkOrder
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

def test_drinkorder_total_price():
    c1 = Coffee(8, 3.0, "Espresso")
    juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
    order = DrinkOrder()
    order.addBeverage(c1)
    order.addBeverage(juice)
    total_price = sum(bev.getPrice() for bev in order.drinks)
    assert total_price == 7.5

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

def test_drinkorder_large_order():
    order = DrinkOrder()
    for i in range(10):
        order.addBeverage(Coffee(12, 5.0, "Latte"))
    assert len(order.drinks) == 10
    assert order.getTotalOrder() == (
        "Order Items:\n" +
        "".join(["* Latte Coffee, 12 oz, $5.00\n" for _ in range(10)]) +
        "Total Price: $50.00"
    )
