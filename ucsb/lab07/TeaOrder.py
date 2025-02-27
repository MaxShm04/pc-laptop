from CustomTea import CustomTea
from SpecialtyTea import SpecialtyTea


class TeaOrder:
    def __init__(self, distance):
        self.teas = []
        self.distance = distance

    def addTea(self, tea):
        self.teas.append(tea)

    def getOrderDescription(self):
        return (f"******\n"
                f"Shipping Distance: {self.distance} miles\n"
                + f"\n".join([i.getTeaDetails() + "\n----" for i in self.teas])
                + f"\nTOTAL ORDER PRICE: ${sum(i.getPrice() for i in self.teas):.2f}\n"
                + f"******\n")

