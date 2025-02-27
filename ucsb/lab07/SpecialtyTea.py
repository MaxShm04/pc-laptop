from Tea import Tea

class SpecialtyTea(Tea):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name

        if self.size == "S":
            self.setPrice(12.00)
        elif self.size == "M":
            self.setPrice(16.00)
        else:
            self.setPrice(20.00)

    def getTeaDetails(self):
        return (f"SPECIALTY TEA\n"
                f"Size: {self.size}\n"
                f"Name: {self.name}\n"
                f"Price: ${self.price:.2f}\n")

