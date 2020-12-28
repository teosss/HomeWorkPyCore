def check_odd_even(number):
    try:
        number = int(number)
        if number % 2 == 0:
            return "Entered number is even"
        else:
            return "Entered number is odd"
    except ValueError:
        return "You entered not a number."



#Function example:

check_odd_even (24)     #output:    "Entered number is even"


check_odd_even (19)     #output:     "Entered number is odd"




"""
Author

def is_number(number):
    check_result = True
    try:
        if isinstance(number, str):
            raise ValueError
    except ValueError:
        check_result = False
    return check_result


def check_odd_even(number):
    try:
        if is_number(number):
            if number % 2 == 0:
                return "Entered number is even"
            else:
                return "Entered number is odd"
        return "You entered not a number."
    except:
        return "You entered incorrect data. Please try again."
"""