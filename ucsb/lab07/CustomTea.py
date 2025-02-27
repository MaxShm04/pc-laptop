from Tea import Tea

class CustomTea(Tea):
    def __init__(self, size, base):
        super().__init__(size.upper())
        self.base = base
        self.flavors = []

        if self.size == "S":
            self.setPrice(10.00)
        elif self.size == "M":
            self.setPrice(15.00)
        else:
            self.setPrice(20.00)

    def setBase(self, base):
        self.base = base

    def getBase(self):
        return self.base

    def addFlavor(self, flavor):
        self.flavors.append(flavor)
        if self.size == "S":
            self.setPrice(10.00+len(self.flavors)*0.25)
        elif self.size == "M":
            self.setPrice(15.00+len(self.flavors)*0.5)
        else:
            self.setPrice(20.00+len(self.flavors)*0.75)

    def getTeaDetails(self):
        return (f"CUSTOM TEA\n"
                f"Size: {self.size}\n"
                f"Base: {self.base}\n"
                f"Flavors:\n"
                + ("\n".join([f"\t+ {i}" for i in self.flavors]) + "\n" if self.flavors else "")
                + f"Price: ${self.price:.2f}\n")

