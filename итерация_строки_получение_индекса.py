def accum(st):
    result = []
    for i, num in enumerate(st):
        result.append(num.upper() + num.lower() * i)
    return '-'.join(result)


print(accum("ZpglnRxqenU"))
