
from tkinter import *
 

win=Tk()
 

win.geometry("700x350")
 
win.resizable(False,False)
 

canvas=Canvas(win, width=700, height=350)
canvas.pack()
 

ball=canvas.create_oval(10,10,50,50, fill="green3")
 

xspeed=yspeed=3
 
def move_ball():
   global xspeed, yspeed
 
   canvas.move(ball, xspeed, yspeed)
   (leftpos, toppos, rightpos, bottompos)=canvas.coords(ball)
   if leftpos <=0 or rightpos>=700:
      xspeed=-xspeed
 
   if toppos <=0 or bottompos >=350:
      yspeed=-yspeed
 
   canvas.after(30,move_ball)
 
canvas.after(30, move_ball)
 
win.mainloop()
