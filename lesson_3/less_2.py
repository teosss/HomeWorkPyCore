# ----- Function Input Number ----- #  
def init_number(number_of_digits):           # функція для отримання чотиризначного числа
    while True:
        number_xxxx = input("Введіть %d-значне натуральне число: " % number_of_digits)
        try:                                 # перевіряє чи не буде помилки із введеним числом (слова й спецсимволи)
            numerosity = len(number_xxxx)    # записуємо кількість символів у стрічці(числі)
            number_xxxx = int(number_xxxx)   # конвертує стрічку у числове значення, якщо на цьому етапі помилка переходимо у except 
            if (numerosity == number_of_digits): # перевіряє кількість символів
                return number_xxxx           # повертає ПІДТВЕРДЖЕНЕ значення
            else:
                print("!!! - Ви ввели не %d-значне число, а %s-значне" % (number_of_digits, numerosity))
        except ValueError:                   # якщо виникла помилка і виводимо повідомлення
             print("!! - Ви ввели не число або воно не натуральне")

# ----- Function Add in String ----- #  
def function_add_string(list_new,number_of_digits):
    list_add = ' '                           # задаємо стрічці, у яку склеюватимемо цифри початкове значення
    for i in range(number_of_digits):        # 
       list_new[i] = str(list_new[i])        # конвертує кожен символ у цифру
       list_add += list_new[i]               # повертаємо основній програмі значення   
    return list_add

# ----- MAIN ----- #  
number_of_digits = 4                         # задаємо скільки цифр має мати число

got_number = init_number(number_of_digits)   # викликає функцію init_number для отримання чотиризначного числа
numbers_list = list(str(got_number))         # конвертує String на список з цифр як символів

# ----- 2.1 ----- #
product_of_numbers = 1                       #  задаємо початкове значення для добутку цифр одержаного числа

for i in range(number_of_digits):            # 
   numbers_list[i] = int(numbers_list[i])    # конвертує кожен символ у цифру
   product_of_numbers *= numbers_list[i]     # поки виконується цикл перемножує цифри списку

print("Добуток цифр числа \"%d\" складає - %d" %(got_number, product_of_numbers))

# ----- 2.2 ----- #
numbers_list.reverse()                       # здійснює реверс списку
print("Реверс числа \"%d\" -- %s" %(got_number, function_add_string(numbers_list,number_of_digits) ))

# ----- 2.3 ----- #
numbers_list.sort()                          # здійснює сортування списку
print("Відсортований список: %s" % function_add_string(numbers_list,number_of_digits))


