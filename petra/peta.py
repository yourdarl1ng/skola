import time, os
retazec = "Mam 10 deti"

def petra(string):
    hehe = []
    for pismenko in range(len(string)):
        hehe.append(pismenko*" "+string[pismenko:])
    for pismenko in range(len(string)):
        hehe.append(string[:pismenko+1]+pismenko * " ")
    return hehe
while True:
    for veta in petra(retazec):
        time.sleep(0.3)
        print(veta)
        #os.system("cls")
