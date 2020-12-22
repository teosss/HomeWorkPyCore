def day_of_week(number):
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    try:
        number = int(number)
        if number > 7:
            raise ValueError("Your number > 7")     
        return weekDays[number-1]             
    except ValueError as e:
        print("Please enter correct number. ", e)

day = day_of_week(input("Please, enter the number: "))
print(day)
