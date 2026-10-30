class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f" {self.name}& age is {self.age}")
d=student("vikas",22)
d.display()