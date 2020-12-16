import func_task_1                                  # імпортуємо функцію перевірки співвідношення
    
count = 10                                          # лічильник кількості можливоих спроб спроб
result = func_task_1.begin_game(count)
if result != False:
    print(f"WIN!!!, you guessed it from {result} attempts")  # передаємо значення і отримуємо кількість спроб
else:
    print("YOU LOSE!!!") 
print(func_task_1.begin_game.__doc__)