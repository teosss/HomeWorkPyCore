from add.login import *
from PIL import ImageTk, Image as PILimage
import random

# class Сoordinate():
#   def __init__(self, x = 0, y = 0):
#        self.x = x
#        self.y = y
   
class Player():
    def __init__(self, name_1, name_2):
        self.name_1 = name_1
        self.name_2 = name_2

GAME = Tk()

game_window = Сoordinate(400, 400)          # розмір вікна
field_size = Сoordinate(zone, zone)         # розмір поля для гри
step = Сoordinate()                         # крок для поля
menu = Сoordinate()                         # розмір і параметри меню
player_zone = Сoordinate()                  # зона для взаємодії в межах сітки  
players = Player(login_name_1, login_name_2)# зараємо імена гравців

game_running = True
move_player = False

step.x = game_window.x // field_size.x  # задаємо крок по горизонталі
step.y = game_window.y // field_size.y  # задаємо крок по вертикалі

game_window.x = step.x * field_size.x   # вирівнюємо розмір вікна відповідно до розміру поля
game_window.y = step.y * field_size.y   # 

delta_menu_x = field_size.x            # ширина у кроках відділу де меню

water_color = "#7FC9FF"
grey_color = "#AAAAAA"
win_color = "#FFD800"

player_1_boom = 0                       # ініціалізуємо кількість попадань 1 гравця
player_2_boom = 0                       # ініціалізуємо кількість попадань 2 гравця
next_step = 1                           # лічильник ходу гри
ship_total = 0                          # кількість клітинок кораблів

menu.x = step.x * delta_menu_x          # розмір меню по ширині
menu.y = 40                             # розмір меню по висоті 

ships = field_size.x // 2               # Визначаємо максимальну кількість кораблів:
ship_len1 = 1           # довжина першого типу корабля
ship_len2 = 2           # довжина другого типу корабля
ship_len3 = 3           # довжина третього типу корабля

img = PILimage.open(r"images\fire.gif")
img = img.resize((step.x,step.y), PILimage.ANTIALIAS)
fire_img =  ImageTk.PhotoImage(img)


enemy_ships1 = [[0 for i in range(field_size.x + 1)] for i in range(field_size.y + 1)]

enemy_ships2 = [[0 for i in range(field_size.x + 1)] for i in range(field_size.y + 1)]

list_objects = []       # список об'єктів canvas

points1 = [[-1 for i in range(field_size.x)] for i in range(field_size.y)] # points1 - Визначає куди натиснули мишкою  в поле 1

points2 = [[-1 for i in range(field_size.x)] for i in range(field_size.y)] # points2 - Визначає куди натиснули мишкою в поле 2

boom = [[0 for i in range(field_size.x)] for i in range(field_size.y)] # boom - список влучень по кораблях ворога


ships_list = []      # ships_list - список кораблів першого і другого гравця

def game_close():
    """
    Функція для виходу з гри через Х
    """                   
    global game_running
    if messagebox.askokcancel("Sea Battle | EXIT", "Бажаєте вийти з гри?"):
        game_running = False
        GAME.destroy()


GAME.protocol("WM_DELETE_WINDOW", game_close)     # функція на вихід з гри
GAME.title("Sea Battle | Game")                   # назва гри
GAME.resizable(0, 0)                              # параметер на зміну розміру вікна
GAME.wm_attributes("-topmost", 1)                 # параметер по видимсть поверх інших вікон
canvas = Canvas(GAME, width=game_window.x + menu.x + game_window.x, height=game_window.y + menu.y, bd=0, highlightthickness=0) 
# задаємо основу для ігрового вікна
zone1 = canvas.create_rectangle(0, 0, game_window.x, game_window.y, fill=water_color)  # Поле гравця 1                           
zone2 = canvas.create_rectangle(game_window.x + menu.x, 0, game_window.x + menu.x + game_window.x, game_window.y,fill=water_color)                                      # Поле гравця 2
canvas.pack()
GAME.update()


def draw_table(offset_x=0):                        # функція створює лінії вертикальні й горизонтальні
    """
    Функція для рисування ліній полів
    """  
    for i in range(0, field_size.x + 1):
        canvas.create_line(offset_x + step.x * i, 0, offset_x + step.x * i, game_window.y)
    for i in range(0, field_size.y + 1):
        canvas.create_line(offset_x, step.y * i, offset_x + game_window.x, step.y * i)

