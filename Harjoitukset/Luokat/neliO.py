#Leikitään luokilla ja piirretään ontto nelio

class Piirto():

    def __init__(self):
        self.height = 0
        self.width = 0
        self.char1 = "#"
        self.char2 = " "

    def drawIt(self):
        print(self.char1*self.height)
        for x in range(self.height):
        
            print(self.char1 + self.char2*self.width + self.char1)
        print(self.char1*self.height)

    def setValues(self):
        self.height = 10
        self.width = self.height - 2

draw = Piirto()

draw.setValues()
draw.drawIt()