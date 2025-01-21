from ucsb.lab02.Beverage import Beverage


class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        super().__init__(ounces, price)
        self.fruits = fruits

    def getInfo(self):
        return f"{'/'.join(self.fruits)} Juice, {super().getInfo()}"