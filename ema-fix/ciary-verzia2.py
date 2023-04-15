#import kniznic
import tkinter
import random as r


#vytvorenie kanvasu
canvas = tkinter.Canvas()
#funkcia ktora obsahuje cyklus
def cyklus():
    #cyklus ktory vytvori 10000 ciar
    for i in range(10000):
        #zaciatocna vyska ciary(prve cislo je min vyska druhe je max vyska)
        y_suradnica = r.randint(0, 400)
        #konecna vyska ciary
        y2_suradnica = r.randint(0, 400)
        #vyber farby
        farba = r.choice(("red", "green", "blue", "black"))

        #prve x je nula aby sa ciara zacala uplne vlavo, a druhe x je 400 aby sa koncila uplne vpravo
        #druhe x si mozte zmenit podla sirky vasho kanvasu, ak ste sirku nemenily tak nechajte x napokoji
        canvas.create_line(0, y_suradnica, 400, y2_suradnica, fill=farba, width=1)
#pustenie funkcie, cyklus sa zacne a ciary sa nakreslia
cyklus()

canvas.pack()
