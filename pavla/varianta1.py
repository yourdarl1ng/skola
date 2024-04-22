# Vytvorime novu premennu s nazvom string
# Ulozime v nej vstup od pouzivatela
string = input("Zadaj vetu: ")

# Definujeme novu funkciu s menom funkcia
# Tato funkcia si pyta argument retazec
def funkcia(retazec):
    # Vytvorime novu premennu vystup vo funkcii funkcia
    # Ulozime tu vystup funkcie, zatial prazdny
    vystup = ""
    # Zaciatok slucky for
    # Zmeriame dlzku retazca a nasledne ideme cez indexy
    for pismenko in range(len(retazec)):
        # Ak je dany index delitelny 2 a nieje 0 tak sa pozreme na dany index od konca
        if pismenko % 2 == 0 and pismenko != 0:
            # Ked sa nan pozreme(od konca preto -) tak ho pripiseme ku vystupu
            vystup+=retazec[-pismenko]
    # Koniec slucky, vraciame vystup
    return vystup
# Spustame funkciu funkcia s dosadenou premennou za argument
# A vypisujeme jej vystup
print(funkcia(string))
