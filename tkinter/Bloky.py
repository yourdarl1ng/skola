import tkinter
import random
width = 400
height = 400
canvas=tkinter.Canvas(width=width,height=height)
canvas.pack()
farby=["red"]
bod = {"x":width/2, "y":height/2}
blok1 = {"x":range(0, 200), "y":range(0,200)}
blok2 = {"x":range(200, 400), "y":range(0,200)}
blok3 = {"x":range(0, 200), "y":range(200,400)}
blok4 = {"x":range(200, 400), "y":range(200,400)}
def ciara1(suradnice):
    farba=random.choice(farby)
    owo=False
    uwu = False
    for s in blok1["x"]:
        if suradnice.x == s:
            owo=True
    for s in blok1["y"]:
        if suradnice.y == s:
            uwu=True
    if uwu and owo:

        canvas.create_line(bod["x"],bod["y"],suradnice.x,suradnice.y, fill='red')
    owo2=False
    uwu2 = False
    for s in blok2["x"]:
        if suradnice.x == s:
            owo2=True
    for s in blok2["y"]:
        if suradnice.y == s:
            uwu2=True
    if uwu2 and owo2:

        canvas.create_line(bod["x"],bod["y"],suradnice.x,suradnice.y, fill='blue')
    owo3=False
    uwu3 = False
    for s in blok3["x"]:
        if suradnice.x == s:
            owo3=True
    for s in blok3["y"]:
        if suradnice.y == s:
            uwu3=True
    if uwu3 and owo3:

        canvas.create_line(bod["x"],bod["y"],suradnice.x,suradnice.y, fill='green')
    owo4=False
    uwu4 = False
    for s in blok4["x"]:
        if suradnice.x == s:
            owo4=True
    for s in blok4["y"]:
        if suradnice.y == s:
            uwu4=True
    if uwu4 and owo4:

        canvas.create_line(bod["x"],bod["y"],suradnice.x,suradnice.y, fill='yellow')
    
canvas.bind("<Button-1>", ciara1)
