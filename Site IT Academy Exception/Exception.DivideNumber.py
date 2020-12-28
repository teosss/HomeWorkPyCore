def divide(numerator, denominator):
    try:
        
        if type(numerator) != int or type(denominator) != int:
            raise ValueError
        else:
            result = numerator / denominator
        
        return f"Result is {result}"
    except ValueError:
        return f"Value Error! You did not enter a number!"
    except ZeroDivisionError as e:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"


print(divide(8, 16))        #output:   "Result is 0.5" 

print(divide(5, 0))        #output:   "Oops, 5 / 0 denominator, division by zero is error!!!" 

print(divide("25", 5))    #output:   "Value Error! You did not enter a number!"

print(divide("abc", 9))  #output:    "Value Error! You did not enter a number!"


"""
Author

def is_number(number_1, number_2):
    check_result = True
    try:
        if isinstance(number_1, str) or isinstance(number_2, str):
            raise ValueError
    except ValueError:
        check_result = False
    return check_result


def divide(numerator, denominator):
    try:
        if is_number(numerator, denominator):
            result = float(numerator) / float(denominator)
            return f"Result is {result}"
        else:
            return "Value Error! You did not enter a number!" 
    
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
"""