def scramble(string):
    for character in range(len(string)):
        if character % 2:
            print(string[character], end='')
    # Novy riadok
    print()
scramble(input('Zadaj Retazec: '))
# informatika
# i f r a i a
def scramble2(string):
    index = 0
    for ch in range(len(string)):
        if not index % 2:
            print(string[index], end='')
        index+=1
    print()
scramble2(input('Zadaj retazec: '))


def scramble3(string):
    for owo in string.split():
        print(owo[::-1], end=" ")
    print()

scramble3(input("Zadaj retazec: "))

def scramble4(string1, string2):
    final = ""
    loop = 0
    for chars in string1:
        final+=chars+string2[loop]
        loop+=1
    return final
print(scramble4(input("retazec1: "), input("retazec2: ")))
