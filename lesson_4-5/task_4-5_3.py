def fibon_1(n):    
    first, second = 0, 1
    print(first, end=' ')
    while second < n:
        print(second, end=' ')
        first, second = second, first + second
    print()

def fibon_2(n):   
    first, second = 0, 1
    result = [first]
    while second < n:
        result.append(second)
        first, second = second, first + second
    print(result)


fibon_1(18)
fibon_2(18)
