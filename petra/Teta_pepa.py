string = "mam 10 deti"

def peta(retazec):
	for i in range(len(retazec)):
		if i % 2 == 0:
			print(retazec[i])
peta(string)
