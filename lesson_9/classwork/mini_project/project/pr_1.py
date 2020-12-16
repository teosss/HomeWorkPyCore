# tkinter бібліотека для розробки графічного інтерфейсу

from tkinter import *
from random import randrange as rnd 
from random import choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна

root.title("Сaught the BALL")

#створ. об'єкт класу canvas

canv = Canvas(root,bg='white')

#pack пакувальник, який дозволяє розміщати 
#зображення одне за одним
#fill=BOTH дозволяє заповнювати все доступне місце і по ширині і по висоті
# expand=1 при розширенні вікна мітка завжди буде посередині 

canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
###################################################
def new_ball():
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    
    #(x-r,y-r)-координати верхнього лівого кута
    #(x+r,y+r)- координати нижнього правого кута
    #квадрата, в якому промальовується коло

    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    
    #root.after(1000,new_ball) 
    # через 1000 мілісек викон.
    # функцію  new_ball()
    
    root.after(1000,new_ball)
    
#######################################################     

new_ball()


mainloop()