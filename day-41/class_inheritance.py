"""
Implement inheritance between classes.
"""

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print(f"{self.name} says woof!")

class Cat(Animal):

    def speak(self):
        print(f"{self.name} says meow!")

if __name__ == "__main__":
    dog = Dog("Dog")
    dog.speak()
    cat = Cat("Cat")
    cat.speak()
