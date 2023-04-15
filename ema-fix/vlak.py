import tkinter


#vytvorenie kanvasu
c = tkinter.Canvas(width=600, height=600)

#rusen
def rusen():
    #hlavne telo
    c.create_rectangle(5,250,95,305, fill='green')
    #okno
    c.create_rectangle(5,260,35,280, fill='blue')
    #komin 1
    c.create_rectangle(15,230,40,250, fill='yellow')
    #komin 2
    c.create_rectangle(50,210,85,250, fill='orange')

def kolesa(medzera):
    c.create_oval(7+medzera, 300, 27+medzera, 320,fill='black')

#funkcia na pokracovanie, vagonov
def vagon(posun):
    #telo
    c.create_rectangle(95+posun, 300, 100+posun, 305)
    c.create_rectangle(100+posun, 270, 200+posun, 310, fill="green")
    #okna
    c.create_rectangle(110+posun, 278, 145+posun, 295, fill="blue")
    c.create_rectangle(155+posun, 278, 190+posun, 295, fill="blue")
    #kolesa
    c.create_oval(115+posun, 300, 135+posun, 320, fill="black")
    c.create_oval(165+posun, 300, 185+posun, 320, fill="black")


rusen()
#cykly
#kolesa na rusni
for i in range(3):
    medzera = 30*i
    kolesa(medzera)
#vagony
for i in range(5):
    posunutie = 105*i
    vagon(posunutie)
#dym z komina
for i in range(80):
    posun = 6*i
    c.create_line(55+posun, 180, 60+posun, 200)
c.pack()

