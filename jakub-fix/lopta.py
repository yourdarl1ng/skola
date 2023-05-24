import tkinter
canvas = tkinter.Canvas(width=400, height=400) 
canvas.pack()
x=-40
x2=400
stop_var = False
def stop(args):
    global stop_var
    if stop_var:
        stop_var=False
    else:
        stop_var=True
def lopta():
    
    global x 
    global x2
    if x >= 400:
        x=0
    if x2 <=-10:
        x2=400
    if not stop_var:
        canvas.delete("all")
        x+=5
        x2-=5
        canvas.create_oval(x, 180, x+40, 220)
        canvas.create_oval(x2, 260, x2+40, 300)
    canvas.after(15, lopta)
lopta()
canvas.bind("<Button-1>", stop)
