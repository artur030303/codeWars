

def get_middle(s):
    text = 'absdf'
    if len(s) % 2 == 0:
        return s[len(s) // 2 - 1] + s[len(s) // 2]
    else:
        return s[len(s) // 2]
    

print(get_middle("test"))