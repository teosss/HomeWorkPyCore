def print_label(status, variable_1, variable_2):
    print("Змінна 1 %s змін: %d" % (status, variable_1))
    print("Змінна 2 %s змін: %d" % (status, variable_2))


variable_1 = int(input("Введіть змінну 1: "))
variable_2 = int(input("Введіть змінну 2: "))
first_status = "до"
second_status = "після"

print("Міняємо місцями змінні 1 і 2 без використання буферної третьої змінної \n -- v1 Спосіб 1 - додаємо між собою")

print_label(first_status, variable_1, variable_2) # до

variable_1 += variable_2
variable_2 = variable_1 - variable_2 
variable_1 -= variable_2

print_label(second_status, variable_1, variable_2) # після

print(" -- v2 Спосіб 2 - множимо їх")

print_label(first_status, variable_1, variable_2) # до

variable_1 *= variable_2
variable_2 = variable_1 / variable_2 
variable_1 /= variable_2

print_label(second_status, variable_1, variable_2) # після

print(" -- v3 Спосіб 3 -  ділимо їх")

print_label(first_status, variable_1, variable_2) # до

variable_1 /= variable_2
variable_2 *= variable_1
variable_1 = int(variable_2 / variable_1)
variable_2 = int(variable_2)  # конвертував для наступного виразу

print_label(second_status, variable_1, variable_2) # після

print(" -- v4 Спосіб через стрічку та список")

print_label(first_status, variable_1, variable_2) # до

variable_1 = str(variable_1)
variable_2 = str(variable_2) + "," + variable_1 
variable_2 = variable_2.split(",")
variable_1 = int(variable_2[0])
variable_2 = int(variable_2[1])

print_label(second_status, variable_1, variable_2) # після


print(" -- v5 ")

print_label(first_status, variable_1, variable_2) # до

variable_2, variable_1, =  variable_1, variable_2

print_label(second_status, variable_1, variable_2) # після
