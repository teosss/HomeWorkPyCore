def getage():
    age = input("Please, enter your age: ")
    return valid_age(age)
     
def valid_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Your age < 0")
        elif age % 2 == 0:
            print("Your age is even")
        else:
            print("Your age is odd")
        return age   
    except ValueError as e:
        print("Please enter correct age. ", e)
        return getage()
    except NameError as e: 
        print("NameError: ", e)
        return getage()
    except ZeroDivisionError as e:
        print("Zero Division Error: ", e)
        return getage()





age = getage()
print("Your age is - ", age)
