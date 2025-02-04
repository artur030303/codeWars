import math


def is_square(n):
    if n < 0:
        return False
    root = math.sqrt(n)
    return root.is_integer()


print(is_square(25))
print(is_square(-2))
print(is_square(26))
print(is_square(16))
