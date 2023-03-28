#funkcia na pocitanie cisel
def kalkuluj(cisla):
    #skusy vypocitat priklad, ak narazi na chybu tak preskoci
    try:
        vysledok = eval(cisla)
        return vysledok
    except:
        return "daco sa podrbalo"
#cyklus na zadavanie prikladov
while True:
    priklad = input("priklad UwU ->")
    print(kalkuluj(priklad))
