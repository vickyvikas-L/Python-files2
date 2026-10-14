class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        cls.emp_str= emp_str
        cls.company="RCB"
        

    def display(self):
        print(f"{self.name} and salary is {self.salary} then company name {self.company} is {self.emp_str}")


emp1 = Employee("Pradeep",50000)
Employee.from_string("perment")
emp1.display()