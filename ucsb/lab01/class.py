
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