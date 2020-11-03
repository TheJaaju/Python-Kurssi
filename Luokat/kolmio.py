#Leikitään luokilla ja piirretään kolmio

class Piirto():

    def __init__(self):
        self.height = 30
        self.height2 = self.height*2+1
        self. char1 = "#"
        self.char2 = " "

    def drawIt(self):
        for i in range(1,self.height,2):
            self.height = self.height - 1
            print(self.char2*self.height + self.char1*i)


draw = Piirto()

draw.drawIt()
