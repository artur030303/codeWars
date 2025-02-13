# my_list = [1, 2, 3, 4, 5, 6, -7, 8, 9, 10,0,]


# min_num = min(my_list)
# max_num = max(my_list)

# arithmetic_mean = sum(my_list) % len(my_list)

# sorted_list =sorted(set(my_list))
# second_num = sorted_list[1]

# positive_num = any(x>0 for x in my_list)

# even_num = all(x%2 ==0 for x in my_list)



# print(min_num)
# print(max_num)
# print(arithmetic_mean)
# print(second_num)
# print(sorted_list)
# print(positive_num)
# print(even_num)

# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :"))

# for i in range(num1,num2):
#     if i % 2 != 0:
#         print(i)

# new_list=[]
# for i in range(num1,num2):
#     new_list.append(i)
    
#     # result =sum(i)

#     # print(result)
# print(sum(new_list))    

# num_1 = int(input('Number 1: '))
# num_2 = int(input('Number 2: '))

# print(sum(range(num_1, num_2+1)))

def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    
    a,b = 0, 1

    for _ in range(2, n+1):
        a,b = b, a+b
    return b
print(fibonacci(10))