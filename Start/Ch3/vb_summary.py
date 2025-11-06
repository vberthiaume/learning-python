# range(start, stop, step) will create a range of numbers, which you can use in a loop
for i in range (5,15,2):
    print(i)

# you can build formated strings with the f prefix
greeting = "Hello!"
count = 10
print(f"{greeting} you are bro number {count}")

# base class
class Vehicle:
    def __init__(self, bodystyle):  # this is the constructor
        self.bodystyle = bodystyle
    
    def drive(self, speed):
        self.speed = speed

# to inherit from a class, you put it in parens lol
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car") # you need to explicitly call the super constructor, you need the parens on super()
        self.engine = enginetype# member variables can be declared whenever I guess?

    def drive(self, speed):
        super().drive(speed)
        print(f"driving my {self.engine} car at {self.speed} KILOMETERS BRO")

car1 = Car("gas")
car2 = Car("electric")
car2.drive(32)