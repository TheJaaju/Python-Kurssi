#Leikitään luokilla ja piirretään kolmio

class Piirto():

    def __init__(self):
        self.width = 30
        self. char1 = "#"
        self.char2 = " "

    def drawIt(self):
        for i in range(1,self.width,2):
            self.width = self.width - 1
            print(self.char2*self.width + self.char1*i)


draw = Piirto()

draw.drawIt()
