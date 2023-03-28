import tkinter
import random as r

#vytvorenie kanvasu
c = tkinter.Canvas()

#funkcia ktora zrobi 1 lajnu
def line(x1, y1, x2, y2, width=int):
    c.create_line(x1, y1, x2, y2, width=width)
#funkcia ktora pise text
def txt(x, y, text=str):
    c.create_text(x, y, text=text)
#cyklus ktory prebehne 15 krat(generacia ciar)
for cycle in range(15):
    #oddelenie ciar, moze sa zvacsit pre vacsie rozostupy
    separator = 7*cycle 
    #pripocitavanie rozostupu k suradnicy x (sirka, y je vyska)
    x1 = 100+separator
    #generacia nahodnej hrubky ciary, druhe cislo v zatvorke je max hrubka
    rand = r.randint(1, 7)
    #kreslenie ciary
    line(x1=x1, y1=20, x2=x1, y2=100, width=rand)
#dajaky text co tam mame mat idk co tu ma byt napisane
txt(150, 10, "ISBN 219043112")
txt(150, 130, "ISBN 219043112")
#len na to aby sme vedeli ze vsetko prebelho uspesne, mozme zmazat
print("Done")
#vytvorenie okna, bez tohoto by sme nevideli co sa nakreslilo
c.pack()
