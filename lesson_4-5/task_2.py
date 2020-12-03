# --- ДОДАТКОВА функція для введення цілочисельного списку ---
def input_list():
    while True:
        
        list_new = input("Ввведіть через пробіл цілочисельних цифри: ")
        list_new = list_new.split(" ")                # розбиваємо стрічку на елементи
        
        for i in range(0, len(list_new)):             # проходить через усі елементи від 0 до довжини списку
            try:                                      # перевіряє чи не має помилки у списку
                list_new[i] = int(list_new[i])        # конвертує елементи у тип integer
            except ValueError:                        # виводить помилку
                print("Помилка! '", list_new[i],"' не є цілочисельним числом")
                break
        
        return list_new                               # повертає готовий цілочисельний список

# --- ОСНОВНА ПРОГРАМА ---

#list = input_list()                                # вводимо стрічку вручну

list = [3, 21, 5, 9, 12, 214, 53, 6, 5, 1, 100, 13] # задаємо список у коді
print("Внесений список: ", list)

for i in range(0, len(list)):             # проходимо через усі елементи від 0 до довжини списку
    list[i] = float(list[i]) 

print("Конвертований список: ", list)



