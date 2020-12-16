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
######################################################
def new_ball():
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)
######################################################### 

 #додали обробку події click
 #     

def click(event):
    print('click the button')   
     
#############################################

new_ball()

#canv.bind зв'язує між собою декілька подій

canv.bind('<Button-1>', click)
mainloop()