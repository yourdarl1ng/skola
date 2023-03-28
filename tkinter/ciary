import tkinter
import random as r

#vytvorenie kanvasu
c = tkinter.Canvas()

#funkcia ktora zrobi 1 lajnu
def line(x1, y1, x2, y2, width=int, fill=str):
    c.create_line(x1, y1, x2, y2, width=width, fill=fill)

for cyklus in range(10000):
    #zaciatocna vyska ciary(prve cislo je min vyska druhe je max vyska)
    y_suradnica = r.randint(0, 400)
    #konecna vyska ciary
    y2_suradnica = r.randint(0, 400)
    #vyber farby
    farba = r.choice(("red", "green", "blue", "black"))

    #prve x je nula aby sa ciara zacala uplne vlavo, a druhe x je 400 aby sa koncila uplne vpravo
    #druhe x si mozte zmenit podla sirky vasho kanvasu, ak ste sirku nemenily tak nechajte x napokoji
    line(0, y_suradnica, 400, y2_suradnica, fill=farba, width=1)
c.pack()
