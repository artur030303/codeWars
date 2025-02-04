def lovefunc(flower1, flower2):
    return (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0)


print(lovefunc(6, 5))
print(lovefunc(4, 8))
print(lovefunc(7, 3))
