#######################################FUNCTION PLOYMORPHISM###################################################

###STRING
x="adstr"
print(len(x))           ###length of string

###TUPLE
x=("ad","cb")
print(len(x))           ####number of items

##DICT
x={"a":"sd","b":"ca"}   ####number of key-value pairs
print(len(x))


#######################################CLASS PLOYMORPHISM###################################################

class Car:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        print(f"{self.name} Drive")
    
class Boat:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        print(f"{self.name} Sails")

car1=Car("lambo")
boat1=Boat("Ibiza")
for i in (car1, boat1):
    i.move()


#################################  CLASS  INHERITANCE  PLOYMORPHISM   ###################################################
class Vehicle:
    def __init__(self, name) -> None:
        self.name=name
    def move(self):
        print(f"{self.name} moves")

class Car(Vehicle):
    def __init__(self, name) -> None:
        super().__init__(name)
    pass
    
class Boat(Vehicle):
    def move(self):
        print(f"{self.name} Sails")

car1=Car("lambo")
boat1=Boat("Ibiza")
for i in (car1, boat1):
    i.move()                ###since move is not in class car, it inherits from class vehicle 