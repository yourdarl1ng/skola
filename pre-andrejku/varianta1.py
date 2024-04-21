# Tu vytvorime premennu do ktorej ulozime vetu ktoru pouzivatel zada
veta = input("Zadaj vetu na prehod: ")

# Tu definujeme funkciu s menom prehod
# Tato funkcia si pyta argument s menom veta
# Funkcia funguje na zaklade slucky for
# Postupne ide slovo po slove, precita ich od zadu a prida do vystupu
# Potom vystup vrati

# V principe cita slova odzadu ale neprehazduje ich poradie

def prehod(veta):

    # Tu v tejto premennej ulozime finalny vystup funkcie, zatial je prazdny
    vystup = ""

    # Tu zacina slucka for
    # Najprv rozdelime vetu tam kde su medzery (preto funkcia split())
    # V riadiacej premennej slovo sa ulozi nase aktualne slovo
    # Postupne sa bude menit
    for slovo in veta.split():
        # Zapiseme do premennej vystup slovo od zadu a
        # jednu medzeru(kedze potom by bol vystup bez medzier)
        vystup += slovo[::-1] + " "
        # Program sa vrati na zaciatok slucky a pokracuje dalsim slovom
    # Ked sme vsetky slova prehodili tak vratime premennu vystup(veta so slovami od zadu)
    return vystup

# Tu urobime novu premennu s menom vystup_funkcie
# V tejto premennej ulozime vystup nasej funkcie prehod
# Ako vidis tak sme za argument veta dosadili premennu veta-> meno_funkcie(argumenty_dosadujeme)
vystup_funkcie = prehod(veta)
# Vypisujeme vystup funkcie
print(vystup_funkcie)
