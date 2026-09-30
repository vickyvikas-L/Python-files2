class bank:
    def bank_ac(self,accno,deposit):
        self.accno=accno
        self.deposit=deposit
    def with_draw(self,withdraw):
        self.withdraw=withdraw
        self.balance=self.deposit-self.withdraw
    def bdisplay(self):
        print(f"with_draw={self.withdraw}| balance={self.balance}")
class savings(bank):
    def interest(self):
        self.intrest_amt=self.balance*0.2
    def sdisplay(self):
        print(f"|deposit={self.deposit} \n| with_draw={self.withdraw}\n| current balance:{self.balance}\n| interest earned:{self.intrest_amt}")

amt=savings()
amt.bank_ac(123,5000)
amt.with_draw(1050)
amt.interest()
amt.sdisplay()