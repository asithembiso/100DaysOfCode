"""
Create a class hierarchy for different shapes (circle, square, triangle).
"""

class Shape:

    def __init__(self, name):
        self.name = name

    def get_name(self) -> str:
        return self.name

class Circle(Shape):

    def __init__(self, name):
        super().__init__(name)


class Square(Shape):

    def __init__(self, name):
        super().__init__(name)


class Triangle(Shape):

    def __init__(self, name):
        super().__init__(name)


if __name__ == "__main__":
    myCircle =  Circle("I'm a Circle")
    print(myCircle.get_name())

    myCircle = Square("I'm a Square")
    print(myCircle.get_name())

    myCircle = Triangle("I'm a Triangle")
    print(myCircle.get_name())

