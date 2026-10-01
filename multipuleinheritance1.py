class Father:
    def father_property(self):
        print("Father property")

class Mother:
    def mother_property(self):
        print("Mother property")

class Child(Father, Mother):
    def child_property(self):
        print("Child property")

c = Child()

c.father_property()
c.mother_property()
c.child_property()