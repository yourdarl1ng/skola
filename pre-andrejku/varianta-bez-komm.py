veta = input("Zadaj vetu na prehod: ")
def prehod(veta2):
    vystup = ""
    for slovo in veta2.split():
        vystup += slovo[::-1] + " "
    return vystup
vystup_funkcie = prehod(veta)
print(vystup_funkcie)
