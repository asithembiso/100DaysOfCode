"""
Implement encapsulation in a class.
"""

class Shape:

    def __init__(self):
        self._name = "Square"

    def get_shape_name(self):
        print(self._name)

if __name__ == "__main__":
    shape = Shape()
    shape.get_shape_name() # accessible
    # print(shape.name) not accessible
