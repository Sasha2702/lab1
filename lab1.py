from math import *
from random import *

print(uniform(0, 1.9))
x = float(input("Please  x: "))

y = (sin((x ** 2) - 1) ** 3) + log(fabs(x)) + e ** x
print(y)
