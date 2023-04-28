import tkinter
import random as r
canvas= tkinter.Canvas(width=600,height=600)
canvas.pack()



for i in range(160):
    farba=r.choice(('red','blue','green'))
    y=r.randint(0,600)
    x=0
    canvas.create_line(x,y,650,x+r.randint(0,600),fill=farba)
