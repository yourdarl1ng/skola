import random
import os 
import time 
class TextAnim:
    def __init__(self, text):
        self.text = text 
        self.original = self.text
        self.consumed = ""
        self.delay = 0.15
        # Use whatever, does not matter
        self.charlist = ["A", "B", "C", "D", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "Z", "M", ")", "(", "F", "G", "H", "O", "P", "R", "S", "T", "V", "W", "Q"]
        self.draw()
    def consume(self, text):
        self.consumed+=text
        self.text = self.text[1:]
    def replace(self, char, index):
        self.text = self.text[:index] + str(char) + self.text[index+1:]
    def randomise(self):
        self.__iteration = 0
        
        for char in self.text:
            self.replace(random.choice(self.charlist), self.__iteration)
            self.__iteration+=1
        self.consume(self.original[int(len(self.consumed))])
    def draw(self):
        while self.text != "":
            print(self.consumed+self.text)
            self.randomise()
            time.sleep(float(self.delay))
            os.system("cls")
        print(self.consumed+self.text)
        
TextAnim("Boze toto zabralo 15 minut mojho casu :)")
