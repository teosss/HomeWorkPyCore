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
def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    #виводити рахунок в консоль незручно
    #зручніше його вивести на canvas
    #використавши функцію canv.create_text()
    canv.create_text(60,20,text="Score: "+str(points), font = 'Arial 20')
    
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)
     
     
def click(event):
    global points
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
 
points = 0
new_ball()
canv.bind('<Button-1>', click)
 
mainloop()