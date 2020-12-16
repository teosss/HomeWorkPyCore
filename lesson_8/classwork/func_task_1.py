from random import randint

def begin_game(count):
    """
    Function for entering and checking the number for truth
    
    Input:
    find(int) - random number
    count(int) - counter
    
    Result:
    count(int)
    """
    global find
    print(f"{count} attempts")
    number = int(input("Please, enter the number from 0 to 100: "))  # Отримує число
    count -= 1                                                       # Індикатор спроб +1 
    if number > find:                                                # Перевіряє і виводить підказки
        print("Your number is too big")                              #
    elif number < find:                                              #
        print("Your number is too small")                            #
    if count == 5:                                                   # Додаткова підказка 
        print ("I give another hint: {} > number < {}".format(round(find-5,-1), round(find+4,-1))) 
    elif count == 0:
        return False
    return count if number is find else begin_game(count)

find = randint(1, 100)       