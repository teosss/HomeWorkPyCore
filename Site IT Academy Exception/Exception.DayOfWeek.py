def day_of_week(day):
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    try:
        number = int(day)
        if type(day) != int and type(number) == int:
            raise KeyError 
        elif day > 7 or day < 1:
            raise KeyError  
        return weekDays[day-1]          
    except KeyError:
        return "There is no such day of the week! Please try again."
    except ValueError:
        return "You did not enter a number! Please try again."



print(day_of_week(2))                      # output:   "Tuesday"

print(day_of_week(11))                     # output:  "There is no such day of the week! Please try again."

print(day_of_week("Monday"))               # output:   "You did not enter a number! Please try again."

print(day_of_week("6"))               # output:   "You did not enter a number! Please try again."

"""
Author

def is_day_of_week(day):
    check_result = True
    try:
        int(day)
    except ValueError:
        check_result = False
    return check_result

def day_of_week(day):
    week_day = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Tuesday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    try:
        if is_day_of_week(day):
            return week_day[day]        
    except KeyError:
        return "There is no such day of the week! Please try again."
    else:
        return "You did not enter a number! Please try again."


"""