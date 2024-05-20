import random
zadana_hodnota = input("kolko chces hesiel: \n")

def heslo_gen(pocet):
	for i in range(int(pocet)):
		vystup = ""
		for i in range(8):
			vystup+=chr(random.randint(65, 90))
		
		print(vystup)
heslo_gen(zadana_hodnota)
