#import kniznice tkinter
#syntax importu je [import <menokniznice>]
import tkinter
#import kniznice random
import random as r


#deklaracia(vytvorenie) premennej canvas, canvas drzi triedu Canvas() a jej funkcie
#syntax vytvorenia premennej je [meno_premennej = <hodnota>]

canvas = tkinter.Canvas()

#definicia funkcie na ciaru
#syntax definicie funkcie je [def menofunckie(argumenty):
#                                       kod funkcie
#                                       ]
def ciara():

    #zaciatocna vyska ciary(prve cislo je min vyska druhe je max vyska)
    #deklaracia premennej y_suradnica, premenna nabera hodnotu nahodneho cisla od 0 po 400. datovy typ premennej je int(celocislo)
    y_suradnica = r.randint(0, 400)
    #konecna vyska ciary
    #to iste tu
    y2_suradnica = r.randint(0, 400)
    #vyber farby
    #deklaracia premennej farba, premenna farba nabera hodnotu nahodne vybranej hodnoty(v tomto pripade farby). datovy typ premennej je str(retazec, alebo string. oboje nazvy su spravne)
    farba = r.choice(("red", "green", "blue", "black"))

    #prve x je nula aby sa ciara zacala uplne vlavo, a druhe x je 400 aby sa koncila uplne vpravo
    #druhe x si mozte zmenit podla sirky vasho kanvasu, ak ste sirku nemenily tak nechajte x napokoji

    #pouzivame funckie triedy tkinter.Canvas(), tym ze tkinter.Canvas() je drzany v premennej, tak tato premenna drzi vsetky jeho funkcie a 
    #tym padom mozeme rovno volat funkcie z canvas premennej. priklad-> tkinter.Canvas().create_line(dajake veci) , s premennou canvas je to jednoduchsie(pozr. riadok nizsie)
    canvas.create_line(0, y_suradnica, 400, y2_suradnica, fill=farba, width=1)
#cyklus ktory vytvori 10000 ciar
#cyklus for, riadiaca premenna i. pojde v slucke 10000 krat. funkcia range vytvara interval od->do. v tomto pripade sme nespecifikovali zaciatok tazke od nuly.
#range je vzdy -1. cize finalne cislo bude 9999 namiesto 10000 ale tym ze sa pocita od 0 tak cyklus sa naozaj zopakoval 10000 krat

#syntax for cyklu
#for <premenna> in <funkcia/list/premenna/slovnik/...>
for i in range(10000):
    #volanie funkcie ciara
    #syntax volania funkcie je <menofunkcie>() <- zatvorky su velmi dolezite inac by sa nezavolala
    #do zatvoriek mozme vkladat argumenty, napriklad pozdrav("Andrej") <- funkcia by pozdravila osobu s menom Andrej.
    #priklad funkcie pozdrav je na konci
    ciara()

canvas.pack()
#priklad funkcie pozdrav
#funkcia pyta argument meno, bez neho by nesla. argumenty mozeme specifikovat pri definicii funkcie
def pozdrav(meno):
    print(f"Ahoj {meno}!")
#dosadzame argument meno a volame funkciu
pozdrav("Andrej")
#podobny princip len netreba argument
def pozdrav2():
    #list mien v premennej mena, list mozes vytvorit hranatymi zatvorkami
    mena = ["Andrej", "Ema", "Jano", "Fero", "Michal", "Jozef", "neche sa mi vymyslat mena"]
    #pozdravi nahodne vybrane meno
    print(f"Ahoj {r.choice(mena)}!")
#volanie funkcie
pozdrav2()


