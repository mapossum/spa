import random

class Dog:

    def __init__(self, name="Fido", age=0):  
        self.name = name
        self.age = age
        self.weight = random.normalvariate(1,0.5)

    def grow(self,years=1):
        self.age = self.age + years
        self.weight = self.weight + random.normalvariate(years, (years * 0.5))
        print("{} is now {} years old and weighs {} pounds".format(self.name, self.age, self.weight))

    def bark(self):
        if self.age > 3:
            print("Woof, Woof!")
        else:
            print("Bow, Wow!")

chloe = Dog()



