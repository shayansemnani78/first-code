import math
class motevazi:
    def __init__(self, border_1, border_2, angle):
        self.border_1=border_1
        self.border_2=border_2
        self.angle=angle


    def ertefae_calc (self):
        ertefae=(math.asin(math.radians(self.angle)) * self.border_2)
        return ertefae


    def space (self):
        print(self.ertefae_calc() * self.border_1)

    def area (self):
        print(self.border_2 * 2 + self.border_1 * 2)


masahat=motevazi(10, 5, 30)
masahat.space()







