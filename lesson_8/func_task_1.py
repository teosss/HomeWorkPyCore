def begin_game(find, count):
    """
    Function for entering and checking the number for truth
    
    Input:
    find(int) - random number
    count(int) - counter
    
    Result:
    count(int)
    """
    number = int(input("Please, enter the number from 0 to 100: "))  # Отримує число
    count += 1                                                       # Індикатор спроб +1 
    if number > find:                                                # Перевіряє і виводить підказки
        print("Your number is too big")                              #
    elif number < find:                                              #
        print("Your number is too small")                            #
    if count == 3:                                                   # Додаткова підказка 
        print ("I give another hint: {} > number < {}".format(round(find-10,-1), round(find+10,-1))) 
    return count if number is find else begin_game(find, count)