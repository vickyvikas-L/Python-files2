class comp:
    def __init__(self,cname,empid):
        self.cname=cname
        self.empid=empid
    def login(self,time):
        self.time=time
        return f"company logged in at {self.time}"
    def logout(self,time):
        self.time=time
        return f"company logged out at {self.time}"

class Devp(comp):
    def __init__(self, cname, empid,role):
        super().__init__(cname, empid)
        self.role=role
    def login(self,time):
        self.time=time
        return f"devp logged in at {self.time} of {self.cname} with role {self.role} and empid is {self.empid}"
    def logout(self,time):
        self.time=time
        return f"devp logged out at {self.time}"

class test(comp):
    def __init__(self, cname, empid,role):
        super().__init__(cname, empid)   
        self.role=role
    def login(self,time):
        self.time=time
        return f"test logged in at {self.time} of a {self.cname} with role {self.role} and empid is {self.empid}"
    def logout(self,time):
        self.time=time
        return f"test logged out at {self.time}"  

d=Devp(cname="RCB",empid="37",role="developer")
print(d.login(9))
print(d.logout(5))

t=test(cname="RCB",empid="43",role="tester")
print(t.login(11))
print(t.logout(8))