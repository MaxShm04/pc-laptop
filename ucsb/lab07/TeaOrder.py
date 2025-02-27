from CustomTea import CustomTea
from SpecialtyTea import SpecialtyTea


class TeaOrder:
    def __init__(self, distance):
        self.teas = []
        self.distance = distance

    def addTea(self, tea):
        self.teas.append(tea)

    def getOrderDescription(self):
        tea_details = "\n".join([i.getTeaDetails() + "\n----" for i in self.teas])

        return (f"******\n"
                f"Shipping Distance: {self.distance} miles\n"
                + (tea_details + "\n" if tea_details else "")  # Avoid extra newline when empty
                + f"TOTAL ORDER PRICE: ${sum(i.getPrice() for i in self.teas):.2f}\n"
                + "******\n")

