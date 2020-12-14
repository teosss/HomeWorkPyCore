import random

def begin_game():
    """
    Function for entering and checking the number for truth
    
    Result:
    (int)
    """
    global find
    global count    
    number = int(input("Please, enter the number from 0 to 100: "))  # Отримує число
    count += 1                                                       # Індикатор спроб +1 
    if number > find:                                                # Перевіряє і виводить підказки
        print("Your number is too big")                              #
    elif number < find:                                              #
        print("Your number is too small")                            #
    if count == 3:                                                   # Додаткова підказка 
        print ("I give another hint: {} > number < {}".format(round(find-10,-1), round(find+10,-1))) 
    return number if number is find else begin_game()
    
count = 0
find = random.randint(1, 100)    
find = begin_game()   
print(f"WIN!!!, you guessed it from {count} attempts")