draw_table()                            # малюємо лінії для першого поля      
draw_table(game_window.x + menu.x)      # малюємо лінії для другого поля


t0 = Label(GAME, text=players.name_1, font=("Helvetica", 16))
t0.place(x=game_window.x // 2 - t0.winfo_reqwidth() // 2, y=game_window.y + 3)
t1 = Label(GAME, text=players.name_2, font=("Helvetica", 16))
t1.place(x=game_window.x + menu.x + game_window.x // 2 - t1.winfo_reqwidth() // 2, y=game_window.y + 3)

def turn_player(igrok_mark_1):
    """
    Функція для перерисування черги ходів активного і пасивного гравця
    """  
    if  igrok_mark_1:
        t0.configure(fg="red")
        t1.configure(fg=grey_color)
        canvas.itemconfig(zone2,fill=grey_color)
        canvas.itemconfig(zone1,fill=water_color)                                                      
    else:
        t1.configure(fg="red")
        t0.configure(fg=grey_color)
        canvas.itemconfig(zone2,fill=water_color)
        canvas.itemconfig(zone1,fill=grey_color)                              

turn_player(move_player)

def button_show_enemy1():               # функція для дебагу (відобразити кораблі 1 гравця)
    """
    Функція для відображення розташування кораблів гравця 1
    """  
    for i in range(0, field_size.x):   
        for j in range(0, field_size.y):
            if enemy_ships1[j][i] > 0:
                color = "red"
                if points1[j][i] != -1:
                    color = "green"
                _id = canvas.create_rectangle(i * step.x, j * step.y, i * step.x + step.x, j * step.y + step.y, fill=color)
                list_objects.append(_id)


def button_show_enemy2():            # функція для дебагу (відобразити кораблі 2 гравця)
    """
    Функція для відображення розташування кораблів гравця 2
    """  
    for i in range(0, field_size.x):
        for j in range(0, field_size.y):
            if enemy_ships2[j][i] > 0:
                color = "red"
                if points2[j][i] != -1:
                    color = "green"
                _id = canvas.create_rectangle(game_window.x + menu.x + i * step.x, j * step.y,
                                              game_window.x + menu.x + i * step.x + step.x, j * step.y + step.y,
                                              fill=color)
                list_objects.append(_id)


def button_begin_again():           # функція для перезапуску гри
    """
    Функція для очитки полів від елементів при початку нової гри
    """  
    global list_objects
    global points1, points2
    global boom, next_step
    global enemy_ships1, enemy_ships2
    
    next_step = 1                         
    Player_turn.configure(text=f"Зараз {next_step} хід")
    
    for element in list_objects:
        try:
            canvas.delete(element)
        except:
            element.destroy()
    list_objects = []
    generate_ships_list()
    # print(ships_list)
    enemy_ships1 = generate_enemy_ships()
    enemy_ships2 = generate_enemy_ships()
    points1 = [[-1 for i in range(field_size.x)] for i in range(field_size.y)]
    points2 = [[-1 for i in range(field_size.x)] for i in range(field_size.y)]
    boom = [[0 for i in range(field_size.x)] for i in range(field_size.y)]


b0 = Button(GAME, text=f"Відобразити кораблі {players.name_1}", command=button_show_enemy1)
b0.place(x=game_window.x + menu.x / 4, y=30)

b1 = Button(GAME, text=f"Відобразити кораблі {players.name_2}", command=button_show_enemy2)
b1.place(x=game_window.x + menu.x / 4, y=70)

b2 = Button(GAME, text="Почати заново", command=button_begin_again)
b2.place(x=game_window.x + menu.x / 4 + 50, y=110)

Player_turn = Label(GAME, text=f"Зараз {next_step} хід", font=("Helvetica", 12))
Player_turn.place(x=game_window.x + menu.x / 4 + 50, y=150)

Generate_ship = Label(GAME, font=("Helvetica", 11))
Generate_ship.place(x=game_window.x + menu.x // 3 + 20 , y=175)

Player_hits_1 = Label(GAME, font=("Helvetica", 10))
Player_hits_1.place(x=game_window.x + 20 , y=200)

Player_hits_2 = Label(GAME, font=("Helvetica", 10))
Player_hits_2.place(x=game_window.x + 20 , y=220)


def draw_point(x, y):              
    """
    Функція рисує на вибрій клітинці об'єкт для першого гравця
    """  
    global player_1_boom
    if enemy_ships1[y][x] == 0:
        color = "white"
        id1 = canvas.create_rectangle(x * step.x, y * step.y, x * step.x + step.x, y * step.y + step.y, fill=color)

        list_objects.append(id1)
    
    if enemy_ships1[y][x] > 0:
        player_1_boom -= 1
        color = "red"
        Player_hits_1.configure(text=f"{players.name_1} -- залишилось {player_1_boom}")
        id1 = canvas.create_rectangle(x * step.x, y * step.y, x * step.x + step.x, y * step.y + step.y, fill=color)        
        id2 = canvas.create_image(x * step.x, y * step.y, image=fire_img, anchor=NW)

        list_objects.append(id1)
        list_objects.append(id2)


def draw_point2(x, y, offset_x=game_window.x + menu.x):   
    """
    Функція рисує на вибрій клітинці об'єкт для другого гравця
    """  
    global player_2_boom
    if enemy_ships2[y][x] == 0:
        color = "white"
        id1 = canvas.create_rectangle(offset_x + x * step.x, y * step.y, offset_x + x * step.x + step.x, y * step.y + step.y, fill=color)

        list_objects.append(id1)

    if enemy_ships2[y][x] > 0:
        player_2_boom -= 1
        color = "red"
        Player_hits_2.configure(text=f"{players.name_2} -- залишилось {player_2_boom}")
        id1 = canvas.create_rectangle(offset_x + x * step.x, y * step.y, offset_x + x * step.x + step.x, y * step.y + step.y, fill=color)
        id2 = canvas.create_image(offset_x + x * step.x, y * step.y, image=fire_img, anchor=NW)        
        list_objects.append(id1)
        list_objects.append(id2)


#def check_winner(x, y):
#    """
#    Функція перевіряє чи гравець задовільнив умови перемоги
#   """  
#    win = False
#    if enemy_ships1[y][x] > 0:
#        boom[y][x] = enemy_ships1[y][x]
#    sum_enemy_ships1 = sum(sum(i) for i in zip(*enemy_ships1))
#    sum_boom = sum(sum(i) for i in zip(*boom))
#    # print(sum_enemy_ships1, sum_boom)
#    if sum_enemy_ships1 == sum_boom:
#        win = True
#    return win


def check_winner2():
    """
    Функція перевіряє чи гравець 1 задовільнив умови перемоги
    """  
    win = True
    for i in range(0, field_size.x):
        for j in range(0, field_size.y):
            if enemy_ships1[j][i] > 0:
                if points1[j][i] == -1:
                    win = False
    return win


def check_winner2_igrok_2():
    """
    Функція перевіряє чи гравець 2 задовільнив умови перемоги
    """  
    win = True
    for i in range(0, field_size.x):
        for j in range(0, field_size.y):
            if enemy_ships2[j][i] > 0:
                if points2[j][i] == -1:
                    win = False
    return win


def add_to_all(event):
    global points1, points2, move_player, next_step
    _type = 0  # ЛКМ
    if event.num == 3:
        _type = 1  # ПКМ
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
 
    player_zone.x = mouse_x // step.x
    player_zone.y = mouse_y // step.y

    # перше ігрове поле
    if player_zone.x < field_size.x and player_zone.y < field_size.y and move_player:
        if points1[player_zone.y][player_zone.x] == -1:
            points1[player_zone.y][player_zone.x] = _type
            move_player = False
            next_step += 1                          # підрахунок ходу гравців
            Player_turn.configure(text=f"Зараз {next_step} хід")
            draw_point(player_zone.x, player_zone.y)
            if check_winner2():
                move_player = True                
                win_back = canvas.create_rectangle(game_window.x + menu.x, 0, game_window.x + menu.x + game_window.x, game_window.y, fill=water_color)
                win = Label(GAME, text="WIN!",fg=win_color, font=("Helvetica", 60))
                win.configure(bg=water_color)
                win.place(x=game_window.x + menu.x + game_window.x // 3, y=game_window.y // 2.5)
            
                list_objects.append(win_back)
                list_objects.append(win)
                print("Перемога гравця №2")
                points1 = [[10 for i in range(field_size.x)] for i in range(field_size.y)]
                points2 = [[10 for i in range(field_size.x)] for i in range(field_size.y)]

    # друге ігрове поле
    if player_zone.x >= field_size.x + delta_menu_x and player_zone.x <= field_size.x + field_size.x + delta_menu_x and player_zone.y < field_size.y and not move_player:
        if points2[player_zone.y][player_zone.x - field_size.x - delta_menu_x] == -1:
            points2[player_zone.y][player_zone.x - field_size.x - delta_menu_x] = _type
            move_player = True
            draw_point2(player_zone.x - field_size.x - delta_menu_x, player_zone.y)
            # if check_winner(player_zone.x, player_zone.y):
            if check_winner2_igrok_2():
                move_player = False
                win_back = canvas.create_rectangle(0, 0, game_window.x, game_window.y, fill=water_color)
                win = Label(GAME, text="WIN!",fg=win_color, font=("Helvetica", 60))
                win.configure(bg=water_color)
                win.place(x=game_window.x // 3, y=game_window.y // 2.5)
                
                list_objects.append(win_back)
                list_objects.append(win)
                print("Перемога гравця №1")
                points1 = [[10 for i in range(field_size.x)] for i in range(field_size.y)]
                points2 = [[10 for i in range(field_size.x)] for i in range(field_size.y)]

    turn_player(move_player)
    

def generate_ships_list(): # функція генерує кораблів
    global ships_list
    ships_list = []
    for i in range(0, ships):
        ships_list.append(random.choice([ship_len1, ship_len2, ship_len3]))


def generate_enemy_ships(): 
    global ships_list, ship_total, player_1_boom, player_2_boom
    enemy_ships = []

    # підрахунок загальної довжини кораблів
    sum_1_all_ships = sum(ships_list)
    sum_ships = 0


    while sum_ships != sum_1_all_ships:
        # онуляємо масив кораблів 
        enemy_ships = [[0 for i in range(field_size.x)] for i in
                       range(field_size.y)]  # +1 для доп. линии справа и снизу, для успешных проверок генерации противника

        for i in range(0, ships):
            len = ships_list[i]
            horizont_vertikal = random.randrange(1, 3)  # 1- горизонтальний 2 - вертикальний

            primerno_x = random.randrange(0, field_size.x)
            if primerno_x + len > field_size.x:
                primerno_x = primerno_x - len

            primerno_y = random.randrange(0, field_size.y)
            if primerno_y + len > field_size.y:
                primerno_y = primerno_y - len

            # print(horizont_vertikal, primerno_x,primerno_y)
            if horizont_vertikal == 1:
                if primerno_x + len <= field_size.x:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                               enemy_ships[primerno_y][primerno_x + j] + \
                                               enemy_ships[primerno_y][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j]
                            # print(check_near_ships)
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y][primerno_x + j] = i + 1  # записываем номер корабля
                        except Exception:
                            pass
            if horizont_vertikal == 2:
                if primerno_y + len <= field_size.y:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                               enemy_ships[primerno_y + j][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                               enemy_ships[primerno_y + j][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j][primerno_x - 1]
                            # print(check_near_ships)
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y + j][primerno_x] = i + 1  # зберігаємо номер корабля
                        except Exception:
                            pass

        # підраховуємо кількість
        sum_ships = 0
        for i in range(0, field_size.x):
            for j in range(0, field_size.y):
                if enemy_ships[j][i] > 0:
                    sum_ships = sum_ships + 1
    ship_total = sum_ships
    player_1_boom = sum_ships
    player_2_boom = sum_ships
    Player_hits_1.configure(text=f"{players.name_1} -- залишилось {ship_total}")
    Player_hits_2.configure(text=f"{players.name_2} -- залишилось {ship_total}")
    Generate_ship.configure(text=f"Створено {ship_total}")
    return enemy_ships

generate_ships_list()

enemy_ships1 = generate_enemy_ships()
enemy_ships2 = generate_enemy_ships()


canvas.bind_all("<Button-1>", add_to_all)  # ЛКМ
canvas.bind_all("<Button-3>", add_to_all)  # ПКМ

while game_running:
    if game_running:
        GAME.update_idletasks()
        GAME.update()
    time.sleep(0.005)