from math import *
from random import *

print(uniform(0, 2))
x = float(input("Please type your x: "))

y = (sin((x ** 2) - 1) ** 3) + log(fabs(x)) + e ** x
print(y)
