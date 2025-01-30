import pytest
from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

def test_init_beverage():
    beverage = Beverage(12, 1.99)
    assert beverage.getOunces() == 12
    assert beverage.getPrice() == 1.99

def test_update_oz_beverage():
    beverage = Beverage(12, 1.99)
    beverage.updateOunces(16)
    assert beverage.getOunces() == 16

def test_update_price_beverage():
    beverage = Beverage(12, 1.99)
    beverage.updatePrice(2.49)
    assert beverage.getPrice() == 2.49

def test_info_beverage():
    beverage = Beverage(12, 1.99)
    assert beverage.getInfo() == "12 oz, $1.99"

def test_zero_oz_beverage():
    beverage = Beverage(0, 1.99)
    assert beverage.getOunces() == 0

def test_zero_price_beverage():
    beverage = Beverage(12, 0)
    assert beverage.getPrice() == 0

def test_neg_oz_beverage():
    beverage = Beverage(-5, 1.99)
    assert beverage.getOunces() == -5

def test_neg_price_beverage():
    beverage = Beverage(12, -1.99)
    assert beverage.getPrice() == -1.99

def test_init_coffee():
    coffee = Coffee(12, 2.99, "Espresso")
    assert coffee.getOunces() == 12
    assert coffee.getPrice() == 2.99
    assert coffee.style == "Espresso"

def test_update_oz_coffee():
    coffee = Coffee(12, 2.99, "Espresso")
    coffee.updateOunces(16)
    assert coffee.getOunces() == 16

def test_update_price_coffee():
    coffee = Coffee(12, 2.99, "Espresso")
    coffee.updatePrice(3.49)
    assert coffee.getPrice() == 3.49

def test_info_coffee():
    coffee = Coffee(12, 2.99, "Espresso")
    assert coffee.getInfo() == "Espresso Coffee, 12 oz, $2.99"

def test_zero_oz_coffee():
    coffee = Coffee(0, 2.99, "Espresso")
    assert coffee.getOunces() == 0

def test_zero_price_coffee():
    coffee = Coffee(12, 0, "Espresso")
    assert coffee.getPrice() == 0

def test_neg_oz_coffee():
    coffee = Coffee(-5, 2.99, "Espresso")
    assert coffee.getOunces() == -5

def test_neg_price_coffee():
    coffee = Coffee(12, -2.99, "Espresso")
    assert coffee.getPrice() == -2.99

def test_init_fruitjuice():
    juice = FruitJuice(12, 3.99, ["Apple", "Orange", "Banana", "Grape"])
    assert juice.getOunces() == 12
    assert juice.getPrice() == 3.99
    assert juice.fruits == ["Apple", "Orange", "Banana", "Grape"]

def test_update_oz_fruitjuice():
    juice = FruitJuice(12, 3.99, ["Apple", "Orange", "Banana", "Grape"])
    juice.updateOunces(16)
    assert juice.getOunces() == 16

def test_update_price_fruitjuice():
    juice = FruitJuice(12, 3.99, ["Apple", "Orange", "Banana", "Grape"])
    juice.updatePrice(4.49)
    assert juice.getPrice() == 4.49

def test_info_fruitjuice():
    juice = FruitJuice(12, 3.99, ["Apple", "Orange", "Banana", "Grape"])
    assert juice.getInfo() == "Apple/Orange/Banana/Grape Juice, 12 oz, $3.99"


def test_zero_price_fruitjuice():
    juice = FruitJuice(12, 0, ["Apple", "Orange", "Banana", "Grape"])
    assert juice.getPrice() == 0

def test_neg_price_fruitjuice():
    juice = FruitJuice(12, -3.99, "Apple")
    assert juice.getPrice() == -3.99

def test_add_beverage():
    order = DrinkOrder()
    beverage = Beverage(12, 1.99)
    order.addBeverage(beverage)
    assert len(order.drinks) == 1
    assert order.drinks[0] == beverage

def test_add_coffee():
    order = DrinkOrder()
    coffee = Coffee(12, 2.99, "Espresso")
    order.addBeverage(coffee)
    assert len(order.drinks) == 1
    assert order.drinks[0] == coffee

def test_add_fruitjuice():
    order = DrinkOrder()
    juice = FruitJuice(12, 3.99, "Apple")
    order.addBeverage(juice)
    assert len(order.drinks) == 1
    assert order.drinks[0] == juice

def test_total_order():
    order = DrinkOrder()
    beverage = Beverage(12, 1.99)
    coffee = Coffee(12, 2.99, "Espresso")
    juice = FruitJuice(12, 4.5 ,["Apple", "Orange", "Banana", "Grape"] )
    order.addBeverage(beverage)
    order.addBeverage(coffee)
    order.addBeverage(juice)
    total_order = order.getTotalOrder()
    assert "Order Items:" in total_order
    assert "* 12 oz, $1.99" in total_order
    assert "* Espresso Coffee, 12 oz, $2.99" in total_order
    assert "* Apple/Orange/Banana/Grape Juice, 12 oz, $4.50" in total_order
    assert "Total Price: $9.48" in total_order
