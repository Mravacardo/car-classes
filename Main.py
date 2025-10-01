class car:

    def __init__(self, brand, fuel, colour, model):
        self.brand=brand
        self.fuel=fuel
        self.colour=colour
        self.model=model

    def getcolour(self):
        return self colour

    def setcolour(self, newcolour):
        self.colour=newcolour

    def showCar(self):
        print("Car - {} - {}, Fuel Type - {}, Colour - {}".format(self.brand, self.model, self.fuel, self.colour))

class SUV(Car):
    def __init__(self, brand, model, fuel, colour, transmission, turbo):
        Car.__init__(self, brand, model, fuel, colour)
        self.transmission = transmission
        self.turbo = turbo

    def showCar(self):
        print("Car - {} - {}, Fuel Type - {}, Colour - {}, Transmission - {}, Turbo True/False - {}".format(self.brand, self.model, self.fuel, self.colour, self.transmission, self.turbo))
