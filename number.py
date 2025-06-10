value1 = 100
print(type(value1))
print(isinstance(value1, int))
print(isinstance(value1, float))
print(isinstance(value1, complex))


# type conversion
print (int(10.5))
print(int(-20.99))
print(float(10))


# python decimal

data1 = 0.1+0.2
print(data1)
data1 = 1.20* 2.50
print(data1)
from decimal import Decimal as D
print(D('0.1') + D('0.2'))
print(D('1.2') * D('2.5'))

# python fractions

from fractions import Fraction as F
print(F(1.5))
print(F(5))
print(F(1,5))


# python math module

import math
print(math.pi)
print(math.cos(10))
print(math.log(10))
print(math.log10(10))
print(math.factorial(5))

# python random module
import random
print('Random Number -> ', random.randrange(5,15))
print('Random Number -> ', random.randrange(5,15))

day=['sun','mon','tue','wed','thu','fri','sat']
print(random.choice(day))

