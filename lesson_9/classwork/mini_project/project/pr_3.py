from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Сaught the BALL")
 
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
#використання global не найкраща ідея
#краще використовувати ООП
#global означає, що змінні будуть 
#вважатися глобальними, і їх 
# значення збережеться і після 
# завершення роботи функції, а не буде
# знищене як це станеться з усіма локальними 
# змінними після завершення виконання функції

#################################################3
def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)
#######################################################
     
 #щоб визначити, чи попали ми в круг,
 # необхідно знати його координати, 
 # радіус круга і координати мишки в момент кліку.
 # Координати мишки легко отримати через 
 # event.x, event.y.    
def click(event):
    print(x,y,r)    
    


new_ball()
canv.bind('<Button-1>', click)
mainloop()