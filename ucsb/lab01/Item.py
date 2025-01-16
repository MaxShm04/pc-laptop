class Item:
    def __init__(self, upc = None, category = None, name = None, price = None ):
        self.upc = upc
        self.category = category.upper() if category else None
        self.name = name.upper() if name else None
        self.price = price

    def setUpc(self, upc):
        self.upc = upc

    def setCategory(self, category):
        self.category = category.upper()

    def setName(self, name):
        self.name = name.upper()

    def setPrice(self, price):
        self.price = price

    def toString(self):
        return(f"UPC: {self.upc}, Category: {self.category}, Name: {self.name}, Price: ${self.price:.2f}")
