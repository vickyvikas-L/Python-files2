class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        
    def display(self):
        print(self.brand,self.price)
        
m1=mobile("redmi",20000)
m1.display()