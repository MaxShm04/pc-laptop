class Beverage:
    def __init__(self, ounces, price):
        if ounces < 0:
            raise ValueError("Ounces must be a non-negative value.")
        if price < 0:
            raise ValueError("Price must be a non-negative value.")
        self.ounces = ounces
        self.price = price

    def updateOunces(self, newOunces):
        if newOunces < 0:
            raise ValueError("Ounces must be a non-negative value.")
        self.ounces = newOunces

    def updatePrice(self, newPrice):
        if newPrice < 0:
            raise ValueError("Price must be a non-negative value.")
        self.price = newPrice

    def getPrice(self):
        return self.price



    def getOunces(self):
        return self.ounces

    def getInfo(self):
        return f"{self.ounces} oz, ${self.price:.2f}"


