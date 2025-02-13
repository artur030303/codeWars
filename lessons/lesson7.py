# def calculate(*args)-> None:
#     l= [1,2,3,4]
#     se = set(['a','b',1])
#     if len(args)>3:
#         print('Too many arguments')
#     else:
#         print('ok')    


# calculate(1,2,3,4,'bla', [4,3553, 'sags'])
# calculate()    

# def calculate2(**kwargs)-> None:
#     print(kwargs)   

# calculate2(a=1,b=2,c=3)


def multiply(a,b):
    return a*b

values = 2,3
result = multiply(*values)
print(result)