from enum import auto
import tkinter
import random as r

#vytvorenie kanvasu
c = tkinter.Canvas()

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
#chyba mi este predny vozen abo co
#cyklus
for cyklus in range(5):
    separator = 105*cyklus
    autobus(separator)
c.pack()
