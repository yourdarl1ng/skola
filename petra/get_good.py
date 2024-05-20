# importujeme kniznicu random
import random
# Tuna vytvorime premennu zadana_hodnota do ktorej bude ulozene kolko hesiel pouzivatel chce
zadana_hodnota = input("kolko chces hesiel: \n")
# Tu sa ulozi ako dlhe pouzivatel chce heslo
ako_dlhe = input("ako dlhe ces hesla: \n")
# Tu sa definuje funkcia heslo_gen s argumentom dlzka
def heslo_gen(dlzka):
	# Tu sa vytvori premenna vystup
	# Je v nej prazdny retazec pretoze tam budeme ukladat znaky
    vystup = ""
	# Pustime cyklus tolko krat kolko chceme znakov
    for i in range(int(dlzka)):
	# Pripiseme nahodne velke alebo male pismeno
	# Generuje sa vzdy 2, napr a K. potom sa vyberie 1 z nich ktore sa zapise
	vystup+=random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))])
	# Po skonceni cyklu sa hodi heslo ako navratova hodnota funkcie
    return vystup
# Pustame cyklus tolko krat kolko hesiel treba
for i in range(int(zadana_hodnota)):
# Vypisujeme vysledky funkcie heslo_gen s dosadenim argumentu ako dlhe chceme heslo
    print(heslo_gen(ako_dlhe))
