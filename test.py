def solve(arr):
    square = 1
    count = 0
    for i in range(0,len(arr),2):
        square *= arr[i]**2 + arr[i+1]**2
    if square > 10**6:
        square /= 2
        count += 1
    a = int(square**0.5)
    b = int((square-a**2)**0.5)
    while True:
        if a**2 + b**2 == square:
            return [a*count,b*count]
        else:
            a -= 1
            print(a)
            b = int((square - a**2)**0.5)

    
    
arr = [3, 9, 8, 4, 6, 8, 7, 8, 4, 8, 5, 6, 6, 4, 4, 5]
print(solve(arr))




"""def solve(arr):
    square = 1
    for i in range(0,len(arr),2):
        square *= arr[i]**2 + arr[i+1]**2
    print (square)
    a = (square**0.5)
    print(a)
    b = (square-a**2)**0.5
    print(b)
    while True:
        if a**2 + b**2 == square:
            return [int(a),int(b)]
        else:
            a -= 1
            b = int((square - a**2)**0.5)"""
