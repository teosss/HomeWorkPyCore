def day_of_week(number):
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    try:
        number = int(number)
        while number > 7:
            number -= 7
        return weekDays[number-1]
           
    except ValueError as e:
        print("Please enter correct number. ", e)
    except NameError as e: 
        print("NameError: ", e)
    except ZeroDivisionError as e:
        print("Zero Division Error: ", e)


day = day_of_week(input("Please, enter the number: "))
print(day)
