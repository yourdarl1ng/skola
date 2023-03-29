import tkinter


#vytvorenie kanvasu
c = tkinter.Canvas()
#predny vagon abo co , idk zevraj to mam mat >~<
def predny_vagon():
    for i in range(15):
        posun = 3*i
        c.create_line(30+posun, 0, 31+posun, 15)
    c.create_rectangle(15, 0, 25, 20, fill="black")
    c.create_rectangle(50, 40, 55, 45)
    c.create_rectangle(0, 10, 95, 50, fill="red")
    c.create_rectangle(65, 18, 95, 35, fill="green")
    c.create_rectangle(50, 18, 90, 35, fill="green")
    c.create_oval(20, 40, 40, 60, fill="black")
    c.create_oval(50, 40, 70, 60, fill="black")
#funkcia ktora zrobi autobus >w<
def autobus(posun):
    #telo
    c.create_rectangle(95+posun, 40, 100+posun, 45)
    c.create_rectangle(100+posun, 10, 200+posun, 50, fill="red")
    #okna
    c.create_rectangle(110+posun, 18, 145+posun, 35, fill="green")
    c.create_rectangle(155+posun, 18, 190+posun, 35, fill="green")
    #kolesa
    c.create_oval(115+posun, 40, 135+posun, 60, fill="black")
    c.create_oval(165+posun, 40, 185+posun, 60, fill="black")

#cyklus
predny_vagon()
for cyklus in range(5):
    separator = 105*cyklus
    autobus(separator)
c.pack()
