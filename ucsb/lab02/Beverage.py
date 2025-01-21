class Beverage:
    def __init__(self, ounces, price):
        self.ounces = ounces if ounces >= 0 else TypeError
        self.price = price if price >= 0 else TypeError

    def updateOunces(self, newOunces):
        self.ounces = newOunces if newOunces >= 0 else TypeError

    def updatePrice(self, newPrice):
        self.price = newPrice if newPrice >= 0 else TypeError

    def getPrice(self):
        return self.price

    def getOunces(self):
        return self.ounces

    def getInfo(self):
        return f"{self.ounces} oz, ${self.price:.2f}"

