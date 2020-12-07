number = input()
number = number.split(" ")

number = list(map(int, number))

min = number[0]
max = number[0]
for i in number:
    if max <= i:
        max = i
    elif min >= i:
        min = i
print("Max = ", max)
print("Min = ", min)

