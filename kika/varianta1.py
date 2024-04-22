# Importujeme kniznicu random
import random 
# Vytvorime novu premennu string
# V nej ulozime vstup pouzivatela
string = input("Zadajte vetu: ")

# Definujeme novu funkciu s menom nahodne_pismenko
# Funkcia si pyta argument string (velmi dolezite)
def nahodne_pismenko(string):
    # V premennej vystup ulozime vystup funkcie, zatial prazdny
    vystup = ""

    # Zaciatok slucky for
    # Zmerame dlzku retazca, a ideme cez jeho indexy za pomoci funkcie range
    for char in range(len(string)):
        # Kazdu iteraciu pridame jedno nahodne pismenko do vystupu
        # Toto pismenko je vybrane na zaklade funkcie randrange z kniznice random
        # Funkcii randrange posunieme dlzku retazca a nechame ju vybrat nahodny index
        vystup+=string[random.randrange(len(string))]
    # Konciek slucky, vratime vystup funkcie
    return vystup
# Spustame funkciu s dosadenou premennou string za argument a vypisujeme jej vystup
print(nahodne_pismenko(string))
