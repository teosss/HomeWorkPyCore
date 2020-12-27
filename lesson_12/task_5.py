from functools import reduce

list1 = [1, 9, 24, 40, 3, 0, 1, 23]

list2 = reduce(lambda y, x: x if x >= y else y, list1)

print(list2)