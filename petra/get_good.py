import random
zadana_hodnota = input("kolko chces hesiel: \n")
ako_dlhe = input("ako dlhe ces hesla: \n")
def heslo_gen(dlzka):
    
    vystup = ""
    for i in range(int(dlzka)):
        nahoda = random.randint(1,2)
	
	if nahoda == 2:
	
	    vystup+=chr(random.randint(65, 90))
	else:
	    vystup+=chr(random.randint(97,122))
		
    return vystup
for i in range(int(zadana_hodnota)):
    print(heslo_gen(ako_dlhe))
