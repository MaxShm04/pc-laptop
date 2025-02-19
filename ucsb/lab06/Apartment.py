class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return f"(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}"

    def _condition_value(self):
        mapping = {"excellent": 0, "average": 1, "bad": 2}
        return mapping[self.condition]

    def __lt__(self, other):
        if self.rent != other.rent:
            return self.rent < other.rent
        if self.metersFromUCSB != other.metersFromUCSB:
            return self.metersFromUCSB < other.metersFromUCSB
        return self._condition_value() < other._condition_value()

    def __eq__(self, other):
        return (self.rent == other.rent and
                self.metersFromUCSB == other.metersFromUCSB and
                self.condition == other.condition)

    def __gt__(self, other):
        return (not self < other) and (not self == other)
