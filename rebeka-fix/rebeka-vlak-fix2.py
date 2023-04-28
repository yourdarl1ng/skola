import tkinter
canvas= tkinter.Canvas(width=850, heigh=400, bg="white")
canvas.pack()


#rusen
canvas.create_rectangle(100,260,300,320, fill='red')
canvas.create_rectangle(190,260,300,200, fill='yellow')
canvas.create_rectangle(120,260,160,220, fill='orange')

for i in range(1,5):
    canvas.create_oval(i*50+50, 320, i*50+90, 360,fill='black')
    
#vagon
def vagon(x,y):
    canvas.create_rectangle(x+200, y+200, x+300, y+270,fill='lime')
    canvas.create_rectangle(x+180, y+250, x+200, y+260,fill='blue')
    canvas.create_oval(x+200, y+270, x+240, y+310,fill='black')
    canvas.create_oval(x+300, y+270, x+260, y+310,fill='black')
#vagon okna
    canvas.create_rectangle(x+215, y+210, x+245, y+230,fill='white')
    canvas.create_rectangle(x+255, y+210, x+285, y+230,fill='white')

for i in range(1,5):
    vagon(i*120,50)
    
#ciary
def ciary(x,y):
    canvas.create_line(x+105, y+130, x+120, y+160)
for i in range(1,7):
    ciary(i*5,50)
    
#okna
def okna(x,y):
    canvas.create_rectangle(x+135, y+160, x+175, y+190, fill='white')
for i in range(1,3):
    okna(i*60,50)
