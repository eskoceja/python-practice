# OOP - object oriented programming
# classes and objects

# Class: Dog
# Properties: name, age, breed
# Methods: bark, eat, sleep

# Object 1, 2, 3...
# Properties: fido, 5, german shepard...

# Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    

p1 = Person("Bob", 22)
print(p1.getName())
print(p1.getAge())