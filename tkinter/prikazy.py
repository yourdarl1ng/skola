import tkinter

canvas_objekt = tkinter.Canvas()

canvas_object.create_circle(x1, y1, x2, y2, fill=str(farba), width=int(cislo))

canvas_objekt.create_text(x, y, text=str(text))

canvas_objekt.create_oval(x1, y1, x2, y2, fill=str(text))

canvas_objekt.create_rectangle(x1, y1, x2, y2, fill=str(text))

canvas_objekt.create_line(x1, y1, x2, y2, width=width, fill=fill)
#funkcia ktora nabinduje lave tlacitko(asi, mozno prave) a spusti funkciu ked sa stali
canvas_objekt.bind('<Button-1>', funkcia)
#to iste len na klavesnicu
canvas_objekt.bind_all('s', funkcia)

#generuje interval od 0 po 4,
 prejde nim a vypise cislo na ktorom je
for slovo in range(5):
    
    print(slovo)
