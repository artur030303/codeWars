def row_sum_odd_numbers(n):
    total_sum = 0
    start = n * (n-1) + 1
    for i in range(n):
        total_sum += start + 2 * i
    return total_sum


print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(19))
print(row_sum_odd_numbers(41))
