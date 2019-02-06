import ex01
import sys
from math import sqrt, sin, cos, pi

sys.path.insert(0, "/Users/vinodkumar/Desktop")

from constants import name, city

print("Hello %s, how's weather in %s?" % (name, city))

sys.exit()


print("This is in module#2")
print("__name__ is " + __name__)


print("There are {0} arguments".format(len(sys.argv)))
print("The arguments are", end="")
print(sys.argv)

n = 1234
print("Square root of {0} is {1}".format(n, sqrt(n)))
print("Sine of {0} is {1}".format(n, sin(n)))
print("Cosine of {0} is {1}".format(n, cos(n)))
print("Value of PI is {0}".format(pi))

# from the command prompt in the working directory, issue this command:
# python ex02.py "vinod kumar" bangalore karnataka india
