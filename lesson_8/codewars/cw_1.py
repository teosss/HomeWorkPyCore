# Count of positives / sum of negatives
# https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives

def count_positives_sum_negatives(arr):
    count, b = 0, 0
    for i in arr:
        if i > 0:
            count += 1
        else:
            b += i
    return [count,b] if arr != [] else []