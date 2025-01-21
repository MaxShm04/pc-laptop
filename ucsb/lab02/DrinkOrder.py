class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        costs = 0
        out = ""
        for drink in self.drinks:
            costs += drink.price
            out += "* " + drink.getInfo() + "\n"

        return f"Order Items:\n{out}Total Price: ${costs:.2f}"

