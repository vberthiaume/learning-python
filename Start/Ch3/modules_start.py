# import the math module, which contains features for working with mathematics
import math
print(math.pi)

# import a specific part of the module so you can refer to it more easily
from math import pi
print(pi)   # no need to use math.pi

# import a module and give it a different name
import random as r
print(r.randint(100, 200))

# Use the 3rd party tabulate module to print tabulated data:
from tabulate import tabulate

# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]

# Create a formatted table
