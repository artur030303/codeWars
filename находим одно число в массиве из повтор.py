


# def search_num (my_arr):
#     result = []
#     for num in my_arr:
#         if num not in result:
#             result.append(num)
#     return result





# print(search_num(my_arr= [17, 17, 3, 17, 17, 17, 17]))

# print(search_num(my_arr= [1,1,2]))




# {
#     '17': "True",
    
# }

# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3




# def search_num (my_arr):
#     result = []
#     number = {}
#     for num in my_arr:
#         if num  in number:
#             if number[num] == False :
#                 number[num] = True
#         else : number[num] = False
            
     

#     for a,b in number.items():
#         print(a,b)
#         if b == False:
#             result.append(a) 
#     print(number)
#     return result


# print(search_num(my_arr= [17, 17, 3, 17, 17, 17, 17,12,12,2,4,4, 5, 5 ,6]))




# def search_num (my_arr):
#     num_count = {}
#     result = []

#     for num in my_arr:
#         if num in num_count:
#             num_count[num] +=1
#         else:
#             num_count[num] = 1

#     print(num_count)
#     for a,b in num_count.items():
#        if b ==1:
#            result.append(a)
        
       

#     return result
         


def stray(arr):
    num_count = {}
    result= []
    
    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] =1
    print(num_count)
    for key,value in num_count.items():
        if value ==1:
            result.append(key)
    return result[0]     

print(stray([17, 17, 3, 17, 17, 17, 17,12,12,2,4,4, 5, 5 ,6]))

