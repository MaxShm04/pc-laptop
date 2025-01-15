class store:
    def __init__(self):
        self.inventory = {}

    def addItem(self, item):
        category = item.category
        if category not in self.inventory:
            self.inventory[category] = []
        self.inventory[category].append(item)

    def removeItem(self, item):
        for i in self.inventory[item.category]:
            if i.upc == item.upc:
                self.inventory[item.category].remove(i)
                break

    def getItems(self, category):
        category = category.upper()
        if category not in self.inventory or not self.inventory[category]:
            return ""
        return "\n".join(item.toString() for item in self.inventory[category])

    def removeCategory(self, category):
        category = category.upper()
        if category not in self.inventory:
            return
        del self.inventory[category]

    def doesItemsExist(self, item):
        cat = item.category
        if item not in self.inventory[cat]:
            return False
        return True

    def countDollarItems(self):
        out = 0
        for cat in self.inventory:
            for item in self.inventory[cat]:
                if item.price <= 1.0: out += 1
        return out


'''
i1 = Item()
i1.setPrice(1.00)
i1.setName("avocado")
i1.setCategory("produce")
i1.setUpc(420012347654)
i2 = Item()
i2.setPrice(0.9)
i2.setName("kiwiw")
i2.setCategory("produce")
i2.setUpc(420012347654)
i3 = Item()
i3.setPrice(3.0)
i3.setName("banana")
i3.setCategory("produce")
i3.setUpc(420012347654)


stre = store()
stre.addItem(i1)
stre.addItem(i2)
stre.addItem(i3)

print(stre.getItems("produce"))
print("____")
#stre.removeItem(i1)
print(stre.getItems("produce"))

print("____")
print(stre.doesItemsExist(i1))
print(stre.doesItemsExist(i3))

print("____")
print(stre.countDollarItems())






class Student: 
    def __init__(self, name, perm):
        self.name = None
        self.perm = None
        
    def set_name(self, name):
        self.name = name

    def set_perm(self, perm):
        self.perm = perm

    def printAttribute(self):
        print("Student name {}, perm {}".format(self.name, self.perm))  #evtl linebreak before \

s = Student ("Chris" , 1111111)
s.set_name("Chris")
s.set_perm(1111111)
s.printAttribute()


'''