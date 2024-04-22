# Vytvorili sme premennu string v ktorej bude ulozeny vstup 
# od pouzivatela
string = input("Zadaj dajaku vetu: ")

# Definujeme funkciu s menom peta
# Tato funkcia si pyta argument menom retazec
# (bez neho by to neslo)
def peta(retazec):
	# Tu sme vytvorili premennu vystup
	# V nej ulozime vystup funkcie, zatial prazdny
	vystup=""

	# Tu sa zacina slucka for
	# Tato slucka najprv zmeria dlzku retazca a nasledne 
	# ide cez jeho indexy, 0 1 2 3 atd(zalezi aky je dlhy)
	for i in range(len(retazec)):
		# Ak je dany index delitelny 2, tak sa pozreme ake pismenko je na danom indexe a 
		# pripiseme ho do premennej vystup
		if i % 2 == 0:
			vystup+=retazec[i]
	# Koniec slucky, vraciame vystup
	return vystup
# Spustame funkciu peta s premennou string dosadenou za argument
# A ukladame jej vystup do premennej vysledok
vysledok = peta(string)
# Vypisujeme vysledok
print(vysledok)
