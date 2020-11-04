#Leikitään luokilla ja piirretään suorakulmio

class Piirto():

    def __init__(self):
        self.height = 5
        self.width = 50
        self.char = "#"

    def drawIt(self):
        for x in range(self.height):
            print(self.char*self.width)

draw = Piirto()

draw.drawIt()

