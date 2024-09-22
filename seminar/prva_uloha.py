class One:
    def __init__(self, string):
        self.__str = string
        self.symbol = "$"
        self.run()
    def run(self):
        for index in range(len(self.__str)):
            print(self.symbol*index + self.__str[index])
One(input("Zadajte retazec: "))

class Two:
    def __init__(self):
        self.__height = input("Zadajte svoju vysku v metroch: ")
        self.__weight = input("Zadajte svoju vahu v kg: ")
        self.run()
    def calc(self, h, w):
        # debilne zapisane ale co uz, potrebujeme floaty kvoli desatinnym cislam pri pocitani
        # ale int aby sme sa vo vysledku zbavili desatinnych cisel
        # a potom na string lebo zadanie tak kaze
        return str(int(float(w) / float(h)**2))
    def run(self):
        print(f"Vas BMI je: {self.calc(self.__height, self.__weight)}")
Two()

class Three:
    def __init__(self):
        self.__str = input("Zadajte retazec: ")
        self.__find = input("Zadajte hladany znak: ")
        self.run()
    def run(self):
        if self.__find in self.__str:
            print(f"{self.__find} sa nachadza v retazci")
            return True
        print(f"{self.__find} sa nenachadza v retazci :((((( strasne smutne :((")

Three()
