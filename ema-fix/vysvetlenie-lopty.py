#import knzinice tktiner
import tkinter
#deklaracia premennej canvas
canvas = tkinter.Canvas(width=400, height=400) 
#renderovanie okna(to co sa kresli)
canvas.pack()
#deklaracia premennej x, drzi hodnotu 15, je celociselna
x=15
#deklaracia premennej stop_var, drzi hodnotu True alebo False. datovy typ je boolean

stop_var = False
#definicia funkcie stop s argumentom args
def stop(args):
    #global tu je aby sme mohli pouzit premennu stop_var, musi tu byt lebo premenna bola deklarovana mimo funkcie
    global stop_var
    #if statement
    #if stop_var: a if_stop_var == True: su uplne tie iste. pouzil som len kratsiu verziu
    if stop_var:
        #zmena hodnoty
        stop_var=False
    #else su vsetky ostatne moznosti, nidky sa nedava podmienka do else
    #v tomto pripade to bude vzdy ked stop_var bude False
    else:
        #zmena hodnoty na True
        stop_var=True
#hlavna funkcia, tu budeme cyklit
def lopta():
    #global aby sme mohli pouzit premennu deklarovanu mimo funkcie
    global x 
    #ak x je vacsie alebo rovne 400(okraj obrazovky) tak resetujeme hodnotu x
    #takze lopta sa vrati nazad do lava
    if x >= 400:
        #zmena hodnoty
        x=0
    #ak stop_var sa rovna False tak lopta sa bude pohybovat
    #not znamena ze podmienka nenastala
    if not stop_var:
        #vymazanie vsetkeho na obrazovke
        canvas.delete("all")
        #pridanie 5 k pozicii lopty, toto ju hybe
        x+=5 
        #kreslenie lopty
        canvas.create_oval(x, 180, x+40, 220)
    #pocka 0.2 sekundy a znova zavola funkciu lopta(iba raz),ale tym ze je vnutry funkcie lopta tak ju
    # bude volat dokola takze sme vytvorili nekonecny cyklus pohybu lopty
    canvas.after(200, lopta)
#volanie funkcie lopta
lopta()
#bindovanie laveho tlacitla mysi na funkciu, vsimni si ze na funkciu stop len odkazujeme no nevolame(niesu tam zatvorky ktore by ju volali)

canvas.bind("<Button-1>", stop)

#priklady premennych
#drzi cislo bez desatinnych miest
celocislo = 5 
#drzi cislo s desatinnymi miestami
desatinne_cislo = 5.5 
#drzi hodnotu True/False
boolean_premenna = True 
boolean_premenna2 = False 
#list moze drzat set hocikolko a hociakych hodnot
#v tomto pripade je to string - retazec, int(nema desatiny) - celocislo, float(desatinne miesta) - cislo s desatinamy, boolean
list_premenna = ["Andrej", 18, 19.5, True]
#for cyklus postupne prejde kazdou hodnotou a vypise ju
for hodnota in list_premenna:
    #vypisovanie hodnoty
    print(hodnota)
#ine datove typy sme nebrali tak ich tu nebudem davat
