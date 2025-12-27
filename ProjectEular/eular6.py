import math
from functools import reduce

def lcm(a, b):
    return a * b // math.gcd(a, b)

result = reduce(lcm, range(1, 21))
print(result)  # Output: 232792560