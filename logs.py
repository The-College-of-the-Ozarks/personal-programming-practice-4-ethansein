# logs.py
#
# Outputs the value of g(x) = ln(100-x^2) + sqrt(84 - 5x - x^2) at the input x-value.

from lib2to3.pgen2.token import LESSEQUAL
import math

def g(x):
    return math.log(100 - x**2) + math.sqrt(84 - 5*x - x**2)

x = input("Input the value for x: ")
x = float(x)


if not x > -10:
    print("Invalid input, number is too low")

if not x <= 7:
    print("Invalid input, number is too high")

else: 
    print("g(" + str(x) + ") = " + str(g(x)))