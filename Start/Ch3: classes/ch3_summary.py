# range(start, stop, step) will create a range of numbers, which you can use in a loop
for i in range (5,15,2):
    print(i)

#=================== classes =========================
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

#=================== exceptions =========================

try:
    answer = int(input ("What should I divide 10 by? "))
    print(10/answer)
except ZeroDivisionError as e:
    print ("can't divide by 0 bro")
except ValueError as e:
    print ("you didn't give me a number bro")
except:
    print("some other exception bro")
finally:
    print("finally done with this bro")

#=================== palindrome test =========================

def is_palindrome(teststr):
    # remove all spaces and special characters
    teststr = ''.join(e for e in teststr if e.isalnum())

    # make it lowercase
    teststr = teststr.lower()

    # needs to be an even-lenght string
    if len(teststr) % 2 == 0:
        return False

    for i, c in enumerate(teststr):
        if c != teststr[-(i+1)]:
            return False

    return True

print(is_palindrome("Madam, I'm Adam."))
