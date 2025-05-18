class Person:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age

class Emplyoee(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age, year)
        self.joining_year = year
    def printname(self):
        print(f"{self.name}, {self.age}yrs old joined in {self.joining_year}")

x=Emplyoee("Gokul", 24, 2022)
x.printname()
