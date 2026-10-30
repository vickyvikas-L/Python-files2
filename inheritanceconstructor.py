class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):
    def show_role(self):
        print("Role: Python Developer")


d = Developer("Vikas", 30000)

d.display()
d.show_role()