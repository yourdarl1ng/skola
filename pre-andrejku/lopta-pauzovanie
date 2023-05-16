import tkinter
canvas = tkinter.Canvas(width=400, height=400) 
canvas.pack()
x=15
stop_var = False
def stop(args):
    global stop_var
    if stop_var:
        stop_var=False
    else:
        stop_var=True
def lopta():
    
    global x 
    
    if x >= 400:
        x=0
    if not stop_var:
        canvas.delete("all")
        x+=5 
        canvas.create_oval(x, 180, x+40, 220)

    canvas.after(200, lopta)
lopta()
canvas.bind("<Button-1>", stop)
