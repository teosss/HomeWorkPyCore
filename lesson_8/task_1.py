import random
import func_task_1                                   # імпортуємо функцію перевірки співвідношення
    
count = 0                                            # лічильник спроб
find = random.randint(1, 100)                        # загадане число
count = func_task_1.begin_game(find,count)           # передаємо значення і отримуємо кількість спроб
print(f"WIN!!!, you guessed it from {count} attempts")
print(func_task_1.begin_game.__doc__)


# Вміст додаткової імпортованої функції

#def begin_game():
#    """
#    Function for entering and checking the number for truth
#    
#    Result:
#    True(boolean)
#    """
#    global find
#    global count    
#    number = int(input("Please, enter the number from 0 to 100: "))  # Отримує число
#    count += 1                                                       # Індикатор спроб +1 
#    if number > find:                                                # Перевіряє і виводить підказки
#        print("Your number is too big")                              #
#    elif number < find:                                              #
#        print("Your number is too small")                            #
#    if count == 3:                                                   # Додаткова підказка 
#        print ("I give another hint: {} > number < {}".format(round(find-10,-1), round(find+10,-1))) 
#    return True if number is find else begin_game()
