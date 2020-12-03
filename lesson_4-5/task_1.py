
number = int(input("Введіть число: "))
f = 1

if number == 0:
    print(f"{number}! = 1")
else:
    for i in range(2,number+1):
        f *= i 
    print(f"{number}! = {f}") # Виводить: 8! = 40320






# --- НАОЧНИЙ ВАРІАНТ (Оформлено наочне відобаження добутку елементів факторіалу)
f = 1
if number == 0:
    print(f"{number}! = 1")
else:
    print(f, end=" ")
    for i in range(2,number+1):
        f *= i 
        print("*", i, end=" ")
    print(f"= {number}! = {f}") # Виводить: 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 = 8! = 40320