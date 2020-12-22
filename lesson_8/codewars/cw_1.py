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


# OR THIS
def count_positives_sum_negatives(arr):
    return [len((filter(lambda x: x > 0, arr))), sum((filter(lambda x: x < 0, arr)))] if arr != [] else []