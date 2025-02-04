def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count_positive = 0
    sum_negative = 0
    for num in arr:
        if num > 0:
            count_positive += 1
        elif num < 0:
            sum_negative += num
    return [count_positive, sum_negative]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
    
