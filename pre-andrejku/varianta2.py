# Tu mame 2 premenne
# Obe drzia slova ROVNAKEJ dlzky(podstatne)

slovo1 = "Peter"
slovo2 = "Slaby"

# Definujeme funkciu prehod2
# Tato funkcia si pyta 2 argumenty
# Pre prve a druhe slovo
# Zluci slova doromady
# Nulty index k nultemu z druheho slova, prvy k prvemu atd
# Potom vrati vystupne slovo(uz zmiesane)
def prehod2(slovo1, slovo2):
    # Tu ulozime vystup funkcia, ktory je zatial prazny
    vystup = ""
    # tu ukladame index na ktorom sme, aby sme vedeli pridat pismenka z druheho slova
    index = 0
    # zaciatok slucky for
    # V riadiacej premennej pismeno sa uklada pismenko zo slova cez ktore postupne ide
    # (vzdy tam je len to 1 pismenko)
    for pismeno in slovo1:
        # do vystupu pridame pismenko zo slova 1 a potom pismenko z druheho slova s rovnakym indexom
        vystup += pismeno + slovo2[index]
        # Pripocitame index a pokracujeme na dalsie pismenko
        index+=1
    # Ked sa slucka skonci tak vratime vystup funkcie
    return vystup
# Tu vypiseme zmiesanie prveho a druheho slova
# Dosadili sme premenne za argumenty
print(prehod2(slovo1, slovo2))
