# Harjoitellaan luokkien käyttöä

class Piirto():
    
    #alustetaan arvoja
    def __init__(self):
        self.koko = 4
        self.merkki = "#"

    def piirraNelio(self):
        for x in range(self.koko):
            print(self.merkki*self.koko)
    
    def muutaKoko(self, uusiKoko):
        self.koko = uusiKoko
    
    def muutaMerkki(self, uusiMerkki):
        self.merkki = uusiMerkki

piirretaan = Piirto()

piirretaan.piirraNelio()

print("Muutetaan Kokoa ja merkkiä")
piirretaan.muutaKoko(10)
piirretaan.muutaMerkki("X")
piirretaan.piirraNelio()

#print(piirretaan.koko, piirretaan.merkki)