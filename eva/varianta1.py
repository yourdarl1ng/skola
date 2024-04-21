# Tu deklarujeme(vytvorime) 2 premenne
# Jedna je pre vetu ktoru pouzivatel napise
# Druha dzri hladane pismenko

# Tu je ulozena veta
retazec = input("zadaj vetu: ")
# Tu je ulozene pismenko
hladam = input("zadaj hladane pismenko: ")


# Tu definujeme funkciu s menom najdi
# Funkcia najdi si pyta 2 argumenty
# Jeden je veta v ktorej hladame a druhy je pismenko co hladame

# Tato funkcia najde kde vo vete( na akom indexe ) sa nachadza hladane pismenko
# Funguje na principe slucky for
# Ide pismenko po pismenku a ak najde ze sa zhoduju tak vrati nam jeho index
def najdi(veta, hladane_pismenko):
    
    # V tejto premennej budeme drzat index(preto som ju pomenoval index)
    index = 0
    
    # Tu zaciname slucku, postupne ideme cez pismenka vo vete
    for pismeno in veta:
        
        # Ak sa najde tak nasa funkcia vrati hodnotu premennej index
        if pismeno == hladane_pismenko:
            # Toto tu vracia tu hodnotu
            return index
        
        # Ak sa pismenko nenaslo tak pridame 1 ku indexu a pokracujeme
        # program sa vrati nazad na 24 riadok(if podmienku) a skusa dalsie pismenko
        index+=1
        
    # Tu konci nasa funkcia ak nenasla hladane pismenko
    # (Tu uz je mimo slucky)
    return "nenasiel som, skus ine pismenko."


# Urobime novu premennu a ukladame do nej vystup funkcie najdi
najdeny_index = najdi(retazec, hladam)
# Tu vypisujeme vysledok premennej vo vete za pomoci fstringu
print(f"Pismenko som nasiel na indexe {najdeny_index}")

