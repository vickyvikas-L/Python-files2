#atm machine with pin using oops
class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
    def check_pin(self, entered_pin):
        return self.pin == entered_pin 
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")  
b=ATM(1234, 1000)
b.check_pin(1234)
b.withdraw(500)