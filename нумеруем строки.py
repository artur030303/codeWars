def num_of_string(sentence):
    result = []
    for i, line in enumerate(sentence,1):
        result.append(f'{i}: {line}')
    return result
    


print(num_of_string(["Hello", "World", "Python"]))
print(num_of_string(["one", "two", "three"]))
print(num_of_string([]))

