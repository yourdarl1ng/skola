string = "Pajton"
# Do range funkcie musi ist vzdy cislo!
# Dali sme string
#for i in range(string):
#    print(i)

len("Python") # Mozeme dosadit aj premennu
# Vypise pismenko podla indexu
for i in range(len(string)):
    print(string[i])
# vypise rook, preskoci z
r = "rozok"
print(r[0:2]+r[3:5])
# Syntax zapisu rezov
#[START : STOP : STEP]
print("ANDREJ"[:1:2])
# vypise jer, pretoze -1 to otoci
print("andrejka"[-3:-6:-1])


krabica = "andrejka"
for i in range(len(krabica)):
    print(krabica[i], i)
