import tkinter
canvas = tkinter.Canvas(width=400, height=400) 
canvas.pack()
x=15
def lopta():
    canvas.delete("all")
    global x 
    x+=5 
    if x >= 400:
        x=0
    canvas.create_oval(x, 180, x+40, 220)
    canvas.after(200, lopta)
lopta()
