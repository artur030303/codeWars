def serch_letters(sentence):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    result = []
    for num in sentence.lower():
        if num in alphabet:
           index = alphabet.index(num) +1
           result.append(index)
    return ' '.join(map(str,result))   



print(serch_letters("The sunset sets at twelve o' clock."))
print(serch_letters("The narwhal bacons at midnight."))
      
                    #  "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
                    
                    #  "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")