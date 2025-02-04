def count_sheep(n):
    result = ''
    for i in range(n):
        result += f'{i + 1}sheep...'
    return result    
    
print(count_sheep(3))    
print(count_sheep(2))  