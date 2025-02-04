def disemvowel(string_):
    vowels = 'aeiouAEOIU'
    result=[]
    for word in string_:
        if word not in vowels:
            result.append(word)
    return ''.join(result)

print(disemvowel("this website is for losers LOL"))