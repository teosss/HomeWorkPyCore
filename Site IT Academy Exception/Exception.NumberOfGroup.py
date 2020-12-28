class ToSmallNumberGroupError():
    def __init__(self, number):
        self.number = number
    
    def __get__(self):
        return "We obtain error:Number of your group can't be less than 10" 

def check_number_group(number):
    try:
        if type(number) != int and type(number) != float:
            number = int(number)
        if number < 10:
            raise BaseException
        return f"Number of your group {number} is valid"
    except ValueError:
        return "You entered incorrect data. Please try again."
    except BaseException:
        expt = ToSmallNumberGroupError(number)
        return expt.__get__()

#Function example:

print(check_number_group(4))        #output:    "We obtain error: Number of your group can't be less than 10"

print(check_number_group(59))     #output:     "Number of your group 59 is valid"

print(check_number_group(0.8))     #output:     "Number of your group 59 is valid"

print(check_number_group("25"))                #output:    "Number of your group 25 is valid"

print(check_number_group("abc"))             #output:     "You entered incorrect data. Please try again."



"""
Author

class ToSmallNumberGroupError(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(self.data)


def check_number_group(number):
    try:
        number_group = int(number)
        if number_group < 10:
            raise ToSmallNumberGroupError("Number of your group can't be less than 10")
    except ToSmallNumberGroupError as e:
        return "We obtain error:" + e.data
    except:
        return "You entered incorrect data. Please try again."
    else:
        return f"Number of your group {number_group} is valid"

"""