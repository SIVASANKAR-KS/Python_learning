class MyClass:
    x=5;

p1=MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name} {self.age}" 

p1=Person("John", 36)
print(p1.name)

del(p1.name)
try:
    print(p1.name)
except Exception as e:
    print(f"{type(e)}:e")
except:
    print("something")