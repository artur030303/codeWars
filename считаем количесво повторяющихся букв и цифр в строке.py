def count_words(text):
    count = {}
    for word in text:
        count[word]= count.get(word,0) +1
    return {word: count for word, count in count.items() if count>1}       


print(count_words("aabcfdddf"))
print(count_words("aabcfdddf"))