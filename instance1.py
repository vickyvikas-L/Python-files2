class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

   
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)



s1 = Student("Vikas", 21)
s2 = Student("Rahul", 22)


s1.display()
s2.display()