class cricket:
   def input(self):
      self.name=input("enter the name:")
      self.age=int(input("enter the age:"))
      self.arm=input("enter the arm:")
      self.team=input("enter the team:")
      self.speciality=input("enter the speciality:")
   def display(self):
       print("\nBiodata")
       print(f"Name :{self.name}")
       print(f"age :{self.age}")
       print(f"course :{self.arm}")
       print(f"team :{self.team}")
       print(f"speciality :{self.speciality}")
bio=cricket()
bio.input()
bio.display()