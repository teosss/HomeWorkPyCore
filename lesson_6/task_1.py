def func_1():
    """ 
    Function 1 find the even, odd, div23 numers classic method """
    even = []
    odd = []
    div23 = []
    for i in range(1,10):
        if i % 2 == 0:
            even.append(i)
        if i % 3 == 0:
            odd.append(i)
        if i % 2 != 0 and i % 3 != 0:
            div23.append(i)
    print(func_1.__doc__)
    print("Even numbers: ", even)
    print("Odd numbers: ", odd)
    print("Numbers div 2 and 3: ", div23)

def func_2():
    """ 
    Function 2 find the even, odd, div23 numers list comprehension """
    
    print(func_2.__doc__)
    print("Even numbers: ", list(i for i in range(1,10) if i % 2 == 0))
    print("Odd numbers: ", list(i for i in range(1,10) if i % 3 == 0))
    print("Numbers not div 2 and 3: ", list(i for i in range(1,10) if i % 2 != 0 and i % 3 != 0))

def func_3(*arg):
    """ 
    Function 3 find the even, odd, div23 numers with tuples """
    
    print(func_3.__doc__)
    print("Even numbers: ", list(i for i in arg if i % 2 == 0))
    print("Odd numbers: ", list(i for i in arg if i % 3 == 0))
    print("Numbers not div 2 and 3: ", list(i for i in arg if i % 2 != 0 and i % 3 != 0))    

func_1()
func_2()
func_3(1,2,3,4,5,6,7,8,9)