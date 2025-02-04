def solution(text, ending):
    return text[-len(ending):] == ending


print(solution("samurai", "ai"))
print(solution("ninja",   "ja"))
print(solution("sensei",  "i"))
print(solution("abc",     "abc"))
print(solution("abcabc",  "bc"))
print(solution("spam",    "eggs"))
