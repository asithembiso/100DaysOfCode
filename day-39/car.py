"""
Create a class for a simple car with methods like start and stop.
"""

class Car:

    def __init__(self):
        self.mode = ""

    def start(self):
        self.mode = "starting"

    def stop(self):
        self.mode = "stopping"

    def get_mode(self) -> str:
        return self.mode


if __name__ == "__main__":
    myCar = Car()
    myCar.start()
    print(myCar.get_mode())

    myCar.stop()
    print(myCar.get_mode())
