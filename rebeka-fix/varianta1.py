# Vytvorili sme novu premennu s menom text
# V tejto premennej ulozime text od pouzivatela
text = input("Zadaj vetu: ")

# Definujeme funkciu s menom vypis
# Tato funkcia si pyta argument menom veta
def vypis(veta):
    # Vytvorili sme novu premennu vo funkcii vypis
    # V tejto premennej ulozime vystup funkcie, zatial prazdny
    f = ""
    # Zaciatok slucky for
    # Ideme postupne cez indexy vety, 0 1 2 3 atd
    for pismeno in range(len(veta)):
        # Ak je index delitelny 2 tak sa pozreme ake pismeno sa na 
        # danom indexe nachadza a pripiseme ho do premennej f
        if pismeno % 2 == 0:
            f += veta[pismeno]
    # Po skonceni slucky vratime vystup funkcie
    return f 
# Spustime funkciu vypis s dosadenou premennou za argument
# A vypiseme jej vystup
print(vypis(text))
